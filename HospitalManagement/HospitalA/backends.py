from django.contrib.auth.backends import ModelBackend
from .models import Doctor, LoginLog, Patient
from django.utils import timezone
from django.contrib.auth.models import User

class DoctorBackend(ModelBackend):
    def authenticate(self, request, license_number=None, password=None, **kwargs):
        doctors = Doctor.objects.filter(license_number=license_number)

        if doctors.exists() and doctors.count() == 1:
            doctor = doctors.first()

            # Direct password comparison (not recommended for production)
            if password == doctor.password:
                last_login = timezone.now()
                # Create a login log entry
                LoginLog.objects.create(user_type='Doctor', user_id=doctor.id)

                return doctor

        return None

class PatientBackend(ModelBackend):
    def authenticate(self, request, unique_code=None, password=None, **kwargs):
        patient = Patient.objects.filter(unique_code=unique_code)

        if patient.exists() and patient.count() == 1:
            patient = patient.first()
            
            # Direct password comparison (not recommended for production)
            if password == patient.password:
                last_login = timezone.now()
                # Create a login log entry
                LoginLog.objects.create(user_type='Patient', user_id=patient.id)

                return patient

        return None
