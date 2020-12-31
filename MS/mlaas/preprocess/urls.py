from django.urls import path,include
from .views import *

urlpatterns = [

    path('mlaas/preprocess/test',TestingClass.as_view())
  
]