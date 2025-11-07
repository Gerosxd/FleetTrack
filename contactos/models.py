from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100, unique=True)
    direccion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre

class SocioNegocio(models.Model):
    nombre_empresa = models.CharField(max_length=150, verbose_name="Nombre o Razón Social")
    contacto = models.CharField(max_length=100, verbose_name="Persona de contacto")
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100, unique=True, verbose_name="Correo del socio")

    class Meta:
        verbose_name = 'Socio de Negocio'
        verbose_name_plural = 'Socios de Negocio'

    def __str__(self):
        return self.nombre_empresa