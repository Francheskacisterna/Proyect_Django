from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Alumno, Genero, Tutor, Profesor, CustomUser, Clase, Especialidad, Inscripcion
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        user = self.request.user
        print(f'Logged in user: {user.username}, user_type: {user.user_type}')
        if user.user_type == 1:  # Admin
            return reverse_lazy('menu')
        elif user.user_type == 2:  # Profesor
            return reverse_lazy('profesor_menu')
        elif user.user_type == 3:  # Alumno
            return reverse_lazy('alumno_menu')
        elif user.user_type == 4:  # Tutor
            return reverse_lazy('tutor_menu')
        else:
            return reverse_lazy('home')

@login_required
def menu(request):
    print(f'User: {request.user.username}, User Type: {request.user.user_type}')
    if request.user.user_type == 1:  # Admin
        return render(request, 'admin_portal/menu.html')
    elif request.user.user_type == 2:  # Profesor
        return render(request, 'user_profesor/menu_prof.html')
    elif request.user.user_type == 3:  # Alumno
        return render(request, 'students_portal/menu_stud.html')
    elif request.user.user_type == 4:  # Tutor
        return render(request, 'tutor_portal/menu_tutor.html')
    else:
        return redirect('home')

def cerrar(request):
    return render(request, 'alumnos/home.html')

def home(request):
    return render(request, 'alumnos/home.html')

def cerrar(request):
    return render(request, 'alumnos/home.html')

def home(request):
    return render(request, 'alumnos/home.html')

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

#REGISTRO DE ALUMNOS
def regis_alum(request):
    generos = Genero.objects.all()
    data = {
        'generos': generos
    }
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
            username = request.POST['username']
            password = request.POST['password']
            
            # Verificar si el username ya existe
            if CustomUser.objects.filter(username=username).exists():
                return JsonResponse({"success": False, "message": "El nombre de usuario ya existe. Por favor elija otro nombre de usuario."})

            genero = Genero.objects.get(id_genero=genero_id)

            # Crear el usuario
            c = CustomUser.objects.create_user(username=username, password=password, user_type=CustomUser.ALUMNO, email=correo_electronico)

            # Asignar el grupo "Alumno" al usuario
            group = Group.objects.get(name='Alumno')
            c.groups.add(group)

            # Crear el alumno
            Alumno.objects.create(
                nombre=nombre,
                username=c.username,
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

    return render(request, 'alumnos/regis_alum.html', data)

#REGISTRO DE PROFESORES

def regis_prof(request):
    generos = Genero.objects.all()
    especialidades = Especialidad.objects.all()
    data = {
        'generos': generos,
        'especialidades': especialidades
    }
    if request.method == 'POST':
        try:
            nombre = request.POST['nombre']
            rut = request.POST['rut']
            especialidad_id = request.POST['especialidad']
            direccion = request.POST['direccion']
            fecha_nacimiento = request.POST['fecha_nacimiento']
            correo_electronico = request.POST['correo_electronico']
            telefono = request.POST['telefono']
            genero_id = request.POST['genero']
            usuario = request.POST['username']
            paswd = request.POST['password']
            genero = Genero.objects.get(id_genero=genero_id)
            especialidad = Especialidad.objects.get(id_especialidad=especialidad_id)

            # Crear el usuario
            c = CustomUser.objects.create_user(
                username=usuario,
                password=paswd,
                user_type=CustomUser.PROFESOR,
                email=correo_electronico
            )
            c.first_name = nombre
            c.last_name = nombre
            c.save()

            # Asignar el grupo "Profesor" al usuario
            group, created = Group.objects.get_or_create(name='Profesor')
            c.groups.add(group)

            # Crear el profesor
            Profesor.objects.create(
                nombre=nombre,
                username=usuario,
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
    return render(request, 'alumnos/regis_prof.html', data)


#REGISTRO DE TUTOR
def regis_tutor(request):
    generos = Genero.objects.all()
    data = {
        'generos': generos
    }
    if request.method == 'POST':
        try:
            nombre = request.POST['nombre']
            rut = request.POST['rut']
            nivel_educacion = request.POST.get('nivel_educacion', '')  # Opcional para tutor
            direccion = request.POST['direccion']
            fecha_nacimiento = request.POST['fecha_nacimiento']
            correo_electronico = request.POST['correo_electronico']
            telefono = request.POST['telefono']
            genero_id = request.POST['genero']
            usuario = request.POST['username']
            paswd = request.POST['password']
            genero = Genero.objects.get(id_genero=genero_id)
            c = CustomUser()
            c.first_name = nombre
            c.last_name = nombre
            c.email = correo_electronico
            c.username = usuario
            c.user_type = CustomUser.TUTOR
            c.set_password(paswd)
            c.save()
            group, created = Group.objects.get_or_create(name='Tutor')
            c.groups.add(group)
            Tutor.objects.create(
                nombre=c.first_name,
                username=c.username,
                rut=rut,
                direccion=direccion,
                fecha_nacimiento=fecha_nacimiento,
                correo_electronico=c.email,
                telefono=telefono,
                genero=genero
            )
            return JsonResponse({"success": True, "message": "Registrado Correctamente"})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    return render(request, 'alumnos/regis_tutor.html', data) 

#Crud Alumnos

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
            username = request.POST['username']

            # Verificar si el username ya existe
            if Alumno.objects.filter(username=username).exists():
                return JsonResponse({"success": False, "message": "El nombre de usuario ya existe. Por favor elija otro nombre de usuario."})

            genero = Genero.objects.get(id_genero=genero_id)

            Alumno.objects.create(
                nombre=nombre,
                rut=rut,
                nivel_educacion=nivel_educacion,
                direccion=direccion,
                fecha_nacimiento=fecha_nacimiento,
                correo_electronico=correo_electronico,
                telefono=telefono,
                genero=genero,
                username=username,
                password='default_password'  # Puedes actualizar esto para establecer una contraseña adecuada
            )

            # Agregar al grupo Alumno
            user = Alumno.objects.get(username=username)
            group = Group.objects.get(name='Alumno')
            user.groups.add(group)

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


#CRUD PROFESOR

def crud_profesor(request):
    profesores = Profesor.objects.all()
    context = {'profesores': profesores}
    return render(request, 'alumnos/profesor_list.html', context)

def profesor_Add(request):
    if request.method == 'POST':
        try:
            nombre = request.POST['nombre']
            rut = request.POST['rut']
            especialidad_id = request.POST['especialidad']
            direccion = request.POST['direccion']
            fecha_nacimiento = request.POST['fecha_nacimiento']
            correo_electronico = request.POST['correo_electronico']
            telefono = request.POST['telefono']
            genero_id = request.POST['genero']
            username = request.POST['username']
            password = request.POST['password']

            # Verificar si el username ya existe
            if CustomUser.objects.filter(username=username).exists():
                return JsonResponse({"success": False, "message": "El nombre de usuario ya existe. Por favor elija otro nombre de usuario."})

            genero = Genero.objects.get(id_genero=genero_id)
            especialidad = Especialidad.objects.get(id_especialidad=especialidad_id)

            # Crear el usuario
            c = CustomUser.objects.create_user(username=username, password=password, user_type='profesor', email=correo_electronico)

            # Asignar el grupo "Profesor" al usuario
            group, created = Group.objects.get_or_create(name='Profesor')
            c.groups.add(group)

            # Crear el profesor
            Profesor.objects.create(
                nombre=nombre,
                rut=rut,
                especialidad=especialidad,
                direccion=direccion,
                fecha_nacimiento=fecha_nacimiento,
                correo_electronico=correo_electronico,
                telefono=telefono,
                genero=genero,
                username=c.username
            )

            return JsonResponse({"success": True, "message": "Profesor registrado exitosamente."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    generos = Genero.objects.all()
    especialidades = Especialidad.objects.all()
    return render(request, 'alumnos/profesor_add.html', {'generos': generos, 'especialidades': especialidades})
    

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
    especialidades = Especialidad.objects.all()

    if profesores.count() == 1:
        profesor = profesores.first()
        context = {'profesor': profesor, 'generos': generos, 'especialidades': especialidades}
        return render(request, 'alumnos/profesor_edit.html', context)
    elif profesores.count() > 1:
        context = {'profesores': profesores, 'generos': generos, 'especialidades': especialidades}
        return render(request, 'alumnos/multiple_profesores.html', context)
    else:
        context = {'mensaje': "Error, rut no existe..."}
        return render(request, 'alumnos/profesor_list.html', context)

def profesorUpdate(request):
    if request.method == "POST":
        id_profesor = request.POST.get('id_profesor')
        profesor = get_object_or_404(Profesor, pk=id_profesor)

        profesor.nombre = request.POST.get("nombre")
        profesor.rut = request.POST.get("rut")
        profesor.direccion = request.POST.get("direccion")
        profesor.fecha_nacimiento = request.POST.get("fecha_nacimiento")
        profesor.telefono = request.POST.get("telefono")
        profesor.correo_electronico = request.POST.get("correo_electronico")
        genero_id = request.POST.get("genero")
        especialidad_id = request.POST.get("especialidad")
        profesor.genero = Genero.objects.get(id_genero=genero_id)
        profesor.especialidad = Especialidad.objects.get(id_especialidad=especialidad_id)

        profesor.save()

        generos = Genero.objects.all()
        especialidades = Especialidad.objects.all()
        context = {
            'mensaje': "Ok, datos actualizados...",
            'generos': generos,
            'especialidades': especialidades,
            'profesor': profesor
        }
        return render(request, 'alumnos/profesor_edit.html', context)
    else:
        profesores = Profesor.objects.all()
        context = {'profesores': profesores}
        return render(request, 'alumnos/profesor_list.html', context)



def lista_combinada(request):
    alumnos = Alumno.objects.all()
    profesores = Profesor.objects.all()
    context = {
        'alumnos': alumnos,
        'profesores': profesores
    }
    return render(request, 'alumnos/lista_combinada.html', context)

# Crud Tutor

def crud_tutor(request):
    tutores = Tutor.objects.all()
    context = {'tutores': tutores}
    return render(request, 'alumnos/tutor_list.html', context)

def tutor_Add(request):
    if request.method == 'POST':
        try:
            nombre = request.POST['nombre']
            rut = request.POST['rut']
            direccion = request.POST['direccion']
            fecha_nacimiento = request.POST['fecha_nacimiento']
            correo_electronico = request.POST['correo_electronico']
            telefono = request.POST['telefono']
            genero_id = request.POST['genero_id']
            username = request.POST['username']
            password = request.POST['password']

            genero = Genero.objects.get(id_genero=genero_id)

            Tutor.objects.create(
                nombre=nombre,
                rut=rut,
                direccion=direccion,
                fecha_nacimiento=fecha_nacimiento,
                correo_electronico=correo_electronico,
                telefono=telefono,
                genero=genero,
                username=username,
                password=password
            )
            return JsonResponse({"success": True, "message": "Tutor registrado exitosamente."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    generos = Genero.objects.all()
    return render(request, 'alumnos/tutor_add.html', {'generos': generos})


def tutor_del(request, pk):
    context = {}
    try:
        tutor = Tutor.objects.get(id_tutor=pk)
        tutor.delete()
        mensaje = "Bien, datos eliminados..."
        tutores = Tutor.objects.all()
        context = {'tutores': tutores, 'mensaje': mensaje}
        return render(request, 'tutores/tutor_list.html', context)
    except Tutor.DoesNotExist:
        mensaje = "Error, tutor no existe"
        tutores = Tutor.objects.all()
        context = {'tutores': tutores, 'mensaje': mensaje}
        return render(request, 'alumnos/tutor_list.html', context)

def tutor_findEdit(request, pk):
    tutores = Tutor.objects.filter(id_tutor=pk)
    generos = Genero.objects.all()

    if tutores.count() == 1:
        tutor = tutores.first()
        context = {'tutor': tutor, 'generos': generos}
        return render(request, 'alumnos/tutor_edit.html', context)
    elif tutores.count() > 1:
        context = {'tutores': tutores, 'generos': generos}
        return render(request, 'alumnos/multiple_tutores.html', context)
    else:
        context = {'mensaje': "Error, el tutor no existe..."}
        return render(request, 'alumnos/tutor_list.html', context)

def tutor_Update(request):
    if request.method == "POST":
        id_tutor = request.POST.get('id_tutor')
        tutor = get_object_or_404(Tutor, id_tutor=id_tutor)

        tutor.nombre = request.POST.get("nombre")
        tutor.rut = request.POST.get("rut")
        tutor.direccion = request.POST.get("direccion")
        tutor.fecha_nacimiento = request.POST.get("fecha_nacimiento")
        tutor.correo_electronico = request.POST.get("correo_electronico")
        tutor.telefono = request.POST.get("telefono")
        genero_id = request.POST.get("genero_id")
        tutor.genero = Genero.objects.get(id_genero=genero_id) 
        tutor.username = request.POST.get("username")
        tutor.password = request.POST.get("password")

        tutor.save()

        generos = Genero.objects.all()
        context = {
            'mensaje': "Ok, datos actualizados...",
            'generos': generos,
            'tutor': tutor
        }
        return render(request, 'alumnos/tutor_edit.html', context)  
    else:
        tutores = Tutor.objects.all()
        generos = Genero.objects.all()  
        context = {'tutores': tutores, 'generos': generos}
        return render(request, 'alumnos/tutor_list.html', context)  



# Crud Clase

def crud_clases(request):
    clases = Clase.objects.all()
    context = {'clases': clases}
    return render(request, 'alumnos/clases_list.html', context)

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
    return render(request, 'alumnos/clases_add.html', {'profesores': profesores})

def clases_del(request, pk):
    context = {}
    try:
        clase = Clase.objects.get(id_clase=pk)
        clase.delete()
        mensaje = "Bien, datos eliminados..."
        clases = Clase.objects.all()
        context = {'clases': clases, 'mensaje': mensaje}
        return render(request, 'alumnos/clases_list.html', context)
    except Clase.DoesNotExist:
        mensaje = "Error, clase no existe"
        clases = Clase.objects.all()
        context = {'clases': clases, 'mensaje': mensaje}
        return render(request, 'alumnos/clases_list.html', context)

def clases_findEdit(request, pk):
    clases = Clase.objects.filter(id_clase=pk)
    profesores = Profesor.objects.all()

    if clases.count() == 1:
        clase = clases.first()
        context = {'clase': clase, 'profesores': profesores}
        return render(request, 'alumnos/clases_edit.html', context)
    elif clases.count() > 1:
        context = {'clases': clases, 'profesores': profesores}
        return render(request, 'alumnos/multiple_clases.html', context)
    else:
        context = {'mensaje': "Error, la clase no existe..."}
        return render(request, 'alumnos/clases_list.html', context)

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
        return render(request, 'alumnos/clases_edit.html', context)
    else:
        clases = Clase.objects.all()
        context = {'clases': clases}
        return render(request, 'alumnos/clases_list.html', context)


# Crud inscripción

def crud_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    context = {'inscripciones': inscripciones}
    return render(request, 'alumnos/inscripcion_list.html', context)

def inscripcion_Add(request):
    if request.method == 'POST':
        try:
            id_alumno = request.POST.get('id_alumno')
            id_clase = request.POST.get('id_clase')

            alumno = Alumno.objects.get(id_alumno=id_alumno)
            clase = Clase.objects.get(id_clase=id_clase)

            Inscripcion.objects.create(id_alumno=alumno, id_clase=clase)
            return JsonResponse({"success": True, "message": "Inscripción registrada exitosamente."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    else:
        alumnos = Alumno.objects.all()
        clases = Clase.objects.all()
        return render(request, 'alumnos/inscripcion_add.html', {'alumnos': alumnos, 'clases': clases})

def inscripcion_del(request, pk):
    try:
        inscripcion = Inscripcion.objects.get(id=pk)
        inscripcion.delete()
        mensaje = "Bien, datos eliminados..."
    except Inscripcion.DoesNotExist:
        mensaje = "Error, inscripción no existe"
    
    inscripciones = Inscripcion.objects.all()
    context = {'inscripciones': inscripciones, 'mensaje': mensaje}
    return render(request, 'alumnos/inscripcion_list.html', context)

def inscripcion_findEdit(request, pk):
    inscripcion = Inscripcion.objects.filter(id=pk).first()
    if inscripcion:
        alumnos = Alumno.objects.all()
        clases = Clase.objects.all()
        context = {'inscripcion': inscripcion, 'alumnos': alumnos, 'clases': clases}
        return render(request, 'alumnos/inscripcion_edit.html', context)
    else:
        mensaje = "Error, la inscripción no existe..."
        return render(request, 'alumnos/inscripcion_list.html', {'mensaje': mensaje})


def inscripcion_update(request, pk):
    if request.method == "POST":
        inscripcion = get_object_or_404(Inscripcion, id=pk)
        inscripcion.id_alumno = Alumno.objects.get(id=request.POST.get("id_alumno"))
        inscripcion.id_clase = Clase.objects.get(id=request.POST.get("id_clase"))
        inscripcion.save()

        mensaje = "Ok, datos actualizados..."
        return render(request, 'alumnos/inscripcion_edit.html', {'mensaje': mensaje, 'inscripcion': inscripcion})
    else:
        inscripciones = Inscripcion.objects.all()
        return render(request, 'alumnos/inscripcion_list.html', {'inscripciones': inscripciones})


def lista_combinada(request):
    alumnos = Alumno.objects.all()
    profesores = Profesor.objects.all()
    context = {
        'alumnos': alumnos,
        'profesores': profesores

    }
    return render(request, 'alumnos/lista_combinada.html', context)



    


