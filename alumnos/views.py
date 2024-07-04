from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Alumno, Genero, Tutor
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home(request):
    context = {}
    return render(request, 'alumnos/home.html', context)

def planes(request):
    context = {}
    return render(request, 'alumnos/planes.html', context)

def servicios(request):
    context = {}
    return render(request, 'alumnos/servicios.html', context)

def nosotros(request):
    context = {}
    return render(request, 'alumnos/nosotros.html', context)

def contactos(request):
    context = {}
    return render(request, 'alumnos/contactos.html', context)

def simulador(request):
    context = {}
    return render(request, 'alumnos/simulador.html', context)


def opcion_user(request):
    context = {}
    return render(request, 'alumnos/opcion_user.html', context)

def regis_alum(request):
    context = {}
    return render(request, 'alumnos/regis_alum.html', context)

def regis_prof(request):
    context = {}
    return render(request, 'alumnos/regis_prof.html', context)

def regis_tutor(request):
    context = {}
    return render(request, 'alumnos/regis_tutor.html', context)


def crud(request):
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def alumnos_Add(request):
    if request.method == "POST":
        genero_id = request.POST.get('genero')
        if not genero_id:
            return HttpResponse("Error: Género no seleccionado", status=400)
        
        try:
            objGenero = Genero.objects.get(id_genero=genero_id)
            Alumno.objects.create(
                nombre=request.POST.get('nombre'),
                rut=request.POST.get('rut'),
                nivel_educacion=request.POST.get('nivel_educacion'),
                direccion=request.POST.get('direccion'),
                fecha_nacimiento=request.POST.get('fecha_nacimiento'),
                correo_electronico=request.POST.get('correo_electronico'),
                telefono=request.POST.get('telefono'),
                genero=objGenero,
            )
            return redirect('crud')
        except Genero.DoesNotExist:
            return HttpResponse("Género no encontrado", status=404)
    else:
        generos = Genero.objects.all()
        return render(request, 'alumnos/alumnos_add.html', {'generos': generos})
        
def alumnos_del(request, pk):
    try:
        alumno = Alumno.objects.get(id_alumno=pk)
        alumno.delete()
        mensaje = "Bien, datos eliminados..."
    except Alumno.DoesNotExist:
        mensaje = "Error, alumno no existe..."
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos, 'mensaje': mensaje}
    return render(request, 'alumnos/alumnos_list.html', context)

def alumnos_findEdit(request, pk):
    try:
        alumno = Alumno.objects.get(id_alumno=pk)
        generos = Genero.objects.all()
        context = {'alumno': alumno, 'generos': generos}
        return render(request, 'alumnos/alumnos_edit.html', context)
    except Alumno.DoesNotExist:
        context = {'mensaje': "Error, alumno no existe..."}
        return render(request, 'alumnos/alumnos_list.html', context)

def alumnos_Update(request):
    if request.method == "POST":
        id_alumno = request.POST["id_alumno"]
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        nivel_educacion = request.POST["nivel_educacion"]
        direccion = request.POST["direccion"]
        fecha_nacimiento = request.POST["fecha_nacimiento"]
        correo_electronico = request.POST["correo_electronico"]
        telefono = request.POST["telefono"]
        genero = request.POST["genero"]

        try:
            objGenero = Genero.objects.get(id_genero=genero)
            alumno = Alumno.objects.get(id_alumno=id_alumno)
            alumno.rut = rut
            alumno.nombre = nombre
            alumno.nivel_educacion = nivel_educacion
            alumno.direccion = direccion
            alumno.fecha_nacimiento = fecha_nacimiento
            alumno.correo_electronico = correo_electronico
            alumno.telefono = telefono
            alumno.genero = objGenero
            alumno.save()
            mensaje = "Ok, datos actualizados..."
        except Genero.DoesNotExist:
            mensaje = "Error, género no existe..."
        except Alumno.DoesNotExist:
            mensaje = "Error, alumno no existe..."

        generos = Genero.objects.all()
        context = {'mensaje': mensaje, 'generos': generos, 'alumno': alumno}
        return render(request, 'alumnos/alumnos_edit.html', context)
    else:
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos}
        return render(request, 'alumnos/alumnos_list.html', context)
