from django.contrib import admin
from .models import Camion, Chofer, Mantenimiento

admin.site.register(Camion)
admin.site.register(Chofer)
admin.site.register(Mantenimiento)