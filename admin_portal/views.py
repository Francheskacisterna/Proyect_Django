
from django.shortcuts import render
from alumnos.models import Alumno
from django.contrib.auth.decorators import login_required

@login_required
def menu(request):
    request.session["usuario"] = "fcisterna"
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'admin_portal/menu.html', context)

def home_adm(request):
    context = {}
    return render(request, 'admin_portal/home_adm.html', context)

def reporte_alumnos(request):
    alumnos = Alumno.objects.all()  
    return render(request, 'alumnos/reporte_alumnos.html', {'alumnos': alumnos})

def planes_adm(request):
    context = {}
    return render(request, 'admin_portal/planes_adm.html', context)

def nosotros_adm(request):
    context = {}
    return render(request, 'admin_portal/nosotros_adm.html', context)

def contactos_adm(request):
    context = {}
    return render(request, 'admin_portal/contactos_adm.html', context)

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
