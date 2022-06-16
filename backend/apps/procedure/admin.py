from django.contrib import admin

from .api.models import TypeProcedure, GeneralProcedure
# Register your models here.
admin.site.register(TypeProcedure)
admin.site.register(GeneralProcedure)
