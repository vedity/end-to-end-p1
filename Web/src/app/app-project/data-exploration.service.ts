import { Injectable } from '@angular/core';
import {HttpClient,HttpHeaders, HttpParams } from '@angular/common/http';
import  { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataExplorationApiService {

   baseUrl = 'http://127.0.0.1:8000/mlaas/'
   headers = new HttpHeaders ({
     'Content-type': 'application/json',
   });
   user:any;
   
  constructor( private httpClient : HttpClient) { 

  }
  
  getExplorationData(dataset_id):Observable<any>{
    var params=new HttpParams().append("dataset_id",dataset_id)
    return this.httpClient.get(this.baseUrl+"preprocess/exploredata/get_data_statistics",{headers:this.headers,params});
  }

 
 
}

