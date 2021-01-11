from django.urls import path,include
from . import views
from ingest.views import *

urlpatterns = [
    
    #URL For User Login
    path('mlaas/ingest/user/login',UserLoginClass.as_view()),

    #URL For Create Project
    path('mlaas/ingest/create_project/',CreateProjectClass.as_view()),

    #URL For Create Dataset
    path('mlaas/ingest/create_dataset/',CreateDatasetClass.as_view()),

    #URL For Data Detail(CSV File)
    path('mlaas/ingest/data_detail/',DataDetailClass.as_view()),

    #URL For Data Detail Column List (CSV File)
    path('mlaas/ingest/data_detail_column_list/',DataDetailColumnListClass.as_view()),

    #URL For delete Project Detail
    path('mlaas/ingest/delete/project_detail/',DeleteProjectDetailClass.as_view()),

    #URL For delete dataset Detail
    path('mlaas/ingest/delete/dataset_detail/',DeleteDatasetDetailClass.as_view()),

    #URL For delete data Detail
    path('mlaas/ingest/delete/data_detail/',DeleteDataDetailClass.as_view()),

    #URL For dataset Schema
    path('mlaas/ingest/dataset_schema/', DatasetSchemaClass.as_view()),

    #path('mlaas/logging/',ToggleLogs.as_view()),

    #URL For project exist
    path('mlaas/ingest/project_exist/',ProjectExistClass.as_view()),

    #URL For dataset exist
    path('mlaas/ingest/dataset_exist/',DatasetExistClass.as_view()),

    #URL For dataset name
    path('mlaas/ingest/datasetname_exist/',DatasetNameClass.as_view()),
    
    #URL for menu
    path('mlaas/menu/',MenuClass.as_view()),


]