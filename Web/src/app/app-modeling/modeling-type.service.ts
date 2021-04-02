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

  checkexperimentname(experiment_name,project_id): Observable<any> {
    // project_id=2;
     var params = new HttpParams().append("experiment_name", experiment_name).append("project_id", project_id);
     return this.httpClient.get(this.baseUrl + "modeling/checkexperimentname/", { headers: this.headers, params });
   }

  showrunningexperimentslist(project_id): Observable<any> {
   // project_id=2;
    var params = new HttpParams().append("project_id", project_id);
    return this.httpClient.get(this.baseUrl + "modeling/runningexperimentslist/", { headers: this.headers, params });
  }

  checkmodelstatus(project_id,experiment_name,dataset_id,user_name): Observable<any> {
   // project_id=2;
    var params = new HttpParams().append("project_id", project_id).append("experiment_name",experiment_name)
    .append("dataset_id",dataset_id)
    .append("user_name",user_name);
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
      append("experiment_desc", obj.experiment_desc)
      .append("model_id",obj.model_id)
      .append("model_name",obj.model_name);
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

  getActualVsPreidiction(experiment_id,model_type): Observable<any> {
    //experiment_id=2;
    var params = new HttpParams().append("experiment_id", experiment_id)
    .append("model_type", model_type);
    return this.httpClient.get(this.baseUrl + "modeling/actualvsprediction/", { headers: this.headers, params });
  }

  getAlgorithmList(dataset_id,project_id,model_type): Observable<any> {
    var params = new HttpParams().append("dataset_id", dataset_id).append("project_id", project_id).append("model_type", model_type);
    return this.httpClient.get(this.baseUrl + "modeling/selectalgorithm/", { headers: this.headers,params });
  }

  getHyperparamsList(model_id): Observable<any> {
    var params = new HttpParams().append("model_id", model_id);
    return this.httpClient.get(this.baseUrl + "modeling/hyperparameters/", { headers: this.headers, params });
  }

  compareExperimentgrid(exp_ids): Observable<any> {
    var params = new HttpParams().append("experiment_ids", exp_ids);
    return this.httpClient.get(this.baseUrl + "modeling/compareexperimentsgrid/", { headers: this.headers, params });
  }

  compareExperimentgraph(exp_ids): Observable<any> {
    var params = new HttpParams().append("experiment_ids", exp_ids);
    return this.httpClient.get(this.baseUrl + "modeling/compareexperimentsgraph/", { headers: this.headers, params });
  }
  
  checkmodelType(dataset_id,project_id){
    var params = new HttpParams()
    .append("dataset_id", dataset_id)
    .append("project_id", project_id);
    return this.httpClient.get(this.baseUrl + "modeling/modeltype/", { headers: this.headers, params });
  }

  checkrunningExperiment(project_id): Observable<any> {
    var params = new HttpParams().append("project_id", project_id);
    return this.httpClient.get(this.baseUrl + "modeling/checkrunningexperiments/", { headers: this.headers, params });
  }

  getproject(): Observable<any> {
    this.user = JSON.parse(localStorage.getItem("currentUser"));
    var params = new HttpParams().set("user_name", this.user.username);
    return this.httpClient.get(this.baseUrl + "ingest/project/create/", { headers: this.headers, params });
  }

  getCheckSplit(project_id){
    var params = new HttpParams().append("project_id", project_id)
    return this.httpClient.get(this.baseUrl + "modeling/checksplit/", { headers: this.headers,params });
  }
}