from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    nombre_completo = models.CharField(max_length=100)
    numero_celular = models.CharField(max_length=20)
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="usuario_set",
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="usuario_set",
        related_query_name="usuario",
    )


class Cuidador(Usuario):
    class Meta:
        permissions = [
            ("registrar_condicion_salud", "Puede registrar condición de salud"),
            ("registrar_dato_veterinario", "Puede registrar dato veterinario"),
            ("registrar_indicador_salud", "Puede registrar indicador de salud"),
            ("registrar_control_medico", "Puede registrar control médico"),
            (
                "registrar_seguimiento_condicion",
                "Puede registrar seguimiento de condición",
            ),
        ]


class Administrador(Usuario):
    class Meta:
        permissions = [
            ("asignar_animal_cuidador", "Puede asignar animal a cuidador"),
            ("generar_reporte", "Puede generar reporte"),
        ]


class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    tipo_comida = models.CharField(max_length=100)
    marca_comida = models.CharField(max_length=100)
    necesidades_aseo = models.TextField()
    necesidades_aseo_habitat = models.TextField()
    fecha_nacimiento = models.DateField(null=True, blank=True)
    cuidadores = models.ManyToManyField(Cuidador, related_name="animales")
    imagen = models.ImageField(upload_to="animales/", null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    sexo = models.CharField(max_length=1, choices=[('M', 'Macho'), ('H', 'Hembra')], null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    peso_actual = models.FloatField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=[
        ('SANO', 'Sano'),
        ('ENFERMO', 'Enfermo'),
        ('EN_TRATAMIENTO', 'En tratamiento'),
        ('CUARENTENA', 'En cuarentena')
    ], default='SANO')

    def obtener_historial_salud(self):
        return RegistroSalud.objects.filter(animal=self).order_by("-fecha")

    def obtener_todos_registros_salud(self):
        return sorted(
            list(self.datoveterinario_registros.all())
            + list(self.indicadorsalud_registros.all())
            + list(self.controlmedico_registros.all())
            + list(self.seguimientocondicion_registros.all()),
            key=lambda x: x.fecha,
            reverse=True,
        )

    def __str__(self):
        return f"{self.nombre} - {self.especie}"


class RegistroSalud(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name="%(class)s_registros"
    )
    fecha = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField()
    registrado_por = models.ForeignKey(Cuidador, on_delete=models.SET_NULL, null=True)
    tipo = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.tipo:
            self.tipo = self.__class__.__name__
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class DatoVeterinario(RegistroSalud):
    procedimiento = models.CharField(max_length=200)
    resultado_examen = models.TextField()
    recomendaciones = models.TextField()
    imagenes = models.JSONField(default=list)

    class Meta:
        verbose_name = "Dato Veterinario"
        verbose_name_plural = "Datos Veterinarios"


class IndicadorSalud(RegistroSalud):
    peso = models.FloatField(null=True, blank=True)
    vacunas = models.JSONField(default=list)
    estado_fisico = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Indicador de Salud"
        verbose_name_plural = "Indicadores de Salud"


class ControlMedico(RegistroSalud):
    nombre_profesional = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Control Médico"
        verbose_name_plural = "Controles Médicos"


class SeguimientoCondicion(RegistroSalud):
    fecha_incidente = models.DateField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    evolucion = models.TextField()

    class Meta:
        verbose_name = "Seguimiento de Condición"
        verbose_name_plural = "Seguimientos de Condición"


class Alergia(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name="alergias"
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()


class Medicamento(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name="medicamentos"
    )
    nombre = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)


class Reporte(models.Model):
    TIPO_CHOICES = [
        ("ANIMAL", "Por Animal"),
        ("CUIDADOR", "Por Cuidador"),
    ]
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    generado_por = models.ForeignKey(
        Administrador, on_delete=models.SET_NULL, null=True
    )
    contenido = models.JSONField(default=dict)

    def save(self, *args, **kwargs):
        if self.tipo == "ANIMAL":
            self.contenido = self.generar_reporte_por_animal()
        elif self.tipo == "CUIDADOR":
            self.contenido = self.generar_reporte_por_cuidador()
        super().save(*args, **kwargs)

    def generar_reporte_por_animal(self):
        from django.db.models import Count, Avg

        animales = Animal.objects.all()
        return [
            {
                "animal": animal.nombre,
                "especie": animal.especie,
                "cantidad_datos_veterinarios": animal.datoveterinario_registros.filter(
                    fecha__range=[self.fecha_inicio, self.fecha_fin]
                ).count(),
                "cantidad_indicadores_salud": animal.indicadorsalud_registros.filter(
                    fecha__range=[self.fecha_inicio, self.fecha_fin]
                ).count(),
                "cantidad_controles_medicos": animal.controlmedico_registros.filter(
                    fecha__range=[self.fecha_inicio, self.fecha_fin]
                ).count(),
                "peso_promedio": animal.indicadorsalud_registros.filter(
                    fecha__range=[self.fecha_inicio, self.fecha_fin]
                ).aggregate(Avg("peso"))["peso__avg"],
                "ultima_visita_veterinaria": (
                    animal.datoveterinario_registros.filter(
                        fecha__range=[self.fecha_inicio, self.fecha_fin]
                    )
                    .order_by("-fecha")
                    .first()
                    .fecha
                    if animal.datoveterinario_registros.filter(
                        fecha__range=[self.fecha_inicio, self.fecha_fin]
                    ).exists()
                    else None
                ),
            }
            for animal in animales
        ]

    def generar_reporte_por_cuidador(self):
        from django.db.models import Count

        cuidadores = Cuidador.objects.all()
        return [
            {
                "cuidador": cuidador.nombre_completo,
                "cantidad_animales": cuidador.animales.count(),
                "cantidad_registros_salud": sum(
                    [
                        cuidador.datoveterinario_set.filter(
                            fecha__range=[self.fecha_inicio, self.fecha_fin]
                        ).count(),
                        cuidador.indicadorsalud_set.filter(
                            fecha__range=[self.fecha_inicio, self.fecha_fin]
                        ).count(),
                        cuidador.controlmedico_set.filter(
                            fecha__range=[self.fecha_inicio, self.fecha_fin]
                        ).count(),
                        cuidador.seguimientocondicion_set.filter(
                            fecha__range=[self.fecha_inicio, self.fecha_fin]
                        ).count(),
                    ]
                ),
                "tipos_registros": {
                    "datos_veterinarios": cuidador.datoveterinario_set.filter(
                        fecha__range=[self.fecha_inicio, self.fecha_fin]
                    ).count(),
                    "indicadores_salud": cuidador.indicadorsalud_set.filter(
                        fecha__range=[self.fecha_inicio, self.fecha_fin]
                    ).count(),
                    "controles_medicos": cuidador.controlmedico_set.filter(
                        fecha__range=[self.fecha_inicio, self.fecha_fin]
                    ).count(),
                    "seguimientos_condicion": cuidador.seguimientocondicion_set.filter(
                        fecha__range=[self.fecha_inicio, self.fecha_fin]
                    ).count(),
                },
                "ultimo_registro": (
                    max(
                        [
                            cuidador.datoveterinario_set.filter(
                                fecha__range=[self.fecha_inicio, self.fecha_fin]
                            )
                            .order_by("-fecha")
                            .first(),
                            cuidador.indicadorsalud_set.filter(
                                fecha__range=[self.fecha_inicio, self.fecha_fin]
                            )
                            .order_by("-fecha")
                            .first(),
                            cuidador.controlmedico_set.filter(
                                fecha__range=[self.fecha_inicio, self.fecha_fin]
                            )
                            .order_by("-fecha")
                            .first(),
                            cuidador.seguimientocondicion_set.filter(
                                fecha__range=[self.fecha_inicio, self.fecha_fin]
                            )
                            .order_by("-fecha")
                            .first(),
                        ],
                        key=lambda x: x.fecha if x else None,
                    ).fecha
                    if any(
                        [
                            cuidador.datoveterinario_set.filter(
                                fecha__range=[self.fecha_inicio, self.fecha_fin]
                            ).exists(),
                            cuidador.indicadorsalud_set.filter(
                                fecha__range=[self.fecha_inicio, self.fecha_fin]
                            ).exists(),
                            cuidador.controlmedico_set.filter(
                                fecha__range=[self.fecha_inicio, self.fecha_fin]
                            ).exists(),
                            cuidador.seguimientocondicion_set.filter(
                                fecha__range=[self.fecha_inicio, self.fecha_fin]
                            ).exists(),
                        ]
                    )
                    else None
                ),
            }
            for cuidador in cuidadores
        ]
