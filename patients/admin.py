
from django.contrib import admin
from .models import Patient, PatientDoctorMapping


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "gender", "owner", "created_at")
    search_fields = ("name", "owner__email")
    list_filter = ("gender",)


@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "doctor", "assigned_at")
    search_fields = ("patient__name", "doctor__name")
