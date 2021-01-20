from django.urls import path
from .views import *

urlpatterns = [
    
    #URL For User Login
    path('mlaas/ingest/user/login',UserLoginClass.as_view()),

    #URL for menu
    path('mlaas/menu/',MenuClass.as_view()),

    #URL for Schema datatype list
    path('mlaas/dataset_schema/datatype/',ScheamDatatypeListClass.as_view()),

    #url for schema column attribute
    path('mlaas/dataset_schema/column_attribute_list/',ScheamColumnListClass.as_view()),
    
    #url for activity timeline
    path('mlaas/activity_timeline/',ActivityTimelineClass.as_view()),
]
