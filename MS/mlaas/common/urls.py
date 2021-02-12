from django.urls import path
from .views import *

urlpatterns = [
    #mlaas/common/user/login/
    #URL For User Login
    path('mlaas/ingest/common/user/login/',UserLoginClass.as_view()),

    #URL for menu
    path('mlaas/common/menu/',MenuClass.as_view()),

    #url for activity timeline
    path('mlaas/common/activity/',ActivityTimelineClass.as_view()),

]