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

  getModelDescription(project_id): Observable<any> {
   // project_id=2;
    var params = new HttpParams().append("project_id", project_id);
    return this.httpClient.get(this.baseUrl + "modeling/showexperimentslist/", { headers: this.headers, params });
  }
  
  showallexperimentslist(project_id): Observable<any> {
   // project_id=2;
    var params = new HttpParams().append("project_id", project_id);
    return this.httpClient.get(this.baseUrl + "modeling/showallexperimentslist/", { headers: this.headers, params });
  }

  checkexperimentname(experiment_name): Observable<any> {
    // project_id=2;
     var params = new HttpParams().append("experiment_name", experiment_name);
     return this.httpClient.get(this.baseUrl + "modeling/checkexperimentname/", { headers: this.headers, params });
   }
    

  showrunningexperimentslist(project_id): Observable<any> {
   // project_id=2;
    var params = new HttpParams().append("project_id", project_id);
    return this.httpClient.get(this.baseUrl + "modeling/runningexperimentslist/", { headers: this.headers, params });
  }

  checkmodelstatus(project_id,experiment_name): Observable<any> {
   // project_id=2;
    var params = new HttpParams().append("project_id", project_id).append("experiment_name",experiment_name);
    return this.httpClient.get(this.baseUrl + "modeling/checkmodelstatus/", { headers: this.headers, params });
  }

  startModeling(obj):Observable<any>{
    var params = new HttpParams().
    append("user_name", obj.user_name).
    append("dataset_id", obj.dataset_id).
    append("project_id", obj.project_id).
    append("model_mode", obj.model_mode).
    append("model_type", obj.model_type).
    append("experiment_name", obj.experiment_name).
    append("experiment_desc", obj.experiment_desc);
    return this.httpClient.post(this.baseUrl + "modeling/startmodel/",obj, { headers: this.headers ,params});
  }


  getLearningCurves(experiment_id): Observable<any> {
   // experiment_id=2;
    var params = new HttpParams().append("experiment_id", experiment_id);
    return this.httpClient.get(this.baseUrl + "modeling/learning_curve/", { headers: this.headers, params });
  }

  getConfusionMatrix(experiment_id): Observable<any> {
   // experiment_id=2;
    var params = new HttpParams().append("experiment_id", experiment_id);
    return this.httpClient.get(this.baseUrl + "modeling/confusionmatrix/", { headers: this.headers, params });
  }

  getFeatureImportance(experiment_id): Observable<any> {
   // experiment_id=2;
    var params = new HttpParams().append("experiment_id", experiment_id);
    return this.httpClient.get(this.baseUrl + "modeling/featureimportance/", { headers: this.headers, params });
  }

  getPerformanceMatrics(experiment_id): Observable<any> {
    //experiment_id=2;
    var params = new HttpParams().append("experiment_id", experiment_id);
    return this.httpClient.get(this.baseUrl + "modeling/performancemetrics/", { headers: this.headers, params });
  }

  getModelSummary(experiment_id): Observable<any> {
   // experiment_id=2;
    var params = new HttpParams().append("experiment_id", experiment_id);
    return this.httpClient.get(this.baseUrl + "modeling/modelsummary/", { headers: this.headers, params });
  }

  getActualVsPreidiction(experiment_id): Observable<any> {
    //experiment_id=2;
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