from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators  import login_required


def home(request):
    return render(request, "home.html")

@login_required
def tareas(request):
    if request.method == "GET":
        return render(request, "tareas.html")
    else:
        try:
            x = float(request.POST["alto"])
            y = float(request.POST["ancho"])
            z = float(request.POST["calibre"])
            m = float(request.POST["material"])
            r1 = x*y*z
            r2 = 1000/r1
            merma = r2 * 0.07
            r3 = r2 - merma
            p = round(m / r3, 2)
            i = request.POST["interno"]
            return render(request, "tareas.html", {
                "prince": f"precio: {p}",
                "alto": f"alto: {x}",
                "ancho": f"ancho: {y}",
                "calibre": f"calibre: {z}",
                "material": f"material: {m}"
                    })
        except:
            x = float(request.POST["alto"])
            y = float(request.POST["ancho"])
            z = float(request.POST["calibre"])
            m = float(request.POST["material"])
            r1 = x*y*z
            r2 = 1000/r1
            merma = r2 * 0.07
            r3 = r2 - merma 
            p2 = round(m / r3, 2)
            p1 = p2 * 0.12
            p = round(p2 + p1, 2)
            return render(request, "tareas.html", {
                "prince": f"precio: $ {p}",
                "precio": f"precio fabrica $ {p2}",
                "alto": f"alto: {x} cm",
                "ancho": f"ancho: {y} cm",
                "calibre": f"calibre: {z} micras",
                "material": f"material: {m}"
                    })                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        
def registro(request):
    if request.method == "GET":
        return render(request, "singup.html", {
            "formulario": UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                Usuario = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                Usuario.save()
                login(request, Usuario)
                return redirect("tareas")
            except:
                return render(request, "singup.html", {
                    "formulario": UserCreationForm,
                    "error": "El usuario ya existe"
                })
        return render(request, "singup.html", {
            "formulario": UserCreationForm,
            "error": "Contraseña invalida"
        })

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect("/")


def iniciarSesion(request):
    if request.method == "GET":
        return render(request, "singin.html", {
            "form": AuthenticationForm
        })
    else:
        Usuario = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if Usuario is None:
            return render(request, "singin.html", {
                "form": AuthenticationForm,
                "error": "La contraseña y el usuario no coinsiden"
            })
        else:
            login(request, Usuario)
            return redirect("tareas")
        
        