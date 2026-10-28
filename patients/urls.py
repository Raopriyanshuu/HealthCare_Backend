
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientDoctorMappingViewSet

router = DefaultRouter()

router.register("patients", PatientViewSet, basename="patient")
router.register(
    "patient-doctor-mappings",
    PatientDoctorMappingViewSet,
    basename="patient-doctor-mapping",
)

urlpatterns = router.urls
