import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class SchemaMappingApiService {
  baseUrl = environment.baseUrl;
  headers = new HttpHeaders({
    'Content-type': 'application/json',
  });
  user: any;
  constructor(private httpClient: HttpClient) { }

  getDataDetails(obj, dataset_id, schema_id): Observable<any> {
    var params = new HttpParams().append("dataset_id", dataset_id).append("schema_id", schema_id)
    return this.httpClient.post(this.baseUrl + "ingest/dataset/detail/", obj, { headers: this.headers, params });
  }

  getColumnList(dataset_id, schema_id): Observable<any> {
    var params = new HttpParams().append("dataset_id", dataset_id)
      .append("schema_id", schema_id)
    return this.httpClient.get(this.baseUrl + "ingest/dataset/columns/", { headers: this.headers, params });
  }

  getproject(): Observable<any> {
    this.user = JSON.parse(localStorage.getItem("currentUser"));
    var params = new HttpParams().set("user_name", this.user.username);
    return this.httpClient.get(this.baseUrl + "ingest/project/create/", { headers: this.headers, params });
  }

  getColumnAttributes(): Observable<any> {
    return this.httpClient.get(this.baseUrl + "preprocess/schema/attribute/list/", { headers: this.headers });
  }

  getDatatypeList(): Observable<any> {
    return this.httpClient.get(this.baseUrl + "dataset_schema/datatype_list/", { headers: this.headers });
  }

  getDatasetSchema(project_id, dataset_id, schema_id): Observable<any> {
    var params = new HttpParams().append("project_id", project_id).append("dataset_id", dataset_id).append("schema_id", schema_id);
    //return this.httpClient.get(this.baseUrl + "ingest/preprocess/schema/detail/", { headers: this.headers, params });
    return this.httpClient.get(this.baseUrl + "preprocess/schema/detail/", { headers: this.headers, params });

  }

  saveDatasetSchema(dataset_id, project_id, schema_id, obj): Observable<any> {
    this.user = JSON.parse(localStorage.getItem("currentUser"));
    var params = new HttpParams()
      .append("user_name", this.user.username)
      .append("project_id", project_id)
      .append("dataset_id", dataset_id)
      .append("schema_id", schema_id)
    return this.httpClient.post(this.baseUrl + "ingest/preprocess/schema/save/", obj, { headers: this.headers, params });
  }

  checkuniqueColumnName(column_name, schema_id) {
    var params = new HttpParams()
      .append("column_name", column_name)
      .append("schema_id", schema_id)
    return this.httpClient.get(this.baseUrl + "preprocess/schema/column/name/exist/", { headers: this.headers, params });
  }

  saveasDatasetSchema(project_id, dataset_name, dataset_desc, visibility, method_name, obj): Observable<any> {
    var params = new HttpParams()
      .append("project_id", project_id)
      .append("dataset_name", dataset_name.toString())
      .append("dataset_desc", dataset_desc.toString())
      .append("visibility", visibility)
      .append("method_name", method_name.toString())
    // .append("dataset_id", dataset_id)
    return this.httpClient.post(this.baseUrl + "ingest/dataset_schema/save_as/", obj, { headers: this.headers, params });
  }

  getfeatureSelection(dataset_id,schema_id,target_col) {
    var params = new HttpParams()
      .append("dataset_id", dataset_id)
      .append("schema_id", schema_id)
      .append("target_col", target_col)
    return this.httpClient.get(this.baseUrl + "preprocess/feature_selection_data/", { headers: this.headers,params });
  }

  getAllDagsStatus(project_id) {
    var params = new HttpParams()
      .append("project_id", project_id)
    return this.httpClient.get(this.baseUrl + "preprocess/dags/status/", { headers: this.headers,params });
  }

  startFeatureSelection(dataset_id,schema_id,target_col) {
    var params = new HttpParams()
      .append("dataset_id", dataset_id)
      .append("schema_id", schema_id)
      .append("target_col", target_col)
    return this.httpClient.get(this.baseUrl + "preprocess/fs_dag/", { headers: this.headers,params });
  }  
}
