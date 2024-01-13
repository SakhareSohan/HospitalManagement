from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission

class Admin(models.Model):
    username = models.CharField(max_length=50, default='root', unique=True)
    password = models.CharField(max_length=255, default='root@123')

class Doctor(AbstractUser):
    license_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    username = models.CharField(max_length=30, unique=False, default="Doctor")
    first_name = models.CharField(max_length=30, default="Hospital")
    last_name = models.CharField(max_length=30, default="A")
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    backend = models.CharField(max_length=255, default='HospitalA.backends.DoctorBackend')
            

    groups = models.ManyToManyField(Group, related_name='doctor_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='doctor_user_permissions')

class Patient(AbstractUser):
    unique_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    allergies = models.TextField()
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(default="patient@gmail.com")
    emergency_contact = models.CharField(max_length=15)
    chronic_disease = models.CharField(max_length=100, blank=True, null=True)  # Changed to CharField
    username = models.CharField(max_length=30, unique=False, default="Patient")
    first_name = models.CharField(max_length=30, default="Patient")
    last_name = models.CharField(max_length=30, default="Panvel")
    backend = models.CharField(max_length=255, default='HospitalA.backends.PatientBackend')

    groups = models.ManyToManyField(Group, related_name='patient_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='patient_user_permissions')

from django.contrib.auth import get_user_model

class LoginLog(models.Model):
    user_type = models.CharField(max_length=10, default=Doctor)  # Add a field to distinguish between 'Doctor' and 'Patient'
    user_id = models.PositiveIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_type} - {self.user_id} - {self.timestamp}"

