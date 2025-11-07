# contactos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs de Clientes
    path('', views.ClienteListView.as_view(), name='cliente_lista'),
    path('nuevo/', views.ClienteCreateView.as_view(), name='cliente_crear'),
    path('editar/<int:pk>/', views.ClienteUpdateView.as_view(), name='cliente_editar'),
    path('borrar/<int:pk>/', views.ClienteDeleteView.as_view(), name='cliente_borrar'),
    
    # --- LÍNEAS PARA SOCIOS ---
    path('socios/', views.SocioNegocioListView.as_view(), name='socio_lista'),
    path('socios/nuevo/', views.SocioNegocioCreateView.as_view(), name='socio_crear'),
    path('socios/editar/<int:pk>/', views.SocioNegocioUpdateView.as_view(), name='socio_editar'),
    path('socios/borrar/<int:pk>/', views.SocioNegocioDeleteView.as_view(), name='socio_borrar'),
]