from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def menu_tutor(request):
    context = {}
    return render(request, 'tutor_portal/menu_stud.html', context)

@login_required
def home_tutor(request):
    context = {}
    return render(request, 'tutor_portal/home_tutor.html', context)

@login_required
def nosotros_tutor(request):
    context = {}
    return render(request, 'tutor_portal/nosotros_tutor.html', context)

@login_required
def contactos_tutor(request):
    context = {}
    return render(request, 'tutor_portal/contactos_tutor.html', context)

@login_required
def planes_tutor(request):
    context = {}
    return render(request, 'tutor_portal/contactos_tutor.html', context)

