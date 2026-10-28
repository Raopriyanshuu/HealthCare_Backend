
from django.db import models


class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ("Cardiology", "Cardiology"),
        ("Dermatology", "Dermatology"),
        ("Neurology", "Neurology"),
        ("Pediatrics", "Pediatrics"),
        ("General", "General Medicine"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=150)
    specialization = models.CharField(
        max_length=50,
        choices=SPECIALIZATION_CHOICES,
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.specialization}"
