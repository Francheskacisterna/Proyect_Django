# Generated by Django 5.0.6 on 2024-06-30 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id_clase', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_curso', models.CharField(max_length=60)),
                ('modalidad', models.CharField(choices=[('online', 'Online'), ('presencial', 'Presencial')], max_length=10)),
                ('horario', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id_alumno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=12)),
                ('nivel_educacion', models.CharField(choices=[('basica', 'Básica'), ('media', 'Media'), ('superior', 'Superior')], max_length=10)),
                ('direccion', models.CharField(max_length=60)),
                ('fecha_nacimiento', models.DateField()),
                ('correo_electronico', models.EmailField(max_length=60)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('genero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alumnos.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id_inscripcion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inscripcion', models.DateField()),
                ('id_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumno')),
                ('id_clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.clase')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id_profesor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=12)),
                ('especialidad', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('fecha_nacimiento', models.DateField()),
                ('correo_electronico', models.EmailField(max_length=60)),
                ('telefono', models.CharField(max_length=20)),
                ('genero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alumnos.genero')),
            ],
        ),
        migrations.AddField(
            model_name='clase',
            name='id_profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.profesor'),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id_tutor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=60)),
                ('fecha_nacimiento', models.DateField()),
                ('correo_electronico', models.EmailField(max_length=60)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('genero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alumnos.genero')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='id_tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alumnos.tutor'),
        ),
    ]
