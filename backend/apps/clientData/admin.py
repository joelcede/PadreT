from django.contrib import admin

from .api.models import (
    MunicipalAccountData, PersonData, CadastralData,
    HouseClientData, OwnerData, ResponsibleData
)
# Register your models here.

admin.site.register(PersonData)
admin.site.register(MunicipalAccountData)
admin.site.register(CadastralData)
admin.site.register(HouseClientData)
admin.site.register(OwnerData)
admin.site.register(ResponsibleData)