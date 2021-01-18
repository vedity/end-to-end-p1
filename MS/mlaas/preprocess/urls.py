from django.urls import path,include
from .views import *

urlpatterns = [

    
    #URL for Dataset Statistics
    path('mlaas/preprocess/exploredata/get_data_statistics',DatasetStatisticsClass.as_view()),

    #URL for returning Column for boxplot
    #path('mlaas/preprocess/exploredata/get_column',DataVisualizationColumnClass.as_view())
  
]