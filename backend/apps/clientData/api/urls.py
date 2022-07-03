from django.urls import path
from ..api import views

urlpatterns = [
    path("active_users/", views.getDataActive, name="active_users"),
    path("post_data/", views.postData, name="data_post")
]
