from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin  # 👈 Importante
from .models import Cliente
from .forms import ClienteForm
from .models import Cliente, SocioNegocio # <-- Asegúrate de importar SocioNegocio
from .forms import ClienteForm
# (Formulario para Socio)
from django import forms

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'contactos/cliente_list.html'
    context_object_name = 'clientes'
    login_url = 'login'  # 👈 Si no está logueado lo manda al login

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'contactos/cliente_form.html'
    success_url = reverse_lazy('cliente_lista')
    login_url = 'login'

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'contactos/cliente_form.html'
    success_url = reverse_lazy('cliente_lista')
    login_url = 'login'

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'contactos/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_lista')
    login_url = 'login'



class SocioNegocioForm(forms.ModelForm):
    class Meta:
        model = SocioNegocio
        fields = '__all__'

# --- VISTAS CRUD PARA SOCIOS DE NEGOCIO ---

class SocioNegocioListView(LoginRequiredMixin, ListView):
    model = SocioNegocio
    template_name = 'contactos/socio_list.html'
    context_object_name = 'socios'
    login_url = 'login'

class SocioNegocioCreateView(LoginRequiredMixin, CreateView):
    model = SocioNegocio
    form_class = SocioNegocioForm
    template_name = 'contactos/socio_form.html'
    success_url = reverse_lazy('socio_lista')
    login_url = 'login'

class SocioNegocioUpdateView(LoginRequiredMixin, UpdateView):
    model = SocioNegocio
    form_class = SocioNegocioForm
    template_name = 'contactos/socio_form.html'
    success_url = reverse_lazy('socio_lista')
    login_url = 'login'

class SocioNegocioDeleteView(LoginRequiredMixin, DeleteView):
    model = SocioNegocio
    template_name = 'contactos/socio_confirm_delete.html'
    success_url = reverse_lazy('socio_lista')
    login_url = 'login'