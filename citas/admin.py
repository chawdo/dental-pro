from django.contrib import admin
from .models import Paciente

# Configuración para que el panel se vea más profesional
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'telefono') # Columnas que verás en la lista
    search_fields = ('nombre', 'apellido', 'cedula')            # Barra de búsqueda
    list_filter = ('fecha_registro',)                           # Filtros laterales

admin.site.register(Paciente, PacienteAdmin)

from .models import Cita # Asegúrate de importar Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha', 'hora', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('paciente__nombre', 'paciente__apellido') # Busca por nombre del paciente vinculado