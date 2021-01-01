import { Injectable } from '@angular/core';
import {HttpClient,HttpHeaders, HttpParams } from '@angular/common/http';
import  { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

   baseUrl = 'http://127.0.0.1:8000/mlaas/ingest/'
   headers = new HttpHeaders ({
     'Content-type': 'application/json',
   });
  constructor( private httpClient : HttpClient) { }
  
  getproject():Observable<any>{
    var params=new HttpParams().set("user_name","admin");
    return this.httpClient.post(this.baseUrl+"create_project/",JSON.stringify({user_name:"admin"}),{headers:this.headers});
  }

  getDataset():Observable<any>{
    return this.httpClient.get(this.baseUrl+"create_dataset/",{headers:this.headers});
  }

  // deleteDataset(id: number):Observable<any>{
  //   return this.httpClient.delete(`${this.baseUrl}${id}/`,{headers:this.headers});
  // }

  getDataDetails():Observable<any>{
    return this.httpClient.get(this.baseUrl+"data_detail/",{headers:this.headers});
  }
}
