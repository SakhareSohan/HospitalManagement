from django.shortcuts import render, redirect
from .backends import DoctorBackend, PatientBackend
from django.contrib.auth import login, authenticate
from django.views import View
from django.contrib import messages
from .forms import AdminLoginForm, DoctorRegistrationForm, DoctorLoginForm, PatientRegistrationForm, PatientLoginForm
from .models import Doctor, Patient
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import BACKEND_SESSION_KEY
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test


def index(request):
    # Your logic for the doctor dashboard goes here
    return render(request, 'index.html')

class AdminLoginView(View):
    template_name = 'admin_login.html'
    form_class = AdminLoginForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Hardcoded username and password for demonstration
            expected_username = 'root'
            expected_password = 'root@123'

            entered_username = form.cleaned_data['username']
            entered_password = form.cleaned_data['password']

            # Check if the user with the given username exists
            user = User.objects.filter(username=expected_username).first()

            if user:
                # If the user exists, check the password and log in
                if user.check_password(expected_password):
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    messages.success(request, 'Successfully logged in as admin.')
                    return redirect('HospitalA:admin_dashboard')
                else:
                    messages.error(request, 'Invalid login credentials.')
            else:
                # If the user does not exist, create a new user and log in
                user = User.objects.create_user(username=expected_username, password=expected_password)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, 'Successfully logged in as admin.')
                return redirect('HospitalA:admin_dashboard')

        return render(request, self.template_name, {'form': form})

#Admin Dashboard

@login_required(login_url='/hospital_admin/login/')
def admin_dashboard(request):
    # Your logic for admin dashboard goes here
    return render(request, 'admin_dashboard.html')

#Doctor

@login_required(login_url='/hospital_admin/login/')
def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor registered successfully!')
            return redirect('HospitalA:admin_dashboard')
    else:
        form = DoctorRegistrationForm()

    return render(request, 'register_doctor.html', {'form': form})

class DoctorLoginView(View):
    template_name = 'doctor_login.html'
    form_class = DoctorLoginForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            license_number = form.cleaned_data['license_number']
            password = form.cleaned_data['password']

            user = DoctorBackend().authenticate(request, license_number=license_number, password=password)

            if user is not None:
                login(request, user, backend = 'HospitalA.backends.DoctorBackend')
                messages.success(request, 'Successfully logged in as doctor.')
                return redirect('HospitalA:doctor_dashboard')
            else:
                messages.error(request, 'Invalid login credentials.')

        return render(request, self.template_name, {'form': form})


@user_passes_test(lambda u: u.is_authenticated == False, login_url='/doctor/login/')
def doctor_dashboard(request):
    
    return render(request, 'doctor_dashboard.html')

#Patient

@user_passes_test(lambda u: u.is_authenticated == False, login_url='/doctor/login/')
def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient registered successfully!')
            return redirect('HospitalA:doctor_dashboard')  # Redirect to doctor dashboard after patient registration
    else:
        form = PatientRegistrationForm()

    return render(request, 'register_patient.html', {'form': form})

class PatientLoginView(View):
    template_name = 'patient_login.html'
    form_class = PatientLoginForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            unique_code = form.cleaned_data['unique_code']
            password = form.cleaned_data['password']

            user = PatientBackend().authenticate(request, unique_code=unique_code, password=password)

            if user is not None:
                login(request, user, backend = 'HospitalA.backends.PatientBackend')
                messages.success(request, 'Successfully logged in as patient.')
                return redirect('HospitalA:patient_dashboard')
            else:
                messages.error(request, 'Invalid login credentials.')

        return render(request, self.template_name, {'form': form})


@user_passes_test(lambda u: u.is_authenticated == False, login_url='/patient/login/')
def patient_dashboard(request):
    # Your logic for the doctor dashboard goes here
    return render(request, 'patient_dashboard.html')