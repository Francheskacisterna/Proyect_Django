from django.contrib import admin
from django.contrib import admin
from .models import Genero, Tutor, Alumno, Profesor, Clase, Inscripcion

# Register your models here.

admin.site.register(Genero)
admin.site.register(Tutor)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Clase)
admin.site.register(Inscripcion)