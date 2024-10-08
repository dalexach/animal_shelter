from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
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
from .serializers import (
    UsuarioSerializer,
    CuidadorSerializer,
    AdministradorSerializer,
    AnimalSerializer,
    DatoVeterinarioSerializer,
    IndicadorSaludSerializer,
    ControlMedicoSerializer,
    SeguimientoCondicionSerializer,
    AlergiaSerializer,
    MedicamentoSerializer,
    ReporteSerializer,
)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAdminUser]


class CuidadorViewSet(viewsets.ModelViewSet):
    queryset = Cuidador.objects.all()
    serializer_class = CuidadorSerializer
    permission_classes = [permissions.IsAdminUser]


class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    permission_classes = [permissions.IsAdminUser]


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["get"])
    def historial_salud(self, request, pk=None):
        animal = self.get_object()
        historial = animal.obtener_historial_salud()
        serializer = DatoVeterinarioSerializer(historial, many=True)
        return Response(serializer.data)


class DatoVeterinarioViewSet(viewsets.ModelViewSet):
    queryset = DatoVeterinario.objects.all()
    serializer_class = DatoVeterinarioSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndicadorSaludViewSet(viewsets.ModelViewSet):
    queryset = IndicadorSalud.objects.all()
    serializer_class = IndicadorSaludSerializer
    permission_classes = [permissions.IsAuthenticated]


class ControlMedicoViewSet(viewsets.ModelViewSet):
    queryset = ControlMedico.objects.all()
    serializer_class = ControlMedicoSerializer
    permission_classes = [permissions.IsAuthenticated]


class SeguimientoCondicionViewSet(viewsets.ModelViewSet):
    queryset = SeguimientoCondicion.objects.all()
    serializer_class = SeguimientoCondicionSerializer
    permission_classes = [permissions.IsAuthenticated]


class AlergiaViewSet(viewsets.ModelViewSet):
    queryset = Alergia.objects.all()
    serializer_class = AlergiaSerializer
    permission_classes = [permissions.IsAuthenticated]


class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=True, methods=["get"])
    def generar(self, request, pk=None):
        reporte = self.get_object()
        if reporte.tipo == "ANIMAL":
            data = reporte.generar_reporte_por_animal()
        else:
            data = reporte.generar_reporte_por_cuidador()
        return Response(data)
