import { Component, HostListener, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { DataTableDirective } from 'angular-datatables';
import { ToastrService } from 'ngx-toastr';
//  import { manualmodeling } from './modeling.model';
import { ModelingTypeApiService } from '../modeling-type.service';
import {CdkDragDrop, moveItemInArray} from '@angular/cdk/drag-drop';
@Component({
  selector: 'app-modeling-type',
  templateUrl: './modeling-type.component.html',
  styleUrls: ['./modeling-type.component.scss']
})
export class ModelingTypeComponent implements OnInit {
  // mySwitch: boolean = false;
  // public data:manualmodeling;
  timePeriods = [
    'Experiment 1','Experiment 2','Experiment 3','Experiment 4'
  ];

 
  isDisplayRunning=true;
  model_type="Regression";
  currentuser:any;
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
  lineColumAreaChart:any;

  @HostListener('window:resize', ['$event'])
	onResize(event) {
    if (this.datatableElement) {
      this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
        dtInstance.columns.adjust();
      })
    }
	}
  
  ngOnInit(): void {
   let projectdatamodel;
    this.dtOptions = {
      paging: false,
      ordering: false,
      scrollCollapse: true,
      info: false,
      searching: false,
      scrollY: "calc(100vh - 545px)",
    }
    this.params = history.state;

    if (this.params.dataset_id != undefined) {
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

    this.lineColumAreaChart = {
      chart: {
          height: 200,
          type: 'line',
          stacked: false,
          toolbar: {
              show: false
          }
      },
      stroke: {
          width: [2, 2, 4],
      },
      colors: ['#f46a6a', '#34c38f'],
      series: [{
          name: 'Experiment 1',
          data: [23, 11, 50, 70, 13, 56, 37, 78, 44, 22, 30]
      }, {
          name: 'Experiment 2',
          data: [23, 10, 22, 30, 13, 20, 31, 21, 40, 20, 32]
      }],
      fill: {
          opacity: [0.85, 1],
          gradient: {
              inverseColors: false,
              shade: 'light',
              type: 'vertical',
              opacityFrom: 0.85,
              opacityTo: 0.55,
              stops: [0, 100, 100, 100]
          }
      },
      // tslint:disable-next-line: max-line-length
      labels: ['01/01/2003', '02/01/2003', '03/01/2003', '04/01/2003', '05/01/2003', '06/01/2003', '07/01/2003', '08/01/2003', '09/01/2003', '10/01/2003', '11/01/2003'],
      markers: {
          size: [0,2]
      },
      legend: {
          offsetY: 5,
      },
      xaxis: {
          type: 'datetime',
      },
      yaxis: {
          title: {
              text: 'Points',
          },
      },
      tooltip: {
          shared: true,
          intersect: false,
          y: {
              formatter(y) {
                  if (typeof y !== 'undefined') {
                      return y.toFixed(0) + ' points';
                  }
                  return y;
              }
          }
      },
      grid: {
          borderColor: '#f1f1f1'
      }
    };
    this.currentuser = localStorage.getItem("currentUser")
    this.params.user_id = JSON.parse(this.currentuser).id;
    console.log(this.currentuser);
    this.getDatasetInfo();
    this.getRunningExperimentList();
    this.getAllExperimentList();
    this.getAlgorithmList();
  }

  drop(event: CdkDragDrop<string[]>) {
    moveItemInArray(this.timePeriods, event.previousIndex, event.currentIndex);
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
      this.algorithmlist = data.response;
      console.log(this.algorithmlist);
      
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
      this.paramsList = data.response.model_parameters;
      console.log(this.paramsList);
      
    }
    else {
      this.errorHandler(data);
    }
  }
  getRunningExperimentList() {
    this.apiservice.showrunningexperimentslist(this.params.project_id).subscribe(
      logs => this.runningexpListsuccessHandler(logs),
      error => this.errorHandler(error));
  }

runningExpList: any = [];
  runningexpListsuccessHandler(data) {
    if (data.status_code == "200") {
      this.runningExpList = data.response;
      this.contentloaded = true;
    }
    else {
      this.errorHandler(data);
    }
  }

  getAllExperimentList() {
    this.apiservice.showallexperimentslist(this.params.project_id).subscribe(
      logs => this.allexpListsuccessHandler(logs),
      error => this.errorHandler(error));
  }

  allExpList: any = [];
  allexpListsuccessHandler(data) {
    if (data.status_code == "200") {
      this.allExpList=[];
      this.allExpList = data.response;
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
    console.log(this.currentuser);
    let currentuser = localStorage.getItem("currentUser")
    let username = JSON.parse(currentuser).username;
    let obj = {
      user_name: username,
      dataset_id:this.params.dataset_id,
      project_id: this.params.project_id,
      model_mode: "Auto",
      model_type:this.model_type,
      experiment_name: this.params.experiment_name,
      experiment_desc: this.params.experiment_desc
    }

    console.log(obj);
    
    this.apiservice.startModeling(obj).subscribe(
      logs=>this.startsuccessHandler(logs),
      error=>this.errorHandler(error)
    )

  }

  changeDisplay(){
    this.isDisplayRunning=!this.isDisplayRunning
  }

  stopModel() {
    this.processclass = "stop";
    if (this.processInterval) {
      clearInterval(this.processInterval);
    }
  }

  checkstatus(){
    this.apiservice.checkmodelstatus(this.params.project_id,this.experiment_name).subscribe(
      logs=>this.statusSuccessHandler(logs),
      error=>this.errorHandler(error)
    )
  }

  statusSuccessHandler(data){
    if (data.status_code == "200") {
      if(data.response=="failed" || data.response=="success")
      this.stopModel();
    }
    else{
      this.errorHandler(data);
    }
  }

  startsuccessHandler(data) {
    if (data.status_code == "200") {
      this.toaster.success(data.error_msg, 'Success');
      this.processInterval = setInterval(() => {
        this.getRunningExperimentList();
        this.getAllExperimentList();
        this.checkstatus();
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
  current_experiment_id:any;
  current_model_type:any;
  extraLarge(exlargeModal: any, obj) {
    this.modeltitle = obj.experiment_name;
    this.current_experiment_id=obj.experiment_id;
    this.current_model_type=obj.model_type;
    this.modalService.open(exlargeModal, { size: 'xl', windowClass: 'modal-holder', centered: true });
  };

  checkexperimentname(event)
{
  var val=event.target.value;
  if(val!=""){
    this.apiservice.checkexperimentname(val).subscribe(
      logs=>this.checksuccessHandler(logs,event.target),
      error=>this.errorHandler(error)
    )
  }
  else
  this.checkuniuqename = false;
}

checkuniuqename=true;
checksuccessHandler(data,target){
  if (data.status_code == '200') {
    this.checkuniuqename = true;
    target.className = target.className.replace("ng-invalid", " ");
    target.className = target.className + " ng-valid";
  }
  else {
    this.checkuniuqename = false;
    target.className = target.className.replace("ng-valid", " ");
    target.className = target.className + " ng-invalid";
  }
}

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

  compareLarge (compareModal: any) 
  {
    this.modalService.open(compareModal, { size: 'xl',windowClass:'modal-holder', centered: true });
  };

  ProjectData(projectModal:any){
    this.modalService.open(projectModal, { size: 'lg', windowClass: 'modal-holder', centered: true });
  }

  showContent(id) {
    this.contentid = id;
  };
}
