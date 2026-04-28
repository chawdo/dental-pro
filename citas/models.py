from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True) # Para que no se repitan
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True) # Puede quedar vacío
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True) # Se pone sola al crear

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Cita(models.Model):
    # Opciones para el estado de la cita
    ESTADOS = [
        ('programada', 'Programada'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    # --- NUEVOS CAMPOS FINANCIEROS ---
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    monto_pagado_adelantado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    monto_pagado_dia = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    metodo_pago = models.CharField(max_length=100, default="Efectivo")


    # Relación: Si borras al paciente, se borran sus citas (on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField(max_length=500)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='programada')
    notas_medicas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cita de {self.paciente} el {self.fecha} a las {self.hora}"