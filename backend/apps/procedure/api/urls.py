from django.urls import path, re_path
from . import views


urlpatterns = [
    path('all/', views.get_data_all, name="get_all"),
    path('active/', views.get_active, name="get_active"),
    path('successfull_job/', views.get_successfull_job, name="get_successfull_job"),
    path('', views.SearchClientDataView.as_view(), name="search_data_client"),
    path('create/', views.create_procedure, name="create_data"),
    path('create_client_data/', views.create_client_data, name="create_client_data"),
    path('create_municipal_account/', views.create_municipal_account, name="create_municipal_account"),
    path('create_person/', views.create_person, name="create_person"),
    path('cadastral/', views.cadastral, name="create_cadastral"),
    path('responsible/', views.responsibles_data, name="create_responsible"),
    path('update_procedure/<int:pk>/', views.update_procedure, name="update_data"),
    path('update_client_data/<int:pk>/', views.update_client_data, name="update_client_data"),
    path('update_municipal_account/<int:pk>/', views.update_municipal_account, name="update_municipal_account"),
    path('update_person/<int:pk>/', views.update_person, name="update_person"),
    path('update_cadastral/<int:pk>/', views.update_cadastral, name="update_cadastral"),
    path('update_responsible/<int:pk>/', views.update_responsibles_data, name="update_responsible"),
]
