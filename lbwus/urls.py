"""
URL configuration for lbwus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from alumnos.views import menu, CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alumnos.urls')),
    path('admin_portal/', include('admin_portal.urls')),
    path('user_profesor/', include('user_profesor.urls')),
    path('students_portal/', include('students_portal.urls')),
    path('tutor_portal/', include('tutor_portal.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('menu/', menu, name='menu'),
]
