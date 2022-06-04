from django.db import models

# Create your models here.

class IdentificationDocument(models.Model):
    dni = models.CharField(max_length=10, unique=True)
    type_identification_document = models.CharField(max_length=10, default="cedula")

    # NAMES
    fisrt_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25, blank=True)
    father_surname = models.CharField(max_length=25)
    mother_surname = models.CharField(max_length=25, blank=True)

    class Meta:
        verbose_name = "Documento de Identificacion"
        verbose_name_plural = "Documentos de Identificacion"

    def __str__(self):
        return self.dni

class ClientData(models.Model):
    # IDENTIFICATION
    identification_id = models.ForeignKey(IdentificationDocument, on_delete=models.CASCADE)

    # CONTACT
    mail = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10, blank=True)

    # LOCATION
    country = models.CharField(max_length=50, blank=True, default="Ecuador")
    province = models.CharField(max_length=50, default="Guayas")
    town = models.CharField(max_length=50, blank=True, default="Guayaquil")
    parish = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    main_road_name = models.CharField(max_length=100)
    cross_road_name = models.CharField(max_length=100, blank=True)

    #Date
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Datos del cliente"
        verbose_name_plural = "Datos de los clientes"

    def __str__(self):
        return self.dni