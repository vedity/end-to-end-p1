import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { DataTableDirective } from 'angular-datatables';
import { ToastrService } from 'ngx-toastr';
// import { setInterval } from 'timers';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-type',
  templateUrl: './modeling-type.component.html',
  styleUrls: ['./modeling-type.component.scss']
})
export class ModelingTypeComponent implements OnInit {
  @ViewChild(DataTableDirective, { static: false })
  datatableElement: DataTableDirective;
  dtOptions: DataTables.Settings = {};
  animation = "progress-dark";
  theme = {
      'border-radius': '5px',
      'height': '40px',
      'background-color': ' rgb(34 39 54)',
      'border': '1px solid #32394e',
      'animation-duration': '20s'
  };
  contentloaded = false;
  constructor(public router: Router,public apiservice:ModelingTypeApiService,public toaster:ToastrService,private modalService: NgbModal) { }
  public params: any;
  public datasetInfo:any;
  experiment_name:any;
  experiment_desc:any;
  public modelDescription:any;
  processclass:any="stop";
  processInterval:any;
  data: any={
    experiment_name:"",
    experiment_desc:""
  };
  ngOnInit(): void {
    this.dtOptions = {
      paging: false,
      ordering: false,
      scrollCollapse: true,
      info: false,
      searching: false,
      scrollY: "calc(100vh - 365px)",
    }
    this.params = history.state;
    if (this.params.dataset_id != undefined)
    {
      let user=localStorage.getItem("currentUser")
      this.params.user_id=JSON.parse(user).id;
      localStorage.setItem("modeling", JSON.stringify(this.params));
    }
    else {
      this.params = localStorage.getItem("params");
      this.params = JSON.parse(this.params);
    }
    this.getDatasetInfo();
    this.getModelDescription();
  }

  getDatasetInfo(){
    this.apiservice.getDatasetInfo(this.params.dataset_id,this.params.project_id,this.params.user_id).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));
    
  }

  getModelDescription(){
    this.apiservice.getModelDescription(this.params.dataset_id,this.params.project_id,this.params.user_id).subscribe(
      logs => this.descsuccessHandler(logs),
      error => this.errorHandler(error));
  }

  modeldata:any=[];
  descsuccessHandler(data){
    if (data.status_code == "200") {
      //this.modeldata=data.response;
      this.modeldata= [
        {
        "experiment_id" :1,
        "experiment_name": "experiment 1",
            "model_name": "Linear Regression With Sklearn",
        "dataset_name":"KC House",
            "modeling_type":"auto",
            "status": "running",
            "cv_score": 0.6984604686,
            "holdout_score": 0.6949536716,
            "start_time_and_date":"2021-02-17T10:47:07.538Z"
        },
    {
        "experiment_id" :2,
        "experiment_name": "experiment 2",
            "model_name": "Logistic Regression With Sklearn",
        "dataset_name":"House_prediction",
            "modeling_type": "manual",
            "status": "completed",
            "cv_score": 0.6984604686,
            "holdout_score": 0.6949536716,
            "start_time_and_date":"2021-02-17T10:47:07.538Z"
        },
    {
            "experiment_id" :3,
        "experiment_name": "experiment 3",
            "model_name": "SVM",
        "dataset_name":"KC House",
            "modeling_type":"auto",
            "status": "running",
            "cv_score": 0.6984604686,
            "holdout_score": 0.6949536716,
            "start_time_and_date":"2021-02-17T10:47:07.538Z"
        },
    {
            "experiment_id" :4,
        "experiment_name": "experiment 4",
            "model_name": "Random Forest",
        "dataset_name":"KC House",
            "modeling_type":"manual",
            "status": "error",
            "cv_score": 0.6984604686,
            "holdout_score": 0.6949536716,
            "start_time_and_date":"2021-02-17T10:47:07.538Z"
        },
       
    ]
      console.log(this.modeldata);
      this.contentloaded=true;
      // data.response.forEach(element => {
      //   this.modeldata.push(JSON.parse(element));
      // });
      // console.log(this.modeldata);
      
      // this.toaster.success(data.error_msg, 'Success');
    }
    else{
      this.errorHandler(data);
    }
  }

  startModel() {
    this.processclass="start";
    this.experiment_name=this.params.experiment_name;
    this.experiment_desc=this.params.experiment_desc;
    let obj = {
      user_id: this.params.user_id,
      dataset_id: this.params.dataset_id,
      project_id: this.params.project_id,
      model_mode: "auto",
      experiment_name: this.params.experiment_name,
      experiment_desc: this.params.experiment_desc
    }
    // this.apiservice.startModeling(obj).subscribe( 
    //   logs => this.startsuccessHandler(logs),
    // error => this.errorHandler(error));

  }


  stopModel(){
    this.processclass="stop";
    if (this.processInterval) {
      clearInterval(this.processInterval);
    }
  }

  startsuccessHandler(data){
    if (data.status_code == "200") {
      this.toaster.success(data.error_msg, 'Success');
      this.processInterval= setInterval(() => {
        console.log("called");
        this.getModelDescription(); 
        }, 5000);
    }
    else{
      this.errorHandler(data);
    }
  }

  datasetdata:any;
  successHandler(data) {
    if (data.status_code == "200") {
      this.datasetdata=data.response;
      // this.toaster.success(data.error_msg, 'Success');
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

  extraLarge (exlargeModal: any) 
  {
    this.modalService.open(exlargeModal, { size: 'xl',windowClass:'modal-holder', centered: true });
  };

   smallModal(modelingmodal: any) {
    this.modalService.open(modelingmodal, { size: 'md', windowClass: 'modal-holder', centered: true });
  }
}
