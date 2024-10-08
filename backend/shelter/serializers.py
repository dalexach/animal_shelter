from rest_framework import serializers
from .models import (
    Usuario,
    Cuidador,
    Administrador,
    Animal,
    DatoVeterinario,
    IndicadorSalud,
    ControlMedico,
    SeguimientoCondicion,
    Alergia,
    Medicamento,
    Reporte,
)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "username", "email", "nombre_completo", "numero_celular"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)
        return super().update(instance, validated_data)


class CuidadorSerializer(UsuarioSerializer):
    class Meta(UsuarioSerializer.Meta):
        model = Cuidador


class AdministradorSerializer(UsuarioSerializer):
    class Meta(UsuarioSerializer.Meta):
        model = Administrador


class AlergiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergia
        fields = "__all__"


class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = "__all__"


class AnimalSerializer(serializers.ModelSerializer):
    alergias = AlergiaSerializer(many=True, read_only=True)
    medicamentos = MedicamentoSerializer(many=True, read_only=True)
    cuidadores = CuidadorSerializer(many=True, read_only=True)

    class Meta:
        model = Animal
        fields = "__all__"


class RegistroSaludSerializer(serializers.ModelSerializer):
    registrado_por = CuidadorSerializer(read_only=True)

    class Meta:
        abstract = True
        fields = ["id", "animal", "fecha", "observaciones", "registrado_por", "tipo"]


class DatoVeterinarioSerializer(RegistroSaludSerializer):
    class Meta(RegistroSaludSerializer.Meta):
        model = DatoVeterinario
        fields = RegistroSaludSerializer.Meta.fields + [
            "procedimiento",
            "resultado_examen",
            "recomendaciones",
            "imagenes",
        ]


class IndicadorSaludSerializer(RegistroSaludSerializer):
    class Meta(RegistroSaludSerializer.Meta):
        model = IndicadorSalud
        fields = RegistroSaludSerializer.Meta.fields + [
            "peso",
            "vacunas",
            "estado_fisico",
        ]


class ControlMedicoSerializer(RegistroSaludSerializer):
    class Meta(RegistroSaludSerializer.Meta):
        model = ControlMedico
        fields = RegistroSaludSerializer.Meta.fields + [
            "nombre_profesional",
            "especialidad",
        ]


class SeguimientoCondicionSerializer(RegistroSaludSerializer):
    class Meta(RegistroSaludSerializer.Meta):
        model = SeguimientoCondicion
        fields = RegistroSaludSerializer.Meta.fields + [
            "fecha_incidente",
            "diagnostico",
            "tratamiento",
            "evolucion",
        ]


class ReporteSerializer(serializers.ModelSerializer):
    generado_por = AdministradorSerializer(read_only=True)

    class Meta:
        model = Reporte
        fields = "__all__"


class AnimalDetalladoSerializer(AnimalSerializer):
    datos_veterinarios = DatoVeterinarioSerializer(
        many=True, read_only=True, source="datoveterinario_registros"
    )
    indicadores_salud = IndicadorSaludSerializer(
        many=True, read_only=True, source="indicadorsalud_registros"
    )
    controles_medicos = ControlMedicoSerializer(
        many=True, read_only=True, source="controlmedico_registros"
    )
    seguimientos_condicion = SeguimientoCondicionSerializer(
        many=True, read_only=True, source="seguimientocondicion_registros"
    )

    class Meta(AnimalSerializer.Meta):
        model = Animal
        fields = list(AnimalSerializer.Meta.fields) + [
            "datos_veterinarios",
            "indicadores_salud",
            "controles_medicos",
            "seguimientos_condicion",
        ]
