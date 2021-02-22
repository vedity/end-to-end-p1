from django.urls import path,include
from .views import *

urlpatterns = [

    
    #URL for Dataset Statistics
    path('mlaas/preprocess/exploredata/get_data_statistics',DatasetExplorationClass.as_view()),

    # #URL for Data Visualization
    # path('mlaas/preprocess/visualize/get_visualization',DataVisualizationClass.as_view()),

    #URL For dataset Schema
    path('mlaas/preprocess/schema/detail/',SchemaClass.as_view()),

    #URL For Save functionality in schema
    path('mlaas/ingest/preprocess/schema/save/',SchemaSaveClass.as_view()),

    #url for schema column attribute
    path('mlaas/preprocess/schema/attribute/list/',ScheamColumnListClass.as_view()),

    #url for possible operation for cleanup
    path('mlaas/preprocess/cleanup/operation/',OperationListClass.as_view()),
    
    #url for possible operation for cleanup
    path('mlaas/preprocess/cleanup/master_operation/',MasterOperationListClass.as_view()),
]