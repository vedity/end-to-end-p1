import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ProjectApiService } from '../project-api.service';
import { createproject } from './project.model'

import bsCustomFileInput from 'bs-custom-file-input';
@Component({
  selector: 'app-create-project',
  templateUrl: './create-project.component.html',
  styleUrls: ['./create-project.component.scss']
})
export class CreateProjectComponent implements OnInit {

  constructor(public router: Router, public apiService: ProjectApiService, public toaster: ToastrService) { }
  public data: createproject = new createproject();
  disableclass:any="";
  datasetlist: any;
  errorStatus: boolean = true;
  errorMessage: any = "";
  validfile: any;
  ngOnInit() {
    this.data.isprivate=true;
    this.apiService.getDataset().subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error)
    );
    bsCustomFileInput.init();
  }

  successHandler(data) {
    if (data.status_code == "200") {
      this.datasetlist = data.response;
      // this.toaster.success( 'Data Load Successfully','Success');
    }
    else
      this.errorHandler(data);
  }

  checkuniqueprojectname(event) {
    var val = event.target.value;
    if (val != "") {
      this.apiService.checkUniqueProjectName(val).subscribe(
        logs => this.successUniquenamevalidation(logs, event.target),
        error => this.errorHandler(error)
      );
    }
    else
    this.projectnameuniqueerror = false;

  }
  projectnameuniqueerror: any = false;

  successUniquenamevalidation(data, target) {
    console.log(data);
    if (data.response == 'false') {
      // this.errorStatus=false;
      this.projectnameuniqueerror = true;
      target.className=target.className.replace("ng-valid", " ");
      target.className = target.className + " ng-invalid";
    }
    else{
      this.projectnameuniqueerror = false;
      target.className=target.className.replace("ng-invalid", " ");
      target.className = target.className + " ng-valid";

    }
  }


  checkuniquedatasetname(event) {
    var val = event.target.value;
    if (val != "") {
      this.apiService.checkUniqueDatasetName(val).subscribe(
        logs => this.successUniquedatasetynamevalidation(logs, event.target),
        error => this.errorHandler(error)
      );
    }
    else {
      this.datasetdisablevalidation = false;

    }
  }
  selectchangedisablevalidation: any = false;
  datasetnameuniqueerror: any = false;
  datasetdisablevalidation: any = false;
  successUniquedatasetynamevalidation(data, target) {
    this.datasetdisablevalidation = true;
    if (data.response == 'false') {
      // this.errorStatus=false;
      this.datasetnameuniqueerror = true;
      target.className.replace("ng-valid", " ");
      target.className = target.className + " ng-invalid";
    }

  }

  datasetfile: File;
  handleFileInput(data: FileList) {
    if (data.length > 0) {
      this.datasetdisablevalidation = true;
      console.log(data);
      this.datasetfile = data.item(0);
    }
    else {
      this.datasetdisablevalidation = false;

    }
  }
  errorHandler(error) {
    console.log(error);
    this.toaster.error('Something went wrong', 'Error');
  }
  selectchange(){
console.log(this.data.datsetid);
if(this.data.datsetid.toString()!=""){
  this.selectchangedisablevalidation=true;
  this.disableclass="disabled";
}
else{
  this.disableclass="";
  this.selectchangedisablevalidation=false;
}
  }
  save() {
    let savedata =new FormData();
savedata.append('user_name','admin')//.user_name="admin";
savedata.append('dataset_id',this.data.datsetid?this.data.datsetid.toString():'')//.dataset_id=this.data.datsetid;
savedata.append('dataset_name',this.data.datasetname);
savedata.append('project_name',this.data.projectname);
savedata.append('description',this.data.description);
if(this.data.isprivate)
savedata.append('visibility',"private");
else
savedata.append('visibility',"public");

savedata.append('inputfile',this.datasetfile);
this.apiService.saveproject(savedata).subscribe(
  logs => this.savesuccess(logs),
  error => this.errorHandler(error)
)
  }

  savesuccess(data){
    if(data.status_code=="200")
    this.router.navigate(['project']);
    else
    this.errorHandler(data);
  }
}
