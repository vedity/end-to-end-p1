from django.urls import path
from .views import *

urlpatterns = [

    #URL For Create Project
    #path('mlaas/modeling/model_run/',ModelRunClass.as_view()),

    #URL For Create Dataset
    #path('mlaas/modeling/split_data/',SplitDataClass.as_view()),

    #URL For Data Detail(CSV File)
    path('mlaas/modeling/showdatasetinfo/',ShowDatasetInfoClass.as_view()),
    
    path('mlaas/modeling/startmodel/',StartModelClass.as_view()),

    path('mlaas/modeling/learning_curve/',LearningCurveClass.as_view()),
 
    path('mlaas/modeling/featureimportance/',FeatureImportanceClass.as_view()),
 
    path('mlaas/modeling/performancemetrics/',PerformanceMetricsClass.as_view()),
 
    path('mlaas/modeling/modelsummary/',ModelSummaryClass.as_view()),

    path('mlaas/modeling/actualvsprediction/',ActualVsPredictionClass.as_view()),

    path('mlaas/modeling/confusion_matrix/',ConfusionMatrixClass.as_view()),

    path('mlaas/modeling/selectalgorithm/', SelectAlgorithmClass.as_view()),

    path('mlaas/modeling/hyperparameters/', HyperParametersClass.as_view()),

    path('mlaas/modeling/showexperimentslist/', ShowExperimentsListClass.as_view()),
    
    path('mlaas/modeling/showallexperimentslist/', ShowAllExperimentsListClass.as_view()),
    
    path('mlaas/modeling/checkmodelstatus/', CheckModelStatusClass.as_view())
    
      
]