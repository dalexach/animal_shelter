from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'cuidadores', views.CuidadorViewSet)
router.register(r'administradores', views.AdministradorViewSet)
router.register(r'animales', views.AnimalViewSet)
router.register(r'datos-veterinarios', views.DatoVeterinarioViewSet)
router.register(r'indicadores-salud', views.IndicadorSaludViewSet)
router.register(r'controles-medicos', views.ControlMedicoViewSet)
router.register(r'seguimientos-condicion', views.SeguimientoCondicionViewSet)
router.register(r'alergias', views.AlergiaViewSet)
router.register(r'medicamentos', views.MedicamentoViewSet)
router.register(r'reportes', views.ReporteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
