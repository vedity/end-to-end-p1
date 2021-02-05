from django.urls import path,include
from .views import *

urlpatterns = [

    
    #URL for Dataset Statistics
    path('mlaas/preprocess/exploredata/get_data_statistics',DatasetExplorationClass.as_view()),

    #URL for Data Visualization
    path('mlaas/preprocess/visualize/get_visualization',DataVisualizationClass.as_view()),

    #URL For dataset Schema
    path('mlaas/ingest/dataset_schema/',SchemaClass.as_view()),

    #URL For dataset Schema Save option
    path('mlaas/ingest/dataset_schema/save/',SchemaSaveClass.as_view()),

    #URL For dataset Schema Save As option
    path('mlaas/ingest/dataset_schema/save_as/',SchemaSaveAsClass.as_view()),
  
]