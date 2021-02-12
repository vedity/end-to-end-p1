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

    

  


]