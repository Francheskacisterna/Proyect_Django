from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Alumno, Genero, Tutor, Profesor, Clase
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
    return render(request, 'alumnos/profesor_list.html', context)

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
    return render(request, 'alumnos/profesor_add.html', {'generos': generos})

def profesor_del(request, pk):
    context = {}
    try:
        profesor = Profesor.objects.get(rut=pk)
        profesor.delete()
        mensaje = "Bien, datos eliminados..."
        profesores = Profesor.objects.all()
        context = {'profesores': profesores, 'mensaje': mensaje}
        return render(request, 'alumnos/profesor_list.html', context)
    except:
        mensaje = "Error, rut no existe"
        profesores = Profesor.objects.all()
        context = {'profesores': profesores, 'mensaje': mensaje}
        return render(request, 'alumnos/profesor_list.html', context)

def profesor_findEdit(request, pk):
    profesores = Profesor.objects.filter(rut=pk)
    generos = Genero.objects.all()

    if profesores.count() == 1:
        profesor = profesores.first()
        context = {'profesor': profesor, 'generos': generos}
        return render(request, 'alumnos/profesor_edit.html', context)
    elif profesores.count() > 1:
        context = {'profesores': profesores, 'generos': generos}
        return render(request, 'alumnos/multiple_profesores.html', context)
    else:
        context = {'mensaje': "Error, rut no existe..."}
        return render(request, 'alumno/profesor_list.html', context)


def profesorUpdate(request):
    if request.method == "POST":
        id_profesor = request.POST.get('id_profesor')
        profesor = get_object_or_404(Profesor, pk=id_profesor)

        profesor.nombre = request.POST.get("nombre")
        profesor.rut = request.POST.get("rut")
        profesor.especialidad = request.POST.get("especialidad")
        profesor.direccion = request.POST.get("direccion")
        profesor.fecha_nacimiento = request.POST.get("fecha_nacimiento")
        profesor.telefono = request.POST.get("telefono")
        profesor.correo_electronico = request.POST.get("correo_electronico")
        genero_id = request.POST.get("genero")
        profesor.genero = Genero.objects.get(id=genero_id)

        profesor.save()

        generos = Genero.objects.all()
        context = {
            'mensaje': "Ok, datos actualizados...",
            'generos': generos,
            'profesor': profesor
        }
        return render(request, 'alumnos/profesor_edit.html', context)
    else:
        profesores = Profesor.objects.all()
        context = {'profesores': profesores}
        return render(request, 'alumnos/profesor_list.html', context)

def crud_clases(request):
    clases = Clase.objects.all()
    context = {'clases': clases}
    return render(request, 'clases/clases_list.html', context)

def clases_Add(request):
    if request.method == 'POST':
        try:
            nombre_curso = request.POST['nombre_curso']
            modalidad = request.POST['modalidad']
            horario = request.POST['horario']
            id_profesor = request.POST['id_profesor']

            profesor = Profesor.objects.get(id_profesor=id_profesor)

            Clase.objects.create(
                nombre_curso=nombre_curso,
                modalidad=modalidad,
                horario=horario,
                id_profesor=profesor
            )
            return JsonResponse({"success": True, "message": "Clase registrada exitosamente."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    profesores = Profesor.objects.all()
    return render(request, 'clases/clases_add.html', {'profesores': profesores})

def clases_del(request, pk):
    context = {}
    try:
        clase = Clase.objects.get(id_clase=pk)
        clase.delete()
        mensaje = "Bien, datos eliminados..."
        clases = Clase.objects.all()
        context = {'clases': clases, 'mensaje': mensaje}
        return render(request, 'clases/clases_list.html', context)
    except Clase.DoesNotExist:
        mensaje = "Error, clase no existe"
        clases = Clase.objects.all()
        context = {'clases': clases, 'mensaje': mensaje}
        return render(request, 'clases/clases_list.html', context)

def clases_findEdit(request, pk):
    clases = Clase.objects.filter(id_clase=pk)
    profesores = Profesor.objects.all()

    if clases.count() == 1:
        clase = clases.first()
        context = {'clase': clase, 'profesores': profesores}
        return render(request, 'clases/clases_edit.html', context)
    elif clases.count() > 1:
        context = {'clases': clases, 'profesores': profesores}
        return render(request, 'clases/multiple_clases.html', context)
    else:
        context = {'mensaje': "Error, la clase no existe..."}
        return render(request, 'clases/clases_list.html', context)

def clases_Update(request):
    if request.method == "POST":
        id_clase = request.POST.get('id_clase')
        clase = get_object_or_404(Clase, id_clase=id_clase)

        clase.nombre_curso = request.POST.get("nombre_curso")
        clase.modalidad = request.POST.get("modalidad")
        clase.horario = request.POST.get("horario")
        id_profesor = request.POST.get("id_profesor")
        clase.id_profesor = Profesor.objects.get(id_profesor=id_profesor)

        clase.save()

        profesores = Profesor.objects.all()
        context = {
            'mensaje': "Ok, datos actualizados...",
            'profesores': profesores,
            'clase': clase
        }
        return render(request, 'clases/clases_edit.html', context)
    else:
        clases = Clase.objects.all()
        context = {'clases': clases}
        return render(request, 'clases/clases_list.html', context)

def lista_combinada(request):
    alumnos = Alumno.objects.all()
    profesores = Profesor.objects.all()
    context = {
        'alumnos': alumnos,
        'profesores': profesores

    }
    return render(request, 'alumnos/lista_combinada.html', context)

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