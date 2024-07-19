from django.urls import path
from .views import menu, reporte_alumnos, home_adm, planes_adm, nosotros_adm, contactos_adm, dashboard

urlpatterns = [
    path('menu', menu, name='menu'),
    path('reporte_alumnos', reporte_alumnos, name='reporte_alumnos'),
    path('home_adm', home_adm, name='home_adm'),
    path('planes_adm', planes_adm, name='planes_adm'),
    path('nosotros_adm', nosotros_adm, name='nosotros_adm'),
    path('contactos_adm', contactos_adm, name='contactos_adm'),
    path('dashboard/', dashboard, name='dashboard'),
]