from django.contrib import admin

from .api.models import (
    CadastralModel, PersonModel, OwnerModel, ResponsibleModel,
    MunicipalAccountModel, HouseClientModel
)
# Register your models here.

admin.site.register(CadastralModel)
admin.site.register(PersonModel)
admin.site.register(OwnerModel)
admin.site.register(ResponsibleModel)
admin.site.register(MunicipalAccountModel)
admin.site.register(HouseClientModel)