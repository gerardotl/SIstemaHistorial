# Generated by Django 4.2.1 on 2023-05-23 01:11

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=65, verbose_name='Nombres')),
                ('apellido', models.CharField(max_length=65, verbose_name='Apellidos')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='N de documento')),
                ('fecha_nacimiento', models.DateField(default=datetime.date.today, verbose_name='Fecha de nacimiento')),
                ('genero', models.PositiveIntegerField(choices=[(1, 'MASCULINO'), (2, 'FEMENINO')], default=1, verbose_name='Género')),
                ('email', models.EmailField(blank=True, max_length=45, null=True, unique=True, verbose_name='Correo electrónico')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono')),
                ('celular', models.CharField(blank=True, max_length=10, null=True, verbose_name='Celular')),
                ('direccion', models.CharField(blank=True, max_length=60, null=True, verbose_name='Dirección')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
            ],
            options={
                'db_table': 'paciente',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('dni', models.CharField(max_length=13, unique=True, verbose_name='N de documento')),
                ('fecha_nacimiento', models.DateField(default=datetime.date.today, verbose_name='Fecha de nacimiento')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono')),
                ('celular', models.CharField(blank=True, max_length=10, null=True, verbose_name='Celular')),
                ('direccion', models.CharField(blank=True, max_length=40, null=True, verbose_name='Dirección')),
                ('genero', models.PositiveIntegerField(choices=[(1, 'MASCULINO'), (2, 'FEMENINO')], default=1, verbose_name='Género')),
                ('tipo', models.PositiveIntegerField(choices=[(1, 'ENFERMERA/O'), (2, 'MÉDICO')], default=1, verbose_name='Tipo')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usuario',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ficha_Medica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('diagnostico', models.CharField(max_length=200, verbose_name='Diagnostico')),
                ('tratamiento', models.CharField(max_length=200, verbose_name='Tratamiento')),
                ('observacion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Observación')),
                ('alta', models.BooleanField(default=False, verbose_name='Dado de alta')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ficha_medica_paciente', to='App.paciente', verbose_name='Paciente')),
            ],
            options={
                'db_table': 'ficha_medica',
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('motivo', models.CharField(max_length=200, verbose_name='Motivo')),
                ('observacion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Observación')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='consulta_paciente', to='App.paciente', verbose_name='Paciente')),
            ],
            options={
                'db_table': 'consulta',
            },
        ),
    ]
