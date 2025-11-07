from django.db import models

class Viaje(models.Model):
    ESTADO_CHOICES = [
        ('Reservado', 'Reservado'),
        ('Confirmado', 'Confirmado'),
        ('Realizado', 'Realizado'),
        ('Cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey("contactos.Cliente", on_delete=models.CASCADE, related_name="viajes_operaciones")
    socio = models.ForeignKey('contactos.SocioNegocio', on_delete=models.SET_NULL, null=True, blank=True, related_name='viajes_enviados')
    camion = models.ForeignKey("flota.Camion", on_delete=models.CASCADE, related_name="viajes_operaciones")
    chofer = models.ForeignKey("flota.Chofer", on_delete=models.CASCADE, related_name="viajes_operaciones")
    
    destino = models.CharField(max_length=200)
    fecha_salida = models.DateTimeField()
    fecha_regreso = models.DateTimeField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Reservado')

    class Meta:
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'

    def __str__(self):
        return f"Viaje a {self.destino} ({self.fecha_salida.strftime('%d/%m/%Y')})"