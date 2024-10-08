from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Verificar si el usuario existe y está activo
        try:
            user = User.objects.get(username=attrs['username'])
            if not user.is_active:
                raise serializers.ValidationError(
                    {"detail": "La cuenta no está activa."}
                )
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"detail": "No se encontró una cuenta con estas credenciales."}
            )

        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
