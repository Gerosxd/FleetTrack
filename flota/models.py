from django.db import models

class Camion(models.Model):
    placas = models.CharField(max_length=20, unique=True, verbose_name="Número de placas")
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(verbose_name="Año de fabricación")
    capacidad = models.IntegerField(verbose_name="Capacidad de pasajeros")
    estado = models.CharField(max_length=20, default='Disponible', choices=[('Disponible', 'Disponible'), ('Mantenimiento', 'Mantenimiento'), ('En Viaje', 'En Viaje')])

    class Meta:
        verbose_name = 'Camión'
        verbose_name_plural = 'Camiones'

    def __str__(self):
        return f"{self.modelo} - {self.placas}"

# En flota/models.py

class Chofer(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre completo")
    licencia = models.CharField(max_length=50, unique=True, verbose_name="Número de licencia")
    telefono = models.CharField(max_length=20)
    direccion = models.TextField(null=True, blank=True)
    # --- CAMPO AÑADIDO ---
    estado = models.CharField(max_length=20, default="Disponible") 
    
    class Meta:
        verbose_name = 'Chófer'
        verbose_name_plural = 'Choferes'

    def __str__(self):
        return self.nombre

class Mantenimiento(models.Model):
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE, related_name='mantenimientos')
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return f"Mantenimiento a {self.camion.placas} - {self.fecha}"