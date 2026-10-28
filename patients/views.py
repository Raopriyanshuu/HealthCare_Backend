
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Patient, PatientDoctorMapping
from .serializers import PatientSerializer, PatientDoctorMappingSerializer




class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)







class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__owner=self.request.user
        ).select_related("patient", "doctor")

    
    def _validate_patient_ownership(self, patient):
        if patient.owner_id != self.request.user.id:
            raise ValidationError({
                "patient": "You can only assign doctors to your own patients."
            })

    def perform_create(self, serializer):
        self._validate_patient_ownership(
            serializer.validated_data["patient"]
        )
        serializer.save()

    def perform_update(self, serializer):
        patient = serializer.validated_data.get(
            "patient",
            self.get_object().patient,
        )
        self._validate_patient_ownership(patient)
        serializer.save()
