
from rest_framework import serializers
from .models import Patient, PatientDoctorMapping


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "age",
            "gender",
            "address",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_age(self, value):
        if value > 120:
            raise serializers.ValidationError(
                "Age must be 120 or below."
            )
        return value





class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(
        source="doctor.name",
        read_only=True,
    )
    patient_name = serializers.CharField(
        source="patient.name",
        read_only=True,
    )

    class Meta:
        model = PatientDoctorMapping
        fields = [
            "id",
            "patient",
            "patient_name",
            "doctor",
            "doctor_name",
            "assigned_at",
        ]
        read_only_fields = ["id", "assigned_at"]
