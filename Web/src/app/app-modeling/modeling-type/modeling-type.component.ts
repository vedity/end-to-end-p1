import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-type',
  templateUrl: './modeling-type.component.html',
  styleUrls: ['./modeling-type.component.scss']
})
export class ModelingTypeComponent implements OnInit {

  constructor(public router: Router,public apiservice:ModelingTypeApiService,public toaster:ToastrService) { }
  public params: any;
  public datasetInfo:any;
  public modelDescription:any;
  
  ngOnInit(): void {
    var data = localStorage.getItem("Modeling")
    if (data) {
      this.params = JSON.parse(data);
    }
  }

  getDatasetInfo(){
    this.apiservice.getDatasetInfo(this.params.dataset_id,this.params.project_id,this.params.user_id).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));
    
  }

  getModelDescription(){
    this.apiservice.getModelDescription(this.params.dataset_id,this.params.project_id,this.params.user_id).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));
    
  }

  startModel() {
    let obj = {
      user_id: this.params.user_id,
      dataset_id: this.params.dataset_id,
      project_id: this.params.project_id,
      model_mode: "auto",
      experiment_name: this.params.experiment_name,
      experiment_desc: this.params.experiment_desc
    }
    this.apiservice.startModeling(obj).subscribe( 
      logs => this.successHandler(logs),
    error => this.errorHandler(error));

  }

  successHandler(data) {
    if (data.status_code == "200") {
      this.toaster.success(data.error_msg, 'Success');
    }
    else{
      this.errorHandler(data);
    }
  }

  errorHandler(error) {
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }
}
