import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class ModelingTypeApiService {
  baseUrl = environment.baseUrl;
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
    // return this.httpClient.get(this.baseUrl + "modeling/finalmodeldescription/", { headers: this.headers, params });
    return this.httpClient.get(this.baseUrl + "modeling/showexperimentslist/", { headers: this.headers, params });
  }

  startModeling(obj):Observable<any>{
    var params = new HttpParams().append("model_mode", obj.model_mode);
    return this.httpClient.post(this.baseUrl + "modeling/startmodel/", { headers: this.headers ,params});
  }


  getLearningCurves(experiment_id): Observable<any> {
    experiment_id=2;
    var params = new HttpParams().append("experiment_id", experiment_id);
    return this.httpClient.get(this.baseUrl + "modeling/learning_curve/", { headers: this.headers, params });
  }

  getFeatureImportance(experiment_id): Observable<any> {
    experiment_id=2;
    var params = new HttpParams().append("experiment_id", experiment_id);
    return this.httpClient.get(this.baseUrl + "modeling/featureimportance/", { headers: this.headers, params });
  }

  getPerformanceMatrics(experiment_id): Observable<any> {
    experiment_id=2;
    var params = new HttpParams().append("experiment_id", experiment_id);
    return this.httpClient.get(this.baseUrl + "modeling/performancemetrics/", { headers: this.headers, params });
  }

  getModelSummary(experiment_id): Observable<any> {
    experiment_id=2;
    var params = new HttpParams().append("experiment_id", experiment_id);
    return this.httpClient.get(this.baseUrl + "modeling/modelsummary/", { headers: this.headers, params });
  }

  getActualVsPreidiction(experiment_id): Observable<any> {
    experiment_id=2;
    var params = new HttpParams().append("experiment_id", experiment_id);
    return this.httpClient.get(this.baseUrl + "modeling/actualvsprediction/", { headers: this.headers, params });
  }

  getAlgorithmList(): Observable<any> {
    return this.httpClient.get(this.baseUrl + "modeling/selectalgorithm/", { headers: this.headers });
  }

  getHyperparamsList(model_name): Observable<any> {
    var params = new HttpParams().append("model_name", model_name);
    return this.httpClient.get(this.baseUrl + "modeling/hyperparameters/", { headers: this.headers, params });
  }
}