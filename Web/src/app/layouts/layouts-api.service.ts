import { Injectable } from '@angular/core';
import {HttpClient,HttpHeaders, HttpParams } from '@angular/common/http';
import  { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LayoutApiService {

   baseUrl = 'http://127.0.0.1:8000/mlaas/'
   headers = new HttpHeaders ({
     'Content-type': 'application/json',
   });
  constructor( private httpClient : HttpClient) { }
  
  getMenu():Observable<any>{
    return this.httpClient.get(this.baseUrl+"common/menu/",{headers:this.headers});
  }


  getActivityTimeline(): Observable<any> {
    let user = JSON.parse(localStorage.getItem("currentUser"));
    var params = new HttpParams().set("user_name", user.username);
    return this.httpClient.get(this.baseUrl + "common/activity/", { headers: this.headers, params });
  }

  
}
