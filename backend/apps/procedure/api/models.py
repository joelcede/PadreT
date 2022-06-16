from django.db import models
# Create your models here.

class GeneralProcedure(models.Model):
    status = models.BooleanField(default=True)

class TypeProcedure(models.Model):
    name = models.CharField(max_length=50)

    general_procedure = models.ForeignKey(GeneralProcedure, related_name="type_procedure", on_delete=models.CASCADE) #One

    def __str__(self) -> str:
        return self.name