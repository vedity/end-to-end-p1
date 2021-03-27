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

    #ValidateColumnName
    path('mlaas/preprocess/schema/column/name/exist/',ValidateColumnName.as_view()),

    #url for possible operation for cleanup
    path('mlaas/preprocess/cleanup/operation/',OperationListClass.as_view()),
    
    #url for possible operation for cleanup
    path('mlaas/preprocess/cleanup/master_operation/',MasterOperationListClass.as_view()),

    #url for get column name
    path('mlaas/preprocess/cleanup/get_col_name/',GetColumnListClass.as_view()),

    #url for save cleanup 
    path('mlaas/preprocess/cleanup/save/',CleanupSave.as_view()),
    
    path('mlaas/preprocess/cleanup/scaling/',ScalingSplitClass.as_view()),
    
    path('mlaas/preprocess/cleanup/scaling/type/',Scalingtype.as_view()),

    path('mlaas/preprocess/cleanup/holdout/',TrainValidHoldout.as_view()),

    path('mlaas/modeling/checksplit/',Check_Split.as_view()),
    
    path('mlaas/preprocess/cldag_status/',CheckCleanupDagStatus.as_view()),
]