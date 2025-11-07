from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin  # 👈 Importante
from .forms import CamionForm
from .models import Camion, Chofer

class CamionListView(LoginRequiredMixin, ListView):
    model = Camion
    template_name = 'flota/camion_list.html'
    context_object_name = 'camiones'
    login_url = 'login'

class CamionCreateView(LoginRequiredMixin, CreateView):
    model = Camion
    form_class = CamionForm
    template_name = 'flota/camion_form.html'
    success_url = reverse_lazy('camion_lista')
    login_url = 'login'

class CamionUpdateView(LoginRequiredMixin, UpdateView):
    model = Camion
    form_class = CamionForm
    template_name = 'flota/camion_form.html'
    success_url = reverse_lazy('camion_lista')
    login_url = 'login'

class CamionDeleteView(LoginRequiredMixin, DeleteView):
    model = Camion
    template_name = 'flota/camion_confirm_delete.html'
    success_url = reverse_lazy('camion_lista')
    login_url = 'login'


from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Chofer

class ChoferListView(ListView):
    model = Chofer
    template_name = 'flota/chofer_list.html' 
    context_object_name = 'choferes'

class ChoferCreateView(CreateView):
    model = Chofer
    template_name = 'flota/chofer_form.html'  
    fields = ['nombre', 'licencia', 'telefono', 'estado']
    success_url = reverse_lazy('chofer_lista')

class ChoferUpdateView(UpdateView):
    model = Chofer
    template_name = 'flota/chofer_form.html'  
    fields = ['nombre', 'licencia', 'telefono', 'estado']
    success_url = reverse_lazy('chofer_lista')

class ChoferDeleteView(DeleteView):
    model = Chofer
    template_name = 'flota/chofer_confirm_delete.html'
    success_url = reverse_lazy('chofer_lista')