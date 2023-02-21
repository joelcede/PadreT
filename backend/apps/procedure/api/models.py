from django.db import models

from ...clientData.api.models import HouseClientData
# Create your models here.

class GeneralProcedure(models.Model):
    #Choices
    PROGRESS_CHOICE = [
        ('inp', 'En progreso'),
        ('fin', 'Finalizado'),
        ('rec', 'Rectificación'),
        ('anu', 'Anulado')
    ]

    #ForeignKey
    id_house = models.ForeignKey(HouseClientData, related_name="house_clients", on_delete=models.CASCADE, db_column="id_house")

    #Body
    successfull_job = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    progress = models.CharField(max_length=25, choices=PROGRESS_CHOICE)
    record = models.CharField(max_length=15, blank=True)

    #Other
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self) -> str:
        return self.progress
