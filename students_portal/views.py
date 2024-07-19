from django.shortcuts import render
from alumnos.models import Alumno
from django.contrib.auth.decorators import login_required

@login_required
def menu_stud(request):
    request.session["usuario"] = "jcisterna"
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'students_portal/menu_stud', context)

def home_stud(request):
    context = {}
    return render(request, 'students_portal/home_stud.html', context)

def nosotros_stud(request):
    context = {}
    return render(request, 'students_portal/nosotros_stud.html', context)

def contactos_stud(request):
    context = {}
    return render(request, 'students_portal/contactos_stud.html', context)

