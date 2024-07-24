from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group, Permission


# Definir constantes para los tipos de usuario
USER_TYPE_ADMIN = 1
USER_TYPE_PROFESOR = 2
USER_TYPE_AlUMNO = 3
USER_TYPE_TUTOR = 4

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('El nombre de usuario debe ser proporcionado')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Esto encripta la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    PROFESOR = 2
    ALUMNO = 3
    TUTOR = 4
    USER_TYPE_CHOICES = (
        (ADMIN, 'Admin'),
        (PROFESOR, 'Profesor'),
        (ALUMNO, 'Alumno'),
        (TUTOR, 'Tutor'),
    )
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=ALUMNO)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion
        
class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Tutor(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField(max_length=60)
    telefono = models.CharField(max_length=20, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    username = models.CharField(unique=True, max_length=20, null=True)
    password = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre
        

class Alumno(AbstractBaseUser, PermissionsMixin):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=12)
    nivel_educacion = models.CharField(max_length=10, choices=[('basica', 'Básica'), ('media', 'Media'), ('superior', 'Superior')])
    direccion = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField(max_length=60)
    telefono = models.CharField(max_length=20, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    username = models.CharField(unique=True, max_length=20, null=False, default='default_username')
    password = models.CharField(max_length=100, default='default_password')
    id_tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        Group,
        related_name='alumnos_groups',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='alumnos_permissions',  
        blank=True
    )

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=12)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)
    direccion = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField(max_length=60)
    telefono = models.CharField(max_length=20)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    username = models.CharField(unique=True, max_length=20, null=True)
    password = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

class Clase(models.Model):
    id_clase = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=60)
    modalidad = models.CharField(max_length=10, choices=[('online', 'Online'), ('presencial', 'Presencial')])
    horario = models.TimeField()
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_curso

class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)  # Cambiado de CustomUser a Alumno
    id_clase = models.ForeignKey(Clase, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_alumno.nombre} inscrito en {self.id_clase.nombre_curso}'


