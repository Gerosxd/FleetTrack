from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Viaje
from .forms import ViajeForm


class ViajeListView(ListView):
    model = Viaje
    template_name = "operaciones/lista_viajes.html"
    context_object_name = "viajes"
    ordering = ["-fecha_salida"]


class ViajeCreateView(CreateView):
    model = Viaje
    template_name = "operaciones/crear_viaje.html"
    form_class = ViajeForm  # <-- Usamos el form_class
    success_url = reverse_lazy("lista_viajes")


class ViajeUpdateView(UpdateView):
    model = Viaje
    template_name = "operaciones/crear_viaje.html"  # Reutiliza el template de crear
    form_class = ViajeForm  # <-- Usamos el form_class
    success_url = reverse_lazy("lista_viajes")


class ViajeDeleteView(DeleteView):
    model = Viaje
    template_name = "operaciones/borrar_viaje.html"
    success_url = reverse_lazy("lista_viajes")
