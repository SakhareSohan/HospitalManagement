from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HospitalA/', include('HospitalA.urls')),
    path('', include('HospitalA.urls')),
]
