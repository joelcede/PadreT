from django.db import models
# Create your models here.

class CadastralData(models.Model):
    sector = models.CharField(max_length=3)
    apple = models.CharField(max_length=4)
    lot = models.CharField(max_length=3)
    div1 = models.CharField(max_length=1, default="0", blank=True)
    div2 = models.CharField(max_length=1, default="0", blank=True)
    div3 = models.CharField(max_length=1, default="0", blank=True)
    div4 = models.CharField(max_length=1, default="1", blank=True)

    #Others
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = "Catastro de la casa"
        verbose_name_plural = "Catastro de las casas"

    def __str__(self) -> str:
        return f"{self.sector}-{self.apple}-{self.lot}-{self.div1}-{self.div2}-{self.div3}-{self.div4}"  

class PersonData(models.Model):
    #Identification
    dni = models.CharField(max_length=13, unique=True)
    type_identification_document = models.CharField(max_length=10, default="cedula")

    # NAMES
    fisrt_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30, blank=True)
    father_surname = models.CharField(max_length=30)
    mother_surname = models.CharField(max_length=30, blank=True)

    # CONTACT
    mobile = models.CharField(max_length=10, blank=True)

    #Other
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = "Datos de la persona"
        verbose_name_plural = "Datos de las personas"

    def __str__(self) -> str:
        return self.dni

class OwnerData(models.Model):
    #ForeignKey
    id_person_data = models.OneToOneField(PersonData, related_name="person_data", on_delete=models.CASCADE, db_column="id_person_data")

    #Body
    is_principal = models.BooleanField(default=False, blank=True)
    
    #Other
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = "Datos del Propietario"
        verbose_name_plural = "Datos de los propietarios"

    def __str__(self) -> str:
        return f"{self.id_person_data.fisrt_name} {self.id_person_data.father_surname}"

class ResponsibleData(models.Model):
    #OneToOneField
    id_person_data = models.OneToOneField(PersonData, related_name="responsible_data", on_delete=models.CASCADE, db_column="id_person_data")

    #Body
    email = models.EmailField(max_length=50, blank=True)
    #Other
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = "Datos del responsable tecnico"
        verbose_name_plural = "Datos de los responsables tecnicos"

    def __str__(self) -> str:
        return f"{self.id_person_data.fisrt_name} {self.id_person_data.father_surname}"

class MunicipalAccountData(models.Model):
    #Credentials
    user = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

    #Others
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = "Credencial municipal"
        verbose_name_plural = "Credenciales municipales"  

    def __str__(self) -> str:
        return self.user

class HouseClientData(models.Model):
    #Key's
    id_owner_data = models.ForeignKey(OwnerData, related_name="owner_data", on_delete=models.CASCADE, db_column="id_owner_data")
    id_responsible_data = models.OneToOneField(ResponsibleData, related_name="responsible_data", on_delete=models.CASCADE, db_column="id_responsible_data")
    id_municipal_account_data = models.OneToOneField(MunicipalAccountData, related_name="municipal_account_data", on_delete=models.CASCADE, db_column="id_municipal_account_data")
    id_cadastral_data = models.OneToOneField(CadastralData, related_name="cadastral_data", on_delete=models.CASCADE, db_column="id_cadastral_data")

    # LOCATION
    image = models.URLField(max_length=200, blank=True)
    country = models.CharField(max_length=50, blank=True, default="Ecuador")
    province = models.CharField(max_length=50, default="Guayas")
    town = models.CharField(max_length=50, blank=True, default="Guayaquil")
    parish = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    main_road_name = models.CharField(max_length=100)
    cross_road_name = models.CharField(max_length=100, blank=True)
    coordinates = models.URLField(max_length=500, blank=True)
    conventional = models.CharField(max_length=10, blank=True)

    #OTHERS
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = "Casa del cliente"
        verbose_name_plural = "Casas del cliente"
    
    def __str__(self) -> str:
        return self.main_road_name
