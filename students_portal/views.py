from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def menu_stud(request):
    context = {}
    return render(request, 'students/home_stud.html', context)

@login_required
def home_stud(request):
    context = {}
    return render(request, 'students_portal/home_stud.html', context)

@login_required
def nosotros_stud(request):
    context = {}
    return render(request, 'students_portal/nosotros_stud.html', context)

@login_required
def contactos_stud(request):
    context = {}
    return render(request, 'students_portal/contactos_stud.html', context)

@login_required
def pagar_stud(request):
    context = {}
    return render(request, 'students_portal/pagar_stud.html', context)

@login_required
def planes_stud(request):
    context = {}
    return render(request, 'students_portal/planes_stud.html', context)

@login_required
def servicios_stud(request):
    context = {}
    return render(request, 'students_portal/servicios_stud.html', context)



