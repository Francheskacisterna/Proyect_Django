from django.urls import path
from .views import menu, reporte_alumnos, home
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('menu', menu, name='menu'),
    path('reporte_alumnos', reporte_alumnos, name='reporte_alumnos'),
    path('home', home, name='home'),
        path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]