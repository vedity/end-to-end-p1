import { Injectable } from '@angular/core';
import {HttpClient,HttpHeaders, HttpParams } from '@angular/common/http';
import  { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProjectApiService {

   baseUrl = 'http://127.0.0.1:8000/mlaas/ingest/'
   headers = new HttpHeaders ({
     'Content-type': 'application/json',
   });
   user:any;
   
  constructor( private httpClient : HttpClient) { 

  }
  
  getproject():Observable<any>{
   this.user=JSON.parse(localStorage.getItem("currentUser"));
    
    var params=new HttpParams().set("user_name",this.user.username);
    return this.httpClient.get(this.baseUrl+"create_project/",{headers:this.headers,params});
  }

  saveproject(obj:FormData):Observable<any>{
    console.log(obj);
    return this.httpClient.post<any>(this.baseUrl+"create_project/",obj);
  }

  deleteproject(id):Observable<any>{
      this.user=JSON.parse(localStorage.getItem("currentUser"));
    var params=new HttpParams().append("user_name",this.user.username).append('project_id',id);
   
    return this.httpClient.delete<any>(this.baseUrl+"delete/project_detail/",{headers:this.headers,params});
  }

  getDataset():Observable<any>{
      this.user=JSON.parse(localStorage.getItem("currentUser"));
    var params=new HttpParams().set("user_name",this.user.username);
    return this.httpClient.get(this.baseUrl+"create_dataset/",{headers:this.headers,params});
  }
  // mlaas/menu/
  savedataset(obj:FormData):Observable<any>{
    console.log(obj);
    return this.httpClient.post<any>(this.baseUrl+"create_dataset/",obj);
  }

  deletedataset(id):Observable<any>{
      this.user=JSON.parse(localStorage.getItem("currentUser"));
    var params=new HttpParams().append("user_name",this.user.username).append('dataset_id',id);
    return this.httpClient.delete(this.baseUrl+"delete/dataset_detail/",{headers:this.headers,params});
  }

  getDataDetails(obj,dataset_id):Observable<any>{
    var params=new HttpParams().append("dataset_id",dataset_id)
    //.append("table_name",obj.table_name).append("dataset_visibility",obj.dataset_visibility)
    return this.httpClient.post(this.baseUrl+"data_detail/",obj,{headers:this.headers,params});
  }

  getDataDetailslist(obj):Observable<any>{
    var params=new HttpParams().append("dataset_id",obj.dataset_id)
    //.append("table_name",obj.table_name).append("dataset_visibility",obj.dataset_visibility)
    return this.httpClient.get(this.baseUrl+"data_detail/",{headers:this.headers,params});
  }

  getColumnList(dataset_id):Observable<any>{
    var params=new HttpParams().append("dataset_id",dataset_id)
    //.append("table_name",obj.table_name).append("dataset_visibility",obj.dataset_visibility)
    return this.httpClient.get(this.baseUrl+"data_detail/column_list/",{headers:this.headers,params});
  }
  
  checkUniqueProjectName(obj):Observable<any>{
      this.user=JSON.parse(localStorage.getItem("currentUser"));
    var params=new HttpParams().append("user_name",this.user.username).append("project_name",obj)
    //.append("table_name",obj.table_name).append("dataset_visibility",obj.dataset_visibility)
    return this.httpClient.get(this.baseUrl+"project_exist/",{headers:this.headers,params});
  }

  checkUniqueDatasetName(obj):Observable<any>{
      this.user=JSON.parse(localStorage.getItem("currentUser"));
    var params=new HttpParams().append("user_name",this.user.username).append("dataset_name",obj)
    //.append("table_name",obj.table_name).append("dataset_visibility",obj.dataset_visibility)
    return this.httpClient.get(this.baseUrl+"dataset_exist/",{headers:this.headers,params});
  }
}

