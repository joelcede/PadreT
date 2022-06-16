from django.contrib import admin

from .api.models import (
    Person, MunicipalAccount, Cadastral,
    HousesClient, ClientData
)
# Register your models here.

admin.site.register(Person)
admin.site.register(MunicipalAccount)
admin.site.register(Cadastral)
admin.site.register(HousesClient)
admin.site.register(ClientData)