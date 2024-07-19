from django.shortcuts import render
from alumnos.models import Alumno
from django.contrib.auth.decorators import login_required

@login_required
def menu_prof(request):
    request.session["usuario"] = "b"
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'user_prof/menu_adm.html', context)

def home_prof(request):
    context = {}
    return render(request, 'user_prof/home_prof.html', context)

def planes_prof(request):
    context = {}
    return render(request, 'user_prof/planes_prof.html', context)

def nosotros_prof(request):
    context = {}
    return render(request, 'user_prof/nosotros_prof.html', context)

def contactos_prof(request):
    context = {}
    return render(request, 'user_prof/contactos_prof.html', context)

