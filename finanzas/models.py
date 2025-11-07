from django.db import models
from contactos.models import Cliente, SocioNegocio
from flota.models import Camion, Chofer
from operaciones.models import Viaje


class Ingreso(models.Model):
    viaje = models.OneToOneField(Viaje, on_delete=models.CASCADE, related_name="ingreso") #
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Ingreso {self.monto} - {self.viaje.destino}"


class Gasto(models.Model):
    camion = models.ForeignKey(Camion, on_delete=models.SET_NULL, null=True, blank=True, related_name="gastos")
    chofer = models.ForeignKey(Chofer, on_delete=models.SET_NULL, null=True, blank=True, related_name="gastos")
    categoria = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Gasto {self.categoria} - {self.monto}"
