from rest_framework import serializers
from .models import Paciente, Cita

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__' # Esto incluye todos los campos (nombre, cédula, etc.)

class CitaSerializer(serializers.ModelSerializer):
    # Esto es para que en la cita veamos el nombre del paciente y no solo su ID
    paciente_nombre = serializers.ReadOnlyField(source='paciente.nombre')

    class Meta:
        model = Cita
        fields = '__all__'