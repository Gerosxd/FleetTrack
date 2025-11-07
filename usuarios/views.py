from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")  #Redirige al dashboard
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "usuarios/login.html")

def landing_view(request):
    return render(request, "usuarios/landing.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("dashboard")  # después de registrarse va al dashboard

    return render(request, "usuarios/register.html")

@login_required
def dashboard_view(request):
    user = request.user
    initials = user.username[:2].upper()  # primeras dos letras del usuario

    context = {
        "user": user,
        "initials": initials,
    }
    return render(request, "usuarios/dashboard.html", context)
