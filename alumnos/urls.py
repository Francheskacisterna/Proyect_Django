#from django.conf.urls import url
from django.urls import path
from .views import home, contactos, nosotros, planes, servicios, simulador, opcion_user, regis_prof, regis_alum, regis_tutor, crud, alumnos_Add, alumnos_del, alumnos_findEdit, alumnos_Update, alumnos_reg, crud_profesor, profesor_Add, profesor_del, profesor_findEdit, profesorUpdate, lista_combinada, dashboard

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
    path('alumnos/alumnos_del/<str:pk>/', alumnos_del, name='alumnos_del'),
    path('alumnos/alumnos_findEdit/<str:pk>/', alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnos/alumnos_Update', alumnos_Update, name='alumnos_Update'),
    path('alumnos/alumnos_reg', alumnos_reg, name='alumnos_reg'),

    path('profesor/crud', crud_profesor, name='crud_profesores'),
    path('profesor/add/', profesor_Add, name='profesor_Add'),
    path('profesor/del/<str:pk>/', profesor_del, name='profesor_del'),
    path('profesor/edit/<str:pk>', profesor_findEdit, name='profesor_findEdit'),
    path('profesor/update/', profesorUpdate, name='profesorUpdate'),

    path('listacli/', lista_combinada, name='lista_combinada'),
    path('dashboard/', dashboard, name='dashboard'),
]
