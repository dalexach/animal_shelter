from django.contrib import admin
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


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "nombre_completo", "numero_celular")
    search_fields = ("username", "email", "nombre_completo")


@admin.register(Cuidador)
class CuidadorAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "nombre_completo", "numero_celular")
    search_fields = ("username", "email", "nombre_completo")


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "nombre_completo", "numero_celular")
    search_fields = ("username", "email", "nombre_completo")


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especie", "habitat")
    search_fields = ("nombre", "especie")
    filter_horizontal = ("cuidadores",)


@admin.register(DatoVeterinario)
class DatoVeterinarioAdmin(admin.ModelAdmin):
    list_display = ("animal", "fecha", "procedimiento")
    list_filter = ("fecha", "animal")


@admin.register(IndicadorSalud)
class IndicadorSaludAdmin(admin.ModelAdmin):
    list_display = ("animal", "fecha", "peso", "estado_fisico")
    list_filter = ("fecha", "animal")


@admin.register(ControlMedico)
class ControlMedicoAdmin(admin.ModelAdmin):
    list_display = ("animal", "fecha", "nombre_profesional", "especialidad")
    list_filter = ("fecha", "animal")


@admin.register(SeguimientoCondicion)
class SeguimientoCondicionAdmin(admin.ModelAdmin):
    list_display = ("animal", "fecha", "fecha_incidente", "diagnostico")
    list_filter = ("fecha", "animal")


@admin.register(Alergia)
class AlergiaAdmin(admin.ModelAdmin):
    list_display = ("animal", "nombre")
    search_fields = ("animal__nombre", "nombre")


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ("animal", "nombre", "dosis", "frecuencia")
    search_fields = ("animal__nombre", "nombre")


@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ("fecha_inicio", "fecha_fin", "tipo", "generado_por")
    list_filter = ("tipo", "fecha_inicio", "fecha_fin")
