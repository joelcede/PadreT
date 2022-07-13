from django.db import models
# Create your models here.

class GeneralProcedure(models.Model):
    successfull_job = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.id)

class TypeProcedure(models.Model):
    name = models.CharField(max_length=50, default="Regularización")

    general_procedure = models.ForeignKey(GeneralProcedure, related_name="type_procedure", on_delete=models.CASCADE) #One

    def __str__(self) -> str:
        return self.name