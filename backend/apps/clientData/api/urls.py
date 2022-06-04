from django.urls import path
from ..api import views

urlpatterns = [
    path("client_data/", views.identificationApi, name="api_identification")
]
