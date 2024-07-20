from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def menu_prof(request):
    return render(request, 'tutor_portal/menu_tutor.html')
@login_required
def home_prof(request):
    context = {}
    return render(request, 'user_prof/home_prof.html', context)
@login_required
def planes_prof(request):
    context = {}
    return render(request, 'user_prof/planes_prof.html', context)
@login_required
def nosotros_prof(request):
    context = {}
    return render(request, 'user_prof/nosotros_prof.html', context)
@login_required
def contactos_prof(request):
    context = {}
    return render(request, 'user_prof/contactos_prof.html', context)

