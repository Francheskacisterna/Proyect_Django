from django.urls import path
from .views import menu_tutor, home_tutor, nosotros_tutor, contactos_tutor

urlpatterns = [
    
    path('menu_tutor/', menu_tutor, name='menu_tutor'),
    path('home_tutor', home_tutor, name='home_tutor'),
    path('nosotros_tutor', nosotros_tutor, name='nosotros_tutor'),
    path('contacto_tutor', contactos_tutor, name='contactos_tutor'),
]