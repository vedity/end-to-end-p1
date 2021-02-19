import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ModelingTypeApiService {
  baseUrl = 'http://127.0.0.1:8000/mlaas/'
  headers = new HttpHeaders({
    'Content-type': 'application/json',
  });
  user: any;
  constructor(private httpClient: HttpClient) { }

  getDatasetInfo(dataset_id,project_id,user_id): Observable<any> {
    var params = new HttpParams().append("dataset_id", dataset_id).append("project_id", project_id).append("user_id",user_id);
    return this.httpClient.get(this.baseUrl + "modeling/showdatasetinfo/", { headers: this.headers, params });
  }

  getModelDescription(dataset_id,project_id,user_id): Observable<any> {
    project_id=2;
    var params = new HttpParams().append("project_id", project_id);
    //.append("dataset_id", dataset_id).append("project_id", project_id).append("user_id",user_id);
    return this.httpClient.get(this.baseUrl + "modeling/finalmodeldescription/", { headers: this.headers, params });
  }

  startModeling(obj):Observable<any>{
    var params = new HttpParams().append("model_mode", obj.model_mode);

    return this.httpClient.post(this.baseUrl + "modeling/startmodel/",obj, { headers: this.headers ,params});
  }
}