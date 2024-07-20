from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import (
    CustomLoginView, home, contactos, nosotros, planes, servicios, simulador, opcion_user,
    regis_prof, regis_alum, regis_tutor, crud, alumnos_Add, alumnos_del, alumnos_findEdit, alumnos_Update, crud_profesor, profesor_Add, profesor_del, profesor_findEdit, profesorUpdate, lista_combinada,
    crud_clases, clases_Add, clases_del, clases_findEdit, clases_Update, crud_inscripciones, inscripcion_Add,
    inscripcion_del, inscripcion_findEdit, inscripcion_update, crud_tutor, tutor_Add, tutor_del, tutor_findEdit, tutor_Update
)

urlpatterns = [
    path('home/', home, name='home'),
    path('alumnos/contactos/', contactos, name='contactos'),
    path('alumnos/nosotros/', nosotros, name='nosotros'),
    path('alumnos/planes/', planes, name='planes'),
    path('alumnos/servicios/', servicios, name='servicios'),
    path('alumnos/simulador/', simulador, name='simulador'),
    path('alumnos/select/', opcion_user, name='opcion_user'),
    path('alumnos/registro_profesor/', regis_prof, name='regis_prof'),
    path('alumnos/registro_tutor/', regis_tutor, name='regis_tutor'),
    path('alumnos/registro_alumno/', regis_alum, name='regis_alum'),

    path('alumnos/crud/', crud, name='crud'),
    path('alumnos/alumnos_Add/', alumnos_Add, name='alumnos_Add'),
    path('alumnos/alumnos_del/<str:pk>/', alumnos_del, name='alumnos_del'),
    path('alumnos/alumnos_findEdit/<str:pk>/', alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnos/alumnos_Update/', alumnos_Update, name='alumnos_Update'),

    path('profesor/crud/', crud_profesor, name='crud_profesor'),
    path('profesor/add/', profesor_Add, name='profesor_Add'),
    path('profesor/del/<str:pk>/', profesor_del, name='profesor_del'),
    path('profesor/edit/<str:pk>/', profesor_findEdit, name='profesor_findEdit'),
    path('profesor/update/', profesorUpdate, name='profesorUpdate'),

    path('clases/crud/', crud_clases, name='crud_clases'),
    path('clases/add/', clases_Add, name='clases_Add'),
    path('clases/del/<str:pk>/', clases_del, name='clases_del'),
    path('clases/findEdit/<str:pk>/', clases_findEdit, name='clases_findEdit'),
    path('clases/update/', clases_Update, name='clases_Update'),

    path('inscripcion/crud/', crud_inscripciones, name='crud_inscripciones'),
    path('inscripcion/add/', inscripcion_Add, name='inscripcion_Add'),
    path('inscripcion/del/<str:pk>/', inscripcion_del, name='inscripcion_del'),
    path('inscripcion/findEdit/<str:pk>/', inscripcion_findEdit, name='inscripcion_findEdit'),
    path('inscripcion/update/', inscripcion_update, name='inscripcion_update'),

    path('tutor/crud/', crud_tutor, name='crud_tutor'),
    path('tutor/add/', tutor_Add, name='tutor_Add'),
    path('tutor/del/<str:pk>/', tutor_del, name='tutor_del'),
    path('tutor/findEdit/<str:pk>/', tutor_findEdit, name='tutor_findEdit'),
    path('tutor/update/', tutor_Update, name='tutor_Update'),

    path('listacli/', lista_combinada, name='lista_combinada'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('admin/menu/', TemplateView.as_view(template_name='admin_portal/menu.html'), name='menu'),
    path('profesor/menu/', TemplateView.as_view(template_name='user_profesor/menu_prof.html'), name='profesor_menu'),
    path('alumno/menu/', TemplateView.as_view(template_name='students_portal/menu_stud.html'), name='alumno_menu'),
    path('tutor/menu/', TemplateView.as_view(template_name='tutor_portal/menu_tutor.html'), name='tutor_menu'),
    

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
