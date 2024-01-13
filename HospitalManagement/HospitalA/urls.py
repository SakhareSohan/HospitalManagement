from django.urls import path
from . import views

app_name = 'HospitalA'

urlpatterns = [
    path('', views.index, name='index'),

    # Admin URLs
    path('hospital_admin/login/', views.AdminLoginView.as_view(), name='admin-login'),
    path('hospital_admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Doctor URLs
    path('hospital_admin/register_doctor/', views.register_doctor, name='register-doctor'),
    path('doctor/login/', views.DoctorLoginView.as_view(), name='doctor-login'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),

    # Patient URLs
    path('doctor/register_patient/', views.register_patient, name='register-patient'),
    path('patient/login/', views.PatientLoginView.as_view(), name='patient-login'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
]
