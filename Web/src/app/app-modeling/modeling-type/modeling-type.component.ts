import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { DataTableDirective } from 'angular-datatables';
import { ToastrService } from 'ngx-toastr';
//  import { manualmodeling } from './modeling.model';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-type',
  templateUrl: './modeling-type.component.html',
  styleUrls: ['./modeling-type.component.scss']
})
export class ModelingTypeComponent implements OnInit {
  // mySwitch: boolean = false;
  // public data:manualmodeling;
  splitmethodselection="crossvalidation";
  hyperparams='sklearn';
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
  iscompare = false;
  constructor(public router: Router, public apiservice: ModelingTypeApiService, public toaster: ToastrService, private modalService: NgbModal) { }
  public params: any;
  public datasetInfo: any;
  experiment_name: any;
  experiment_desc: any;
  public modelDescription: any;
  processclass: any = "stop";
  processInterval: any;
 
  ngOnInit(): void {
   let projectdatamodel;
    this.dtOptions = {
      paging: false,
      ordering: false,
      scrollCollapse: true,
      info: false,
      searching: false,
      scrollY: "calc(100vh - 365px)",
    }
    this.params = history.state;
    if (this.params.dataset_id != undefined) {
      let user = localStorage.getItem("currentUser")
      this.params.user_id = JSON.parse(user).id;
      localStorage.setItem("modeling", JSON.stringify(this.params));
    }
    else {
      if(this.params.selectproject==false){
        $(".openmodal").trigger('click');
      }
    //this.modalService.open(projectdatamodel, { size: 'lg', windowClass: 'modal-holder', centered: true });
      this.params = localStorage.getItem("params");
      this.params = JSON.parse(this.params);
    }
    this.getDatasetInfo();
    this.getModelDescription();
    this.getAlgorithmList();
  }


  compareIds = [];
  setCopmareIds(val, id) {
    // console.log(val, id);
    if (val == true) {
      this.compareIds.push(id);
    }
    else {
      // console.log(this.compareIds.indexOf(id));
      var index = this.compareIds.indexOf(id);
      if (index != -1) {
        this.compareIds.splice(index, 1);
      }
    }
    // console.log(this.compareIds);
    if (this.compareIds.length > 1) {
      this.iscompare = true;
    }
    else {
      this.iscompare = false;
    }
  }

  getDatasetInfo() {
    this.apiservice.getDatasetInfo(this.params.dataset_id, this.params.project_id, this.params.user_id).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));

  } 
  
  getAlgorithmList() {
    this.apiservice.getAlgorithmList().subscribe(
      logs => this.successAlgorithmListHandler(logs),
      error => this.errorHandler(error));
  }

  algorithmlist: any;
  successAlgorithmListHandler(data) {
    if (data.status_code == "200") {
      this.algorithmlist = data.response.model_name;
    }
    else {
      this.errorHandler(data);
    }
  }


  getHyperParams(val){
    if(val!=""){
      this.apiservice.getHyperparamsList(val).subscribe(
        logs => this.successParamsListHandler(logs),
        error => this.errorHandler(error));
    }
    else
    this.paramsList=null
  }

  paramsList: any;
  successParamsListHandler(data) {
    if (data.status_code == "200") {
      this.paramsList = data.response.model_parameter;
      console.log(this.paramsList);
      
    }
    else {
      this.errorHandler(data);
    }
  }
  getModelDescription() {
    this.apiservice.getModelDescription(this.params.dataset_id, this.params.project_id, this.params.user_id).subscribe(
      logs => this.descsuccessHandler(logs),
      error => this.errorHandler(error));
  }

  modeldata: any = [];
  descsuccessHandler(data) {
    if (data.status_code == "200") {
      this.modeldata = data.response;
      this.contentloaded = true;
    }
    else {
      this.errorHandler(data);
    }
  }

  startModel() {
    this.processclass = "start";
    this.experiment_name = this.params.experiment_name;
    this.experiment_desc = this.params.experiment_desc;
    let obj = {
      user_id: this.params.user_id,
      dataset_id: this.params.dataset_id,
      project_id: this.params.project_id,
      model_mode: "auto",
      experiment_name: this.params.experiment_name,
      experiment_desc: this.params.experiment_desc
    }
  }

  stopModel() {
    this.processclass = "stop";
    if (this.processInterval) {
      clearInterval(this.processInterval);
    }
  }

  startsuccessHandler(data) {
    if (data.status_code == "200") {
      this.toaster.success(data.error_msg, 'Success');
      this.processInterval = setInterval(() => {
        this.getModelDescription();
      }, 5000);
    }
    else {
      this.errorHandler(data);
    }
  }

  datasetdata: any;
  successHandler(data) {
    if (data.status_code == "200") {
      this.datasetdata = data.response;
      // this.toaster.success(data.error_msg, 'Success');
    }
    else {
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

  modeltitle: any;
  extraLarge(exlargeModal: any, name) {
    this.modeltitle = name;
    this.modalService.open(exlargeModal, { size: 'xl', windowClass: 'modal-holder', centered: true });
  };

  smallModal(modelingmodal: any) {
    this.modalService.open(modelingmodal, { size: 'md', windowClass: 'modal-holder', centered: true });
  }

  contentid = 0;
  LargeModal(largeModal: any, val) {
    if (val) {
      this.contentid = 1;
      this.modalService.open(largeModal, { size: 'lg', windowClass: 'modal-holder', centered: true });
    }
  };

  ProjectData(projectModal:any){
    this.modalService.open(projectModal, { size: 'lg', windowClass: 'modal-holder', centered: true });
  }

  showContent(id) {
    this.contentid = id;
  };
}
