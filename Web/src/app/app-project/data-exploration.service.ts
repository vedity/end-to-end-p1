import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class DataExplorationApiService {
  baseUrl = environment.baseUrl;
  headers = new HttpHeaders({
    'Content-type': 'application/json',
  });
  user: any;
  constructor(private httpClient: HttpClient) { }

  getExplorationData(dataset_id,schema_id): Observable<any> {
    var params = new HttpParams().append("dataset_id", dataset_id).append("schema_id", schema_id)
    return this.httpClient.get(this.baseUrl + "preprocess/exploredata/get_data_statistics", { headers: this.headers, params });
  }
}