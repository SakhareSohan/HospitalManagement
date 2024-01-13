# Generated by Django 4.2.6 on 2024-01-13 22:20

import HospitalA.models
import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='root', max_length=50, unique=True)),
                ('password', models.CharField(default='root@123', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LoginLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(default=HospitalA.models.Doctor, max_length=10)),
                ('user_id', models.PositiveIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('unique_code', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('allergies', models.TextField()),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(default='patient@gmail.com', max_length=254)),
                ('emergency_contact', models.CharField(max_length=15)),
                ('chronic_disease', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(default='Patient', max_length=30)),
                ('first_name', models.CharField(default='Patient', max_length=30)),
                ('last_name', models.CharField(default='Panvel', max_length=30)),
                ('backend', models.CharField(default='HospitalA.backends.PatientBackend', max_length=255)),
                ('groups', models.ManyToManyField(related_name='patient_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='patient_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('license_number', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(default='Doctor', max_length=30)),
                ('first_name', models.CharField(default='Hospital', max_length=30)),
                ('last_name', models.CharField(default='A', max_length=30)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
                ('backend', models.CharField(default='HospitalA.backends.DoctorBackend', max_length=255)),
                ('groups', models.ManyToManyField(related_name='doctor_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='doctor_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
