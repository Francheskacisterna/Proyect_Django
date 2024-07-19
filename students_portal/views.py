from django.shortcuts import render
from alumnos.models import Alumno
from django.contrib.auth.decorators import login_required

@login_required
def menu(request):
    request.session["usuario"] = "jcisterna"
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'students_portal/menu_stud', context)

def home_adm(request):
    context = {}
    return render(request, 'students_portal/home_stud.html', context)

def nosotros_adm(request):
    context = {}
    return render(request, 'students_portal/nosotros_stud.html', context)

def contactos_adm(request):
    context = {}
    return render(request, 'students_portal/contactos_stud.html', context)

@login_required
def dashboard(request):
    if request.user.user_type == 1:  # Admin
        return render(request, 'menu_.html')
    elif request.user.user_type == 2:  # Profesor
        return render(request, 'menu_prof.html')
    elif request.user.user_type == 3:  # Estudiante
        return render(request, 'menu_stud.html')
    else:
        return redirect('home')
