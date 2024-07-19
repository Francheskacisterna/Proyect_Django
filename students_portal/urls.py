from django.urls import path
from .views import menu_stud, home_stud, nosotros_stud, contactos_stud, dashboard

urlpatterns = [
    
    path('menu_stud', menu_stud, name="menu_stud"),
    path('home_stud', home_stud, name="home_stud"),
    path('nosotros_stud', nosotros_stud, name='nosotros_stud'),
    path('contactos_stud', contactos_stud, name='contactos_stud'),
    path('dashboard/', dashboard, name='dashboard'),

]