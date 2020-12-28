from django.urls import path,include
from . import views
from ingest.views import *

urlpatterns = [
  
    #URL For Create Project
    # path('mlaas/ingest/create_project/',views.create_project,name='create_project'),
    path('mlaas/ingest/create_project/',CreateProjectClass.as_view()),

    #URL For Create Dataset
    # path('mlaas/ingest/create_dataset/',views.create_dataset,name='create_dataset'),
    path('mlaas/ingest/create_dataset/',CreateDatasetClass.as_view()),

    #URL For Data Detail(CSV File)
    # path('mlaas/ingest/data_detail/',views.data_details,name='data_details'),
    path('mlaas/ingest/data_detail/',DataDetailClass.as_view()),


    #URL For Project Detail
    # path('mlaas/ingest/project_detail/',views.project_details,name='project_details'),
    path('mlaas/ingest/project_detail/',ProjectDetailClass.as_view()),

    #URL For delete Project Detail
    path('mlaas/ingest/delete/project_detail/',DeleteProjectDetailClass.as_view()),

    #URL For delete dataset Detail
    path('mlaas/ingest/delete/dataset_detail/',DeleteDatasetDetailClass.as_view()),

    #URL For delete data Detail
    path('mlaas/ingest/delete/data_detail/',DeleteDataDetailClass.as_view()),

    path('mlaas/ingest/dataset_schema/', DatasetSchemaClass.as_view())
  
]