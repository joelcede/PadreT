from django.urls import path, re_path
from . import views


urlpatterns = [
    path('all/', views.get_data_all, name="get_all"),
    path('active/', views.get_active, name="get_active"),
    path('successfull_job/', views.get_successfull_job, name="get_successfull_job"),
    path('search/', views.PersonView.as_view(), name="get_data_dni"),
    #path(r'^active$', views.DniDataList.as_view(), name="get_data_dni"),
]
