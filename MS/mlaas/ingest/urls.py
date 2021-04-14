from django.urls import path
from .views import *

urlpatterns = [

    #URL For Create Project
    path('mlaas/ingest/project/create/',CreateProjectClass.as_view()),

    #URL For Create Dataset
    path('mlaas/ingest/dataset/create/',CreateDatasetClass.as_view()),

    #URL For Data Detail(CSV File)
    path('mlaas/ingest/dataset/detail/',DataDetailClass.as_view()),
    
    #URL For Project Detail
    path('mlaas/ingest/project/detail/',ProjectDetailClass.as_view()),

    #URL For delete Project Detail
    path('mlaas/ingest/project/delete/',DeleteProjectDetailClass.as_view()),

    #URL For delete dataset Detail
    path('mlaas/ingest/dataset/delete/',DeleteDatasetDetailClass.as_view()),

    #URL For delete data Detail
    path('mlaas/ingest/delete/data_detail/',DeleteDataDetailClass.as_view()),

    #URL For project exist
    path('mlaas/ingest/project/exist/',ProjectExistClass.as_view()),

    #URL For dataset exist
    path('mlaas/ingest/dataset/exist/',DatasetExistClass.as_view()),

    #URL For dataset name
    path('mlaas/ingest/dataset/list/',DatasetNameClass.as_view()),

    #URL For Data Detail Column List (CSV File)
    path('mlaas/ingest/dataset/columns/',DataDetailColumnListClass.as_view()),

]