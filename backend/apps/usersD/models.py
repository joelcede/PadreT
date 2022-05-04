from django.db import models

IDENTIFICATION_DOCUMENT = [
    ('Cedula', 'Cedula'),
    ('Pasaporte', 'Pasaporte')
]
GENDER = [
    ('Mujer', 'Mujer'),
    ('Hombre', 'Hombre'),
    ('UNDEFINED', 'UNDEFINED')
]
MARITAL_STATUS = [
    ('Soltero/a', 'Soltero/a'),
    ('Casado/a', 'Casado/a'),
    ('Unión libre', 'Unión libre'),
    ('Separado/a', 'Separado/a')
]
LEVEL_OF_INSTRUCTION = [
    ('Primaria','Primaria'),
    ('Secundaria', 'Secundaria'),
    ('3er nivel', '3er nivel'),
    ('4to nivel', '4to nivel')
]
# Create your models here.

class ProvinceList(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    # DNI
    dni = models.CharField(max_length=10, unique=True, verbose_name="Número del Identidad")
    type_identification_document = models.CharField(
        max_length=10, choices=IDENTIFICATION_DOCUMENT, 
        default=IDENTIFICATION_DOCUMENT[0][0], verbose_name="Tipo de Identidad"
    )
    
    # NAMES
    fisrt_name = models.CharField(max_length=20, verbose_name="Primer nombre")
    second_name = models.CharField(max_length=20, blank=True, verbose_name="Segundo nombre")
    father_surname = models.CharField(max_length=20, verbose_name="Apellido Paterno")
    mother_surname = models.CharField(max_length=20, blank=True, verbose_name="Apellido Materno")

    # LOCATION
    country = models.CharField(max_length=50, verbose_name="Pais", blank=True, default="Ecuador")
    province = models.ForeignKey(
        ProvinceList, on_delete=models.CASCADE, 
        default="Guayas", verbose_name="Provincia", blank=True
    )
    town = models.CharField(max_length=50, verbose_name="Ciudad", blank=True, default="Guayaquil")
    parish = models.CharField(max_length=100, verbose_name="Parroquia", blank=True)
    district = models.CharField(max_length=100, verbose_name="Ciudadela/Coorperativa/Barrio", blank=True)
    main_road_name = models.CharField(max_length=100, verbose_name="Calle principal")
    cross_road_name = models.CharField(max_length=100, verbose_name="Calle transversal", blank=True)

    # CONTACT
    mail = models.EmailField(max_length=100, unique=True, verbose_name="Correo Electronico")
    password = models.CharField(max_length=30, verbose_name="Contraseña")
    phone = models.CharField(max_length=10, verbose_name="Telefono convensional")
    mobile = models.CharField(max_length=10, blank=True, verbose_name="Celular")

    # ADDITIONAL INFORMATION
    gender = models.CharField(max_length=10, choices=GENDER ,blank=True, verbose_name="Genero")
    marital_status = models.CharField(
        max_length=15, choices=MARITAL_STATUS, 
        blank=True, verbose_name="Estado civil"
    )
    level_of_instruction = models.CharField(
        max_length=25, choices=LEVEL_OF_INSTRUCTION, 
        blank=True, verbose_name="Nivel de Instrucción"
    )
    occupation = models.CharField(max_length=50, blank=True, verbose_name="Ocupación")

    #Date
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def __str__(self):
        return self.dni
