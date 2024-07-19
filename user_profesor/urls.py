from django.urls import path
from .views import menu_prof, contactos_prof, home_prof, nosotros_prof, contactos_prof, planes_prof

urlpatterns = [
    path('menu_prof', menu_prof, name="menu_prof"),
    path('home_prof', home_prof, name="home_prof"),
    path('nosotros_prof', nosotros_prof, name='nosotros_prof'),
    path('contactos_prof', contactos_prof, name='contactos_prof'),
    path('planes_prof', planes_prof, name='planes_prof'),
    
]

