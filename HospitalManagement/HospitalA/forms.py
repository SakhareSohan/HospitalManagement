from django import forms
from .models import Doctor, Patient

class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=50, initial='root')  # Set default username
    password = forms.CharField(widget=forms.PasswordInput, initial='root@123')  # Set default password

class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['license_number', 'name', 'mobile_number', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class DoctorLoginForm(forms.Form):
    license_number = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'allergies', 'mobile_number', 'emergency_contact', 'chronic_disease', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class PatientLoginForm(forms.Form):
    unique_code = forms.UUIDField()
    password = forms.CharField(widget=forms.PasswordInput)
