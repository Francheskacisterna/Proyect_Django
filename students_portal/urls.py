from django.urls import path
from .views import menu_stud, home_stud, nosotros_stud, contactos_stud, planes_stud, pagar_stud, servicios_stud

urlpatterns = [
    
    path('menu_stud', menu_stud, name="menu_stud"),
    path('home_stud', home_stud, name="home_stud"),
    path('nosotros_stud', nosotros_stud, name='nosotros_stud'),
    path('contactos_stud', contactos_stud, name='contactos_stud'),
    path('planes_stud', planes_stud, name='planes_stud'),
    path('pagar_stud', pagar_stud, name='pagar_stud'),
    path('servicios_stud', servicios_stud, name='servicios_stud'),


]