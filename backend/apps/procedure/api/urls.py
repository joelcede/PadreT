from django.urls import path, re_path
from ...clientData.api import views as vs
from . import views


urlpatterns = [
    path('get_all_cadastral/', vs.getCadastralAll, name="get_all_cadastral"),
    path('get_all_persons/', vs.getPersonAll, name="get_all_persons"),
    path('get_all_owners/', vs.getOwnerAll, name="get_all_owners"),
    path('get_all_responsible/', vs.getResponsibleAll, name="get_all_responsible"),
    path('get_all_municipal_accounts/', vs.getMunicipalAccountAll, name="get_all_municipal_accounts"),
    path('get_all_houses/', vs.getHousesClientsAll, name="get_all_houses"),
    path('get_owner_x_person/<int:id>', vs.get_person_x_owner, name="get_owner_x_person"),
    path('post_cadastral/', vs.postCadastral, name="post_cadastral"),
    path('post_persons/', vs.postPerson, name="post_persons"),
    path('post_owner/', vs.postOwner, name="post_owner"),
    path('post_responsible/', vs.postResponsible, name="post_responsible"),
    path('post_municipal_account/', vs.postMunicipalAccount, name="post_municipal_account"),
    path('post_house/', vs.postHouseClient, name="post_house")
    # path('all/', views.get_data_all, name="get_all"),
    # path('get_all_persons/', vs.get_PersonData, name="get_all_persons"),
    # path('get_all_houses/', vs.get_HousesData, name="get_all_houses"),
    # path('get_all_clients/', vs.get_OwnerData, name="get_all_clients"),
    # path('active/', views.get_active, name="get_active"),
    # path('successfull_job/', views.get_successfull_job, name="get_successfull_job"),
    # #path('', views.SearchClientDataView.as_view(), name="search_data_client"),
    # path('create/', views.create_procedure, name="create_data"),
    # path('create_client_data/', views.create_client_data, name="create_client_data"),
    # path('create_municipal_account/', views.create_municipal_account, name="create_municipal_account"),
    # path('create_person/', views.create_person, name="create_person"),
    # path('cadastral/', views.cadastral, name="create_cadastral"),
    # #path('responsible/', views.responsibles_data, name="create_responsible"),
    # path('update_procedure/<int:pk>/', views.update_procedure, name="update_data"),
    # path('update_client_data/<int:pk>/', views.update_client_data, name="update_client_data"),
    # path('update_municipal_account/<int:pk>/', views.update_municipal_account, name="update_municipal_account"),
    # path('update_person/<int:pk>/', views.update_person, name="update_person"),
    # path('update_cadastral/<int:pk>/', views.update_cadastral, name="update_cadastral"),
    # #path('update_responsible/<int:pk>/', views.update_responsibles_data, name="update_responsible"),
    # path('post_person/', vs.post_PersonData, name="post_data_person"),
    # path('get_owner/', vs.get_OwnerData, name="create_owner"),
    # path('create_owner/', vs.create_ownerData, name="create_owner")
]
