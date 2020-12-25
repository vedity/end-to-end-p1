from django.urls import path,include
from . import views



urlpatterns = [
    
    #URL For file upload
    path('motaadmin/fileupload/',views.FileUploadClass.as_view()),

    #URL For dataset_details
    path('motaadmin/dataset_details/',views.DatasetDetailClass.as_view()),

    #URL For dataslide_status
    path('motaadmin/dataslide_status/',views.DataSlideStatusClass.as_view()),

    #URL For totalsales
    path('motaadmin/totalsales/',views.TotalSalesClass.as_view()),

    #URL For yearlydetail
    path('motaadmin/yearlydetail/',views.YearlyDetailsClass.as_view()),

    #URL For timeline
    path('motaadmin/timeline/',views.TimelineClass.as_view()),
    
    #URL For delete_record
    path('motaadmin/delete_record/',views.DeleteReocordClass.as_view()),

    #URL For delete_rupdate_recordecord
    path('motaadmin/update_record/',views.UpldateReocordClass.as_view()),


    
    

]