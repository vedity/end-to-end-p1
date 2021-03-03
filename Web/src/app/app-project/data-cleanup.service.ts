import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class DataCleanupApiService 
{
  baseUrl = 'http://127.0.0.1:8000/mlaas/'
  headers = new HttpHeaders({
    'Content-type': 'application/json',
  });
  user: any;
  constructor(private httpClient: HttpClient) { }

  getOperation(): Observable<any> {
    return this.httpClient.get(this.baseUrl + "preprocess/cleanup/master_operation/", { headers: this.headers });
  } 
  
  getColumnList(schema_id): Observable<any> {
    var params = new HttpParams().append("schema_id", schema_id)
    return this.httpClient.get(this.baseUrl + "preprocess/cleanup/get_col_name/", { headers: this.headers, params });
  }

  getColumnviseOperations(obj): Observable<any> {
    return this.httpClient.post(this.baseUrl + "preprocess/cleanup/operation/",obj, { headers: this.headers });
  }
}