from rest_framework import serializers
from .models import Usuario, Cuidador, Administrador, Animal, DatoVeterinario, IndicadorSalud, ControlMedico, SeguimientoCondicion, Alergia, Medicamento, Reporte

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'nombre_completo', 'numero_celular']
        extra_kwargs = {'password': {'write_only': True}}

class CuidadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuidador
        fields = ['id', 'username', 'email', 'nombre_completo', 'numero_celular']
        extra_kwargs = {'password': {'write_only': True}}

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ['id', 'username', 'email', 'nombre_completo', 'numero_celular']
        extra_kwargs = {'password': {'write_only': True}}

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class DatoVeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatoVeterinario
        fields = '__all__'

class IndicadorSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicadorSalud
        fields = '__all__'

class ControlMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlMedico
        fields = '__all__'

class SeguimientoCondicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguimientoCondicion
        fields = '__all__'

class AlergiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergia
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'
