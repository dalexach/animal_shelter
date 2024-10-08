from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            user = User.objects.get(username=attrs['username'])
            if not user.is_active:
                raise serializers.ValidationError({"detail": "La cuenta no está activa."})

            authenticate_kwargs = {
                'username': attrs['username'],
                'password': attrs['password'],
            }
            user = authenticate(**authenticate_kwargs)
            if user is None:
                raise serializers.ValidationError({"detail": "Credenciales inválidas."})

            data = super().validate(attrs)
            return data
        except ObjectDoesNotExist:
            raise serializers.ValidationError({"detail": "No se encontró una cuenta con estas credenciales."})

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
