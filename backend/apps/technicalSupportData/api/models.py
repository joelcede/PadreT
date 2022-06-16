from django.db import models
from ...procedure.api.models import GeneralProcedure

# Create your models here.

class ResponsibleData(models.Model):
    #Identification
    dni = models.CharField(max_length=10, unique=True)
    type_identification_document = models.CharField(max_length=10, default="cedula")

    # NAMES
    fisrt_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25, blank=True)
    father_surname = models.CharField(max_length=25)
    mother_surname = models.CharField(max_length=25, blank=True)

    # CONTACT
    mobile = models.CharField(max_length=10, blank=True)

    procedure = models.ForeignKey(GeneralProcedure, related_name="responsible_technical", on_delete=models.CASCADE) #One

    class Meta:
        verbose_name = "Responsible Data"
        verbose_name_plural = "Responsibles Data"

    def __str__(self) -> str:
        return self.dni
