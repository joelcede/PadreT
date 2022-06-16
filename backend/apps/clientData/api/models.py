from django.db import models
from ...procedure.api.models import GeneralProcedure
# Create your models here.

class ClientData(models.Model):
    # CONTACT
    mail = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=10)

    procedure = models.ForeignKey(GeneralProcedure, related_name="client_data", on_delete=models.CASCADE) #One

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = "Datos del cliente"
        verbose_name_plural = "Datos de los clientes"
    
    def __str__(self) -> str:
        return self.telephone

class HousesClient(models.Model):
    # LOCATION
    country = models.CharField(max_length=50, blank=True, default="Ecuador")
    province = models.CharField(max_length=50, default="Guayas")
    town = models.CharField(max_length=50, blank=True, default="Guayaquil")
    parish = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    main_road_name = models.CharField(max_length=100)
    cross_road_name = models.CharField(max_length=100, blank=True)

    client_data = models.ForeignKey(ClientData, related_name="houses_customer", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = "Casa del cliente"
        verbose_name_plural = "Casas del cliente"
    
    def __str__(self) -> str:
        return self.main_road_name

class Cadastral(models.Model):
    sector = models.CharField(max_length=3)
    apple = models.CharField(max_length=4)
    lot = models.CharField(max_length=3)
    div1 = models.CharField(max_length=1, default="0", blank=True)
    div2 = models.CharField(max_length=1, default="0", blank=True)
    div3 = models.CharField(max_length=1, default="0", blank=True)
    div4 = models.CharField(max_length=1, default="1", blank=True)

    home_client = models.ForeignKey(HousesClient, related_name="house_cadastral", on_delete=models.CASCADE) #One

    def __str__(self) -> str:
        return f"{self.sector}-{self.apple}-{self.lot}-{self.div1}-{self.div2}-{self.div3}-{self.div4}"

class MunicipalAccount(models.Model):
    user = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

    client_data = models.ForeignKey(ClientData, related_name="municipal_account", on_delete=models.CASCADE) #One

    def __str__(self) -> str:
        return self.user

class Person(models.Model):
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

    #Other
    is_principal = models.BooleanField(default=False)

    client_data = models.ForeignKey(ClientData, related_name="person_identification", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Datos de la persona"
        verbose_name_plural = "Datos de las personas"

    def __str__(self) -> str:
        return self.dni
