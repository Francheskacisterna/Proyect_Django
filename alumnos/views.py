from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Alumno, Genero, Tutor
from django.http import HttpResponse

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
    if request.method == 'POST':
        try:
            nombre = request.POST['nombre']
            rut = request.POST['rut']
            nivel_educacion = request.POST['nivel_educacion']
            direccion = request.POST['direccion']
            fecha_nacimiento = request.POST['fecha_nacimiento']
            correo_electronico = request.POST['correo_electronico']
            telefono = request.POST['telefono']
            genero_id = request.POST['genero']

            genero = Genero.objects.get(id_genero=genero_id)

            Alumno.objects.create(
                nombre=nombre,
                rut=rut,
                nivel_educacion=nivel_educacion,
                direccion=direccion,
                fecha_nacimiento=fecha_nacimiento,
                correo_electronico=correo_electronico,
                telefono=telefono,
                genero=genero
            )
            return JsonResponse({"success": True, "message": "Alumno registrado exitosamente."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    generos = Genero.objects.all()
    return render(request, 'alumnos/alumnos_add.html', {'generos': generos})

def alumnos_del(request, pk):
    context={}
    try:
        alumno = Alumno.objects.get(rut=pk)

        alumno.delete()
        mensaje = "Bien, datos eliminados..."
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    except:
        mensaje="Error, rut no existe"
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)

def alumnos_findEdit(request, pk):
    alumnos = Alumno.objects.filter(rut=pk)
    generos = Genero.objects.all()

    if alumnos.count() == 1:
        alumno = alumnos.first()
        context = {'alumno': alumno, 'generos': generos}
        return render(request, 'alumnos/alumnos_edit.html', context)
    elif alumnos.count() > 1:
        context = {'alumnos': alumnos, 'generos': generos}
        return render(request, 'alumnos/multiple_alumnos.html', context)
    else:
        context = {'mensaje': "Error, rut no existe..."}
        return render(request, 'alumnos/alumnos_list.html', context)



def alumnos_Update(request):
    if request.method == "POST":
        id_alumno = request.POST.get('id_alumno')
        alumno = get_object_or_404(Alumno, id_alumno=id_alumno)

        alumno.nombre = request.POST.get("nombre")
        alumno.rut = request.POST.get("rut")
        alumno.nivel_educacion = request.POST.get("nivel_educacion")
        alumno.direccion = request.POST.get("direccion")
        alumno.fecha_nacimiento = request.POST.get("fecha_nacimiento")
        alumno.telefono = request.POST.get("telefono")
        alumno.correo_electronico = request.POST.get("correo_electronico")
        genero_id = request.POST.get("genero")
        alumno.genero = Genero.objects.get(id_genero=genero_id)

        alumno.save()

        generos = Genero.objects.all()
        context = {
            'mensaje': "Ok, datos actualizados...",
            'generos': generos,
            'alumno': alumno
        }
        return render(request, 'alumnos/alumnos_edit.html', context)
    else:
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos}
        return render(request, 'alumnos/alumnos_list.html', context)



def alumnos_reg(request):
    if request.method == 'POST':
        try:
            nombre = request.POST['nombre']
            rut = request.POST['rut']
            nivel_educacion = request.POST['nivel_educacion']
            direccion = request.POST['direccion']
            fecha_nacimiento = request.POST['fecha_nacimiento']
            correo_electronico = request.POST['correo_electronico']
            telefono = request.POST['telefono']
            genero_id = request.POST['genero']

            genero = Genero.objects.get(id_genero=genero_id)

            Alumno.objects.create(
                nombre=nombre,
                rut=rut,
                nivel_educacion=nivel_educacion,
                direccion=direccion,
                fecha_nacimiento=fecha_nacimiento,
                correo_electronico=correo_electronico,
                telefono=telefono,
                genero=genero
            )
            return JsonResponse({"success": True, "message": "Alumno registrado exitosamente."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    generos = Genero.objects.all()
    return render(request, 'alumnos/regis_alum.html', {'generos': generos})


def crud_profesor(request):
    profesores = Profesor.objects.all()
    context = {'profesores': profesores}
    return render(request, 'profesor/profesor_list.html', context)

def profesor_Add(request):
    if request.method == 'POST':
        try:
            nombre = request.POST['nombre']
            rut = request.POST['rut']
            especialidad = request.POST['especialidad']
            direccion = request.POST['direccion']
            fecha_nacimiento = request.POST['fecha_nacimiento']
            correo_electronico = request.POST['correo_electronico']
            telefono = request.POST['telefono']
            genero_id = request.POST['genero']

            genero = Genero.objects.get(id_genero=genero_id)

            Profesor.objects.create(
                nombre=nombre,
                rut=rut,
                especialidad=especialidad,
                direccion=direccion,
                fecha_nacimiento=fecha_nacimiento,
                correo_electronico=correo_electronico,
                telefono=telefono,
                genero=genero
            )
            return JsonResponse({"success": True, "message": "Profesor registrado exitosamente."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    generos = Genero.objects.all()
    return render(request, 'profesor/profesor_add.html', {'generos': generos})

def profesor_del(request, pk):
    context = {}
    try:
        profesor = Profesor.objects.get(rut=pk)
        profesor.delete()
        mensaje = "Bien, datos eliminados..."
        profesores = Profesor.objects.all()
        context = {'profesores': profesores, 'mensaje': mensaje}
        return render(request, 'profesor/profesor_list.html', context)
    except:
        mensaje = "Error, rut no existe"
        profesores = Profesor.objects.all()
        context = {'profesores': profesores, 'mensaje': mensaje}
        return render(request, 'profesor/profesor_list.html', context)

def profesor_find_edit(request, pk):
    profesores = Profesor.objects.filter(rut=pk)
    generos = Genero.objects.all()

    if profesores.count() == 1:
        profesor = profesores.first()
        context = {'profesor': profesor, 'generos': generos}
        return render(request, 'profesor/profesor_edit.html', context)
    elif profesores.count() > 1:
        context = {'profesores': profesores, 'generos': generos}
        return render(request, 'profesor/multiple_profesores.html', context)
    else:
        context = {'mensaje': "Error, rut no existe..."}
        return render(request, 'profesor/profesor_list.html', context)

def alumnosUpdate(request):
    if request.method == "POST":
        id_alumno = request.POST.get('id_alumno')
        alumno = get_object_or_404(Alumno, id_alumno=id_alumno)

        alumno.nombre = request.POST.get("nombre")
        alumno.rut = request.POST.get("rut")
        alumno.nivel_educacion = request.POST.get("nivel_educacion")
        alumno.direccion = request.POST.get("direccion")
        alumno.fecha_nacimiento = request.POST.get("fecha_nacimiento")
        alumno.telefono = request.POST.get("telefono")
        alumno.correo_electronico = request.POST.get("correo_electronico")
        genero_id = request.POST.get("genero")
        alumno.genero = Genero.objects.get(id_genero=genero_id)

        alumno.save()

        generos = Genero.objects.all()
        context = {
            'mensaje': "Ok, datos actualizados...",
            'generos': generos,
            'alumno': alumno
        }
        return render(request, 'alumnos/alumnos_edit.html', context)
    else:
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos}
        return render(request, 'alumnos/alumnos_list.html', context)
