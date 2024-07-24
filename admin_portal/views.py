
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def menu(request):
    context = {}
    return render(request, 'admin_portal/menu.html')

@login_required
def home_adm(request):
    context = {}
    return render(request, 'admin_portal/home_adm.html')

@login_required
def planes_adm(request):
    context = {}
    return render(request, 'admin_portal/planes_adm.html')

@login_required
def nosotros_adm(request):
    context = {}
    return render(request, 'admin_portal/nosotros_adm.html')

@login_required
def contactos_adm(request):
    context = {}
    return render(request, 'admin_portal/contactos_adm.html')


