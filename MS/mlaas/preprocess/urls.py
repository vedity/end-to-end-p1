from django.urls import path,include
from .views import *

urlpatterns = [

    
    #URL for Dataset Statistics
    path('mlaas/preprocess/exploredata/get_data_statistics',DatasetExplorationClass.as_view())
  
]