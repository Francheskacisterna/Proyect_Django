from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Genero, Tutor, Alumno, Profesor, Clase, Inscripcion, CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type',)}),
    )


admin.site.register(Genero)
admin.site.register(Tutor)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Clase)
admin.site.register(Inscripcion)

