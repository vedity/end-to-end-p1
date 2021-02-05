from django.urls import path,include
from .views import *

urlpatterns = [

    
    #URL for Dataset Statistics
    path('mlaas/preprocess/exploredata/get_data_statistics',DatasetExplorationClass.as_view()),

    #URL for Data Visualization
    # path('mlaas/preprocess/visualize/get_visualization',DataVisualizationClass.as_view())
  
]