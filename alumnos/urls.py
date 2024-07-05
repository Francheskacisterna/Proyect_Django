#from django.conf.urls import url
from django.urls import path
from .views import home, contactos, nosotros, planes, servicios, simulador, opcion_user, regis_prof, regis_alum, regis_tutor, crud, alumnos_Add, alumnos_del, alumnos_findEdit, alumnos_Update

urlpatterns = [
    path('', home, name='home'),
    path('alumnos/contactos', contactos, name='contactos'),
    path('alumnos/nosotros', nosotros, name='nosotros'),
    path('alumnos/planes', planes, name='planes'),
    path('alumnos/servicios', servicios, name='servicios'),
    path('alumnos/simulador', simulador, name='simulador'),
    path('alumnos/select', opcion_user, name='opcion_user'),
    path('alumnos/registro_profesor', regis_prof, name='regis_prof'),
    path('alumnos/registro_tutor', regis_tutor, name='regis_tutor'),
    path('alumnos/registro_alumno', regis_alum, name='regis_alum'),
    path('alumnos/crud/', crud, name='crud'),
    path('alumnos/alumnos_Add', alumnos_Add, name='alumnos_Add'),
    path('alumnos/alumnos_del', alumnos_del, name='alumnos_del'),
    path('alumnos/alumnos_finEdit/str:pk', alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnos/alumnos_Update', alumnos_Update, name='alumnos_Update')
]
