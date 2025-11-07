from django.urls import path
from . import views
from .views import (
    CamionListView, CamionCreateView, CamionUpdateView, CamionDeleteView,
    ChoferListView, ChoferCreateView, ChoferUpdateView, ChoferDeleteView
)

urlpatterns = [
    # Rutas de Camiones
    path("camiones/", views.CamionListView.as_view(), name="camion_lista"),
    path("camiones/nuevo/", views.CamionCreateView.as_view(), name="camion_crear"),
    path("camiones/editar/<int:pk>/", views.CamionUpdateView.as_view(), name="camion_editar"),
    path("camiones/borrar/<int:pk>/", views.CamionDeleteView.as_view(), name="camion_borrar"),

    # Rutas de Choferes
    path('choferes/', views.ChoferListView.as_view(), name='chofer_lista'),
    path('choferes/crear/', views.ChoferCreateView.as_view(), name='chofer_crear'),
    path('choferes/editar/<int:pk>/', views.ChoferUpdateView.as_view(), name='chofer_editar'),
    path('choferes/eliminar/<int:pk>/', views.ChoferDeleteView.as_view(), name='chofer_eliminar'),
]
