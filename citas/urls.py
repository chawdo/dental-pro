from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet, CitaViewSet

# El router crea automáticamente las URLs para nosotros
router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'citas', CitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]