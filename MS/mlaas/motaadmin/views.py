from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
import pandas as pd
from database import *
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.motaadmin import *
from .utils import motaadmin
from database import *


class FileUploadClass(APIView):
     def get(self, request, format=None):
        try: 
            MotaAdminObject = MotaAdmin(database,user,password,host,port)
            Status=MotaAdminObject.load_data()
            return Response({"Status":Status}) 
        except Exception as e:
            return Response({"Exception":str(e)})  

class DatasetDetailClass(APIView):
    def get(self, request, format=None):
        try: 
            MotaAdminObject = MotaAdmin(database,user,password,host,port)
            dataset_df=MotaAdminObject.show_dataset_details()
            dataset_record=json.loads(dataset_df.to_json(orient='records',date_format='iso')) # convert datafreame into json
            return Response({"Status":dataset_record}) 
        except Exception as e:
            return Response({"Exception":str(e)}) 

class DataSlideStatusClass(APIView):
    def get(self, request, format=None):
        try: 
            MotaAdminObject = MotaAdmin(database,user,password,host,port)
            dataset_df=MotaAdminObject.show_data_slide_status()
            dataset_record=json.loads(dataset_df.to_json(orient='records')) # convert datafreame into json
            return Response({"Status":dataset_record}) 
        except Exception as e:
            return Response({"Exception":str(e)}) 

class  TotalSalesClass(APIView):
     def get(self, request, format=None):
        try: 
            MotaAdminObject = MotaAdmin(database,user,password,host,port)
            bedrooms_price_df,bathrooms_price_df=MotaAdminObject.total_sales()
            bedrooms_price_record=json.loads(bedrooms_price_df.to_json(orient='records')) # convert datafreame into json
            bathrooms_price_record=json.loads(bathrooms_price_df.to_json(orient='records')) #
            return Response({"bedrooms_price":bedrooms_price_record,"bathrooms_price":bathrooms_price_record}) 
        except Exception as e:
            return Response({"Exception":str(e)}) 


class YearlyDetailsClass(APIView):
    def get(self, request, format=None):
        try: 
            MotaAdminObject = MotaAdmin(database,user,password,host,port)
            dataset_df=MotaAdminObject.show_yearly_details()
            dataset_record=json.loads(dataset_df.to_json(orient='records')) # convert datafreame into json
            return Response({"Status":dataset_record}) 
        except Exception as e:
            return Response({"Exception":str(e)}) 

class TimelineClass(APIView):
    def get(self, request, format=None):
        try: 
            MotaAdminObject = MotaAdmin(database,user,password,host,port)
            dataset_df=MotaAdminObject.timeline()
            dataset_record=json.loads(dataset_df.to_json(orient='records',date_format='iso')) # convert datafreame into json
            return Response({"Status":dataset_record}) 
        except Exception as e:
            return Response({"Exception":str(e)}) 


class DeleteReocordClass(APIView):
    def get(self, request, format=None):
        try: 
            index=request.POST.get('index')
            MotaAdminObject = MotaAdmin(database,user,password,host,port)
            Status=MotaAdminObject.delete_records(index)
            # dataset_record=json.loads(dataset_df.to_json(orient='records',date_format='iso')) # convert datafreame into json
            return Response({"Status":Status}) 
        except Exception as e:
            return Response({"Exception":str(e)}) 


class UpldateReocordClass(APIView):
    def post(self, request, format=None):
        try: 
            index=request.POST.get('index')
            date=request.POST.get('date')
            price=request.POST.get('price')
            bedrooms=request.POST.get('bedrooms')
            bathrooms=request.POST.get('bathrooms')
            MotaAdminObject = MotaAdmin(database,user,password,host,port)
            status=MotaAdminObject.update_records(index,date,price,bedrooms,bathrooms)
            return Response({"Status":status}) 
        except Exception as e:
            return Response({"Exception":str(e)}) 


















                
