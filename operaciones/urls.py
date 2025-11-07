from django.urls import path
from . import views

urlpatterns = [
    path("", views.ViajeListView.as_view(), name="lista_viajes"),
    path("nuevo/", views.ViajeCreateView.as_view(), name="crear_viaje"),
    path("editar/<int:pk>/", views.ViajeUpdateView.as_view(), name="viaje_editar"),
    path("borrar/<int:pk>/", views.ViajeDeleteView.as_view(), name="viaje_borrar"),
]
