from django.contrib import admin
from django.urls import path, include
from usuarios import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Landing como página de inicio
    path("", views.landing_view, name="landing"),

    # Autenticación
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("dashboard/", views.dashboard_view, name="dashboard"),

    # CRUD adicionales
    path("clientes/", include("contactos.urls")),   # Clientes
    path("flota/", include("flota.urls")),         # Camiones (opción B)
    path("viajes/", include("operaciones.urls")),  # ¡ESTA ES LA CLAVE!
]
