from django.urls import path
from .views import *

urlpatterns = [
    
    #URL For User Login
    path('mlaas/ingest/user/login',UserLoginClass.as_view()),

    #URL for menu
    path('mlaas/menu/',MenuClass.as_view()),

    #URL for menu
    path('mlaas/dataset_schema/datatype_list/',ScheamDatatypeListClass.as_view()),

    path('mlaas/dataset_schema/column_attribute_list/',ScheamColumnListClass.as_view()),
]
