from django.urls import path
from ..api import views

urlpatterns = [
    path('all/', views.getDataAll, name="general")
]
