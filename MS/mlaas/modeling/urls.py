from django.urls import path
from .views import *

urlpatterns = [

    #URL For Create Project
    #path('mlaas/modeling/model_run/',ModelRunClass.as_view()),

    #URL For Create Dataset
    #path('mlaas/modeling/split_data/',SplitDataClass.as_view()),

    #URL For Data Detail(CSV File)git 
    path('mlaas/modeling/showdatasetinfo/',ShowDatasetInfoClass.as_view()),
    
    path('mlaas/modeling/startmodel/',StartModelClass.as_view()),

    path('mlaas/modeling/learning_curve/',LearningCurveClass.as_view()),
 
    path('mlaas/modeling/featureimportance/',FeatureImportanceClass.as_view()),
 
    path('mlaas/modeling/performancemetrics/',PerformanceMetricsClass.as_view()),
 
    path('mlaas/modeling/modelsummary/',ModelSummaryClass.as_view()),

    path('mlaas/modeling/actualvsprediction/',ActualVsPredictionClass.as_view()),

    path('mlaas/modeling/confusionmatrix/',ConfusionMatrixClass.as_view()),

    path('mlaas/modeling/selectalgorithm/', SelectAlgorithmClass.as_view()),

    path('mlaas/modeling/hyperparameters/', ShowHyperParametersClass.as_view()),

    path('mlaas/modeling/runningexperimentslist/', ShowRunningExperimentsListClass.as_view()),
    
    path('mlaas/modeling/showallexperimentslist/', ShowAllExperimentsListClass.as_view()),
    
    path('mlaas/modeling/checkmodelstatus/', CheckModelStatusClass.as_view()),

    path('mlaas/modeling/refreshmodeling/', RefreshModelingPageClass.as_view()),

    path('mlaas/modeling/confusionmatrix/', ConfusionMatrixClass.as_view()),

    path('mlaas/modeling/roccurve/', ROCCurveClass.as_view()),

    path('mlaas/modeling/compareexperimentsgrid/', CompareExperimentsGridClass.as_view()),

    path('mlaas/modeling/compareexperimentsgraph/', CompareExperimentsGraphClass.as_view()),

    path('mlaas/modeling/checkexperimentname/', CheckExperimentNameClass.as_view()),

    path('mlaas/modeling/checkrunningexperiments/', CheckRunningExperimentsClass.as_view()), 

    path('mlaas/modeling/modeltype/', ModelTypeClass.as_view()),     

    path('mlaas/getsplitdata/', GetSplitDataClass.as_view()),  

    path('mlaas/modeling/modelfailed/', ModelFailedClass.as_view()),
    
    path('mlaas/modeling/pdpcurve/', PDPCurveClass.as_view()),
]