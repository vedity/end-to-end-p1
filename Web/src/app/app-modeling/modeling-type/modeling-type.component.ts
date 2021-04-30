import { Component, HostListener, OnInit, ViewChild } from '@angular/core';
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
  isDisplayRunning = true;
  model_type = "";
  currentuser: any;
  splitmethodselection = "crossvalidation";
  hyperparams = 'sklearn';
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
  lineColumAreaChart: any;

  @HostListener('window:resize', ['$event'])
  onResize(event) {
    if (this.datatableElement) {
      this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
        dtInstance.columns.adjust();
      })
    }
  } 

  ngOnInit(): void {
    this.dtOptions = {
      paging: false,
      ordering: false,
      scrollCollapse: true,
      info: false,
      searching: false,
      scrollY: "calc(100vh - 545px)",
    }

    this.params = history.state;
    if (this.params.isFromMenu == true) {
      this.getproject();
      $(".openmodal").trigger('click');
    } else {
      if (this.params.dataset_id != undefined) {
        localStorage.setItem("modeling", JSON.stringify(this.params));
      }
      else {
        this.params = localStorage.getItem("modeling");
        this.params = JSON.parse(this.params);
      }
      // this.checkstatus();
      this.checkmodelType(this.params.dataset_id,this.params.project_id)
      this.currentuser = localStorage.getItem("currentUser")
      this.params.user_id = JSON.parse(this.currentuser).id;
      this.getDatasetInfo();
      this.getRunningExperimentList('onload');
      this.getAllExperimentList();
      // setTimeout(() => {
      //   if(this.runningExpList.length==0){
      //     $("#switcher-list")[0].click();
      //   }
      //   else{
      //     this.processclass = "start";
      //   }
      // }, 10);
     
    }
  }

  checkmodelType(dataset_id,project_id){
    this.apiservice.checkmodelType(dataset_id,project_id).subscribe(
      logs=>this.modelTypeSuccessHandlers(logs),
      error=>this.errorHandler(error)
    )
  }

  modelTypeSuccessHandlers(data){
    if(data.status_code=="200"){
      this.model_type=data.response.model_type;
      console.log(this.model_type);
    }
    else{
      this.errorHandler(data);
    }
  }

  projectList: any;
  getproject() {
    this.apiservice.getproject().subscribe(
      logs => this.successProjectListHandler(logs),
      error => this.errorHandler(error)
    );
  }

  successProjectListHandler(data) {
    if (data.status_code == "200") {
      this.projectList = data.response;
    }
    else {
      this.projectList = []
    }
  }

  projectdata: any;
  setproject(value) {
    console.log(value);
    if (value != "") {
      var projects = this.projectList.filter(function (elem) {
        if (elem.project_id == value)
          return elem
      })
      this.getCheckSplit(projects[0].project_id,projects[0].schema_id);
      this.projectdata = projects[0];
    }
    else {
      this.projectdata = undefined
    }
    console.log(this.projectdata);
  }

  setModeling() {
    if (this.projectdata != undefined) {
      this.params = {
        dataset_id: this.projectdata.dataset_id,
        dataset_name: this.projectdata.dataset_name,
        project_id: this.projectdata.project_id, navigate_to: "/project",
        schema_id: this.projectdata.schema_id
      }
      localStorage.setItem("modeling", JSON.stringify(this.params));
      this.currentuser = localStorage.getItem("currentUser")
      this.params.user_id = JSON.parse(this.currentuser).id;
      this.checkmodelType(this.projectdata.dataset_id,this.projectdata.project_id)

      this.getDatasetInfo();
      this.getRunningExperimentList();
      this.getAllExperimentList();
      setTimeout(() => {
      this.modalService.dismissAll();
      }, 0);
    }
    else {
      this.toaster.error("Please select any project", "Error");
    }
  }

  // checkrunningExperiment() {
  //   this.apiservice.checkrunningExperiment(this.params.project_id).subscribe(
  //     logs => this.checkrunningexpuccessHandler(logs),
  //     //  error=>this.errorHandler(error)
  //   )
  // }

  // checkrunningexpuccessHandler(data) {
  //   if (data.status_code == "200") {
  //     if (data.response.exp_name != "") {
  //       this.processInterval = setInterval(() => {
  //         this.getRunningExperimentList();
  //         this.getAllExperimentList();
  //         this.checkstatus();
  //       }, 4000);
  //     }
  //   }
  //   // else {
  //   //   this.errorHandler(data);
  //   // }
  // }

  compareIds = [];
  compareExps = [];
  setCopmareIds(val, id,name) {
    // console.log(val, id);
    if (val == true) {
      this.compareIds.push(id);
      this.compareExps.push({id:id,name:name});
    }
    else {
      // console.log(this.compareIds.indexOf(id));
      var index = this.compareIds.indexOf(id);
      if (index != -1) {
        this.compareIds.splice(index, 1);
      this.compareExps.splice(index,1);

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
    this.apiservice.getAlgorithmList(this.params.dataset_id, this.params.project_id, this.model_type).subscribe(
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

  selectedalgorithm: any;
  selectedalgorithmname: any;
  getHyperParams(event) {
    let val = event.target.value;
    this.selectedalgorithm = val;
    this.selectedalgorithmname = event.target.selectedOptions[0].innerText;
    console.log(this.selectedalgorithmname);
    if (val != "") {
      this.apiservice.getHyperparamsList(val).subscribe(
        logs => this.successParamsListHandler(logs),
        error => this.errorHandler(error));
    }
    else
      this.paramsList = null
  }

  paramsList: any;
  successParamsListHandler(data) {
    if (data.status_code == "200") {
      this.paramsList = data.response;
      console.log(this.paramsList);

    }
    else {
      this.errorHandler(data);
    }
  }

  getRunningExperimentList(type='') {
    this.apiservice.showrunningexperimentslist(this.params.project_id).subscribe(
      logs => this.runningexpListsuccessHandler(logs,type)
      // error => this.errorHandler(error)
    );
  }

  runningExpList: any = [];
  runningexpListsuccessHandler(data,type) {
    if (data.status_code == "200") {
      this.runningExpList = data.response;
      this.contentloaded = true;
      if(type!=''){
        if(this.runningExpList.length==0){
          $("#switcher-list")[0].click();
        }
        else{
          if(type=='onload'){
            // this.processclass = "start";
            // this.processInterval = setInterval(() => {
            //   this.getRunningExperimentList(type);
            //   this.getAllExperimentList();
            //   this.checkstatus(type);
            // }, 4000);
          }
         
        }
      }
    }
    // else {
    //   this.errorHandler(data);
    // }
  }

  getAllExperimentList() {
    this.apiservice.showallexperimentslist(this.params.project_id).subscribe(
      logs => this.allexpListsuccessHandler(logs)
      // error => this.errorHandler(error)
    );
  }

  allExpList: any = [];
  allexpListsuccessHandler(data) {
    if (data.status_code == "200") {
      this.allExpList = [];
      this.allExpList = data.response;
      this.contentloaded = true;
    }
    // else {
    //   this.errorHandler(data);
    // }
  }


  startModel() {

    this.experiment_name = this.params.experiment_name;
    this.experiment_desc = this.params.experiment_desc;
    console.log(this.currentuser);
    let currentuser = localStorage.getItem("currentUser")
    let username = JSON.parse(currentuser).username;
    let obj;
    if (this.model_mode == "Auto") {
      obj = {
        user_name: username,
        dataset_id: this.params.dataset_id,
        project_id: this.params.project_id,
        model_mode: this.model_mode,
        model_type: this.model_type,
        experiment_name: this.params.experiment_name,
        experiment_desc: this.params.experiment_desc,
        model_id: 0,
        model_name: undefined
      }
    }
    else {
      obj = {
        user_name: username,
        dataset_id: this.params.dataset_id,
        project_id: this.params.project_id,
        model_mode: this.model_mode,
        model_type: this.model_type,
        experiment_name: this.params.experiment_name,
        experiment_desc: this.params.experiment_desc,
        model_id: this.responsearray["model_id"],
        model_name: this.responsearray["model_name"],
        hyperparameters: this.responsearray["hyperparameters"]
      }
      this.modalService.dismissAll();
    }

    console.log(obj);

    this.apiservice.startModeling(obj).subscribe(
      logs => this.startsuccessHandler(logs),
      error => this.errorHandler(error)
    )

  }

  changeDisplay() {
    this.isDisplayRunning = !this.isDisplayRunning
  }

  stopModel() {
    this.processclass = "stop";
    if (this.processInterval) {
      clearInterval(this.processInterval);
    }
  }

  checkstatus(type='') {
    let currentuser = localStorage.getItem("currentUser")
    let username = JSON.parse(currentuser).username;
    this.apiservice.checkmodelstatus(this.params.project_id, this.experiment_name, this.params.dataset_id, username,type).subscribe(
      logs => this.statusSuccessHandler(logs)
      // error=>this.errorHandler(error)
    )
  }

  statusSuccessHandler(data) {
    if (data.status_code == "200") {
      if (data.response == "failed" || data.response == "success")
        this.stopModel();
    }
    else {
      this.errorHandler(data);
    }
  }

  startsuccessHandler(data) {
    if (data.status_code == "200") {
      this.processclass = "start";
      this.modalService.dismissAll();
      this.toaster.success(data.error_msg, 'Success');
      if(!this.isDisplayRunning){
          $("#switcher-list")[0].click();
      }
      this.processInterval = setInterval(() => {
        this.getRunningExperimentList();
        this.getAllExperimentList();
        this.checkstatus();
      }, 4000);
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
  current_experiment_id: any;
  current_model_type: any;
  itemstatus:any;
  extraLarge(exlargeModal: any, obj) {
    this.modeltitle = obj.experiment_name;
    this.current_experiment_id = obj.experiment_id;
    this.current_model_type = obj.model_type;
    this.itemstatus=obj.status;
    if(this.itemstatus=="success")
    this.modalService.open(exlargeModal, { size: 'xl', windowClass: 'modal-holder', centered: true });
    if(this.itemstatus=="failed")
    this.modalService.open(exlargeModal, { size: 'sm', windowClass: 'modal-holder', centered: true });
  };

  checkexperimentname(event) {
    var val = event.target.value;
    if (val != "") {
      this.apiservice.checkexperimentname(val, this.params.project_id).subscribe(
        logs => this.checksuccessHandler(logs, event.target),
        error => this.errorHandler(error)
      )
    }
    else
      this.checkuniuqename = false;
  }

  checkuniuqename = true;
  checksuccessHandler(data, target) {
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

onClickStart(modelingmodal:any,largeModal:any){
if(this.model_mode=='Auto'){
this.smallModal(modelingmodal);
}
else{
  this.LargeModal(largeModal,true);
}
}

  smallModal(modelingmodal: any) {
    this.params.experiment_name = ''
    this.params.experiment_desc = ''
    this.modalService.open(modelingmodal, { size: 'md', windowClass: 'modal-holder', centered: true });
  }

  model_mode = 'Auto';
  contentid = 0;
  LargeModal(largeModal: any, val) {
    this.model_mode = 'Auto';
    if (val) {
      this.model_mode = 'Manual';
      this.selectedalgorithm = "";
      this.selectedalgorithmname = "";
      this.paramsList = undefined;
      this.contentid = 1;
      this.getAlgorithmList();
      this.modalService.open(largeModal, { size: 'lg', windowClass: 'modal-holder', centered: true });
    }
  };

  compareExperiment(compareModal: any) {
    console.log(this.compareIds);
    this.modalService.open(compareModal, { size: 'xl', windowClass: 'modal-holder', centered: true });
   
    
  };

  ProjectData(projectModal: any) {
    this.modalService.open(projectModal, { size: 'lg', windowClass: 'modal-holder', centered: true });
  }

  showContent(id) {
    this.contentid = id;
  };

  responsearray = {};
  nextValidate(modelingmodal) {
    var errorflag = false;
    var hyperparameters = {};
    if (this.selectedalgorithm != "") {
      $(".hyperparamsinput").removeClass("errorinput")
      if (this.paramsList.length > 0) {
        var hyperparameters = {};
        this.paramsList.forEach(element => {
          let val;
          if (element.display_type == "") {
            val = $("#txt_" + element.param_name).val();
          }
          if (element.display_type == "validation") {
            val = $("#txt_" + element.param_name).val();
            var valid = element.param_value;
            if (val >= valid[0] && val <= valid[1]) {
            }
            else {
              errorflag = true;
              $("#txt_" + element.param_name).addClass("errorinput")
            }
          }
          if (element.display_type == "dropdown") {
            val = $("#txt_" + element.param_name).val();
          }
          if (val != "") {
            element.value = val;
            hyperparameters[element.param_name] = val;
          }
          else {
            $("#txt_" + element.param_name).addClass("errorinput")
            errorflag = true;
          }
        });
        if (errorflag)
          this.toaster.error("Please enter all valid input", 'Error');

      }
      this.responsearray["model_id"] = this.selectedalgorithm;
      this.responsearray["model_name"] = this.selectedalgorithmname;
      this.responsearray["hyperparameters"] = hyperparameters;
    }
    else {
      this.toaster.error("Please select model", 'Error');
      errorflag = true
    }
    if (!errorflag) {
      this.modalService.dismissAll();
      this.smallModal(modelingmodal);
      // $("#createExperiment").trigger('click');
    }
  }

  getCheckSplit(project_id,schema_id) {
    return this.apiservice.getCheckSplit(project_id,schema_id).subscribe(
      logs => this.checksplitSuccessHandler(logs)
    );
  }

  isEnableModeling = false;
  checksplitSuccessHandler(data) {
    if (data.status_code == "200") {
      this.isEnableModeling = data.response;
      if (!this.isEnableModeling)
        this.toaster.error(data.error_msg, 'Error');
    }
    else {
      this.isEnableModeling = false;
      this.toaster.error(data.error_msg, 'Error');

    }
  }

}
