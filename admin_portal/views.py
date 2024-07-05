
from django.shortcuts import render
from alumnos.models import Alumno
from django.contrib.auth.decorators import login_required

@login_required
def menu(request):
    # luego modificaremos esto ya que tenemos autenticación...
    request.session["usuario"] = "fcisterna"
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'admin_portal/menu.html', context)

def home(request):
    context = {}
    return render(request, 'admin_portal/home.htlm', context)

def reporte_alumnos(request):
    alumnos = Alumno.objects.all()  # Puedes agregar filtros si es necesario
    return render(request, 'alumnos/reporte_alumnos.html', {'alumnos': alumnos})

