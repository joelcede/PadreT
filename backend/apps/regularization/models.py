from django.db import models
from django.core.validators import MinValueValidator ,MaxValueValidator
from datetime import datetime

"""Datos del predio"""
class Edification(models.Model):
    number_buildings = models.PositiveIntegerField(default=1)
    total_construction_area = models.FloatField()

class ServiceAccess(models.Model):
    drinking_water = models.BooleanField(verbose_name="Agua Potable")
    electric_power = models.BooleanField(verbose_name="Energia Electrica")
    sewerage = models.BooleanField(verbose_name="Alcantarillado")
    sidewalks = models.BooleanField(verbose_name="Aceras")
    keratin = models.BooleanField(verbose_name="Bordillos")
    paved_street = models.BooleanField(verbose_name="Calle Pavimentada")

class PropertyData(models.Model):
    cadastral_code = models.CharField(max_length=14)
    sector = models.CharField(max_length=3)
    mz = models.CharField(max_length=4)
    lot = models.CharField(max_length=3)
    div = models.CharField(max_length=4)
    property_address = models.CharField(max_length=100)
    parish = models.CharField(max_length=50)
    service_access = models.ForeignKey(ServiceAccess, on_delete=models.CASCADE)
    edification = models.ForeignKey(Edification, on_delete=models.CASCADE)

"""Datos de las Edificaciones"""
class EdificationData(models.Model):
    # Edificación principal
    number_loors = models.PositiveIntegerField()
    height = models.FloatField()
    construction_area = models.FloatField()
    building_use = models.CharField()
    finished_construction = models.BooleanField()
    age_building = models.PositiveIntegerField()

    # Materiales de construcción
    structure = models.CharField(max_length=25)
    walls = models.CharField(max_length=25)
    floors = models.CharField(max_length=25)
    overlays = models.CharField(max_length=25)
    deck = models.CharField(max_length=25)
    lying_down = models.CharField(max_length=25)


"""Datos de las actividades desarrolladas en el predio"""
class PropertyActivityData(models.Model):
    activity = models.CharField(max_length=250)
    local_measures = models.FloatField()
    local_area = models.FloatField()
    independent_access = models.BooleanField()
    antique_commerce = models.PositiveIntegerField()
    last_enabling_enable = models.PositiveIntegerField(
        validators=[
            MinValueValidator(int(datetime.today().strftime("%Y")) - 90),
            MaxValueValidator(int(datetime.today().strftime("%Y")) - 18)
        ]
    )

    class Meta: 
        verbose_name = "Datos de la actividad desarrollada en el predio"
        verbose_name_plural = "Datos de la actividades desarrolladas en el predio"

class UserDataProperty(models.Model):
    property_data = models.ForeignKey(PropertyData, on_delete=models.CASCADE)
    edification_data = models.ForeignKey(EdificationData, on_delete=models.CASCADE)
    property_activity_data = models.ForeignKey(PropertyActivityData, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Datos de la propiedad del propietario"
        verbose_name_plural = "Datos de las propiedades de los propietarios"

