from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username)
            if not user.is_active:
                raise serializers.ValidationError(
                    {"detail": "La cuenta no está activa."}
                )
            if not check_password(password, user.password):
                raise serializers.ValidationError(
                    {"detail": "Contraseña incorrecta."}
                )
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"detail": "No se encontró una cuenta con estas credenciales."}
            )

        data = super().validate(attrs)
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
