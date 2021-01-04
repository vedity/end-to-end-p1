import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ApiService } from '../api.service';
import {createproject} from './project.model'

import bsCustomFileInput from 'bs-custom-file-input';
@Component({
  selector: 'app-create-project',
  templateUrl: './create-project.component.html',
  styleUrls: ['./create-project.component.scss']
})
export class CreateProjectComponent implements OnInit {

  constructor(public router:Router,public apiService:ApiService,public toaster:ToastrService) { }
 public data:createproject =  new createproject();
 datasetlist:any;
 errorStatus:boolean=true;
 errorMessage:any="";
 validfile:any;
  ngOnInit() {
    this.apiService.getDataset().subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error)
    );
    bsCustomFileInput.init();
  }

  successHandler(data){
    if(data.status_code=="200"){
      this.datasetlist=data.response;
     // this.toaster.success( 'Data Load Successfully','Success');
    }
    else
        this.errorHandler(data);
}

checkuniqueprojectname(event){
  var val=event.target.value;
  if(val!=""){
      this.apiService.checkUniqueProjectName(val).subscribe(
        logs => this.successUniquenamevalidation(logs,event.target),
        error => this.errorHandler(error)
      );
  }
}
projectnameuniqueerror:any=false;

successUniquenamevalidation(data,target){
  console.log(data);
if(data.response=='false'){
  // this.errorStatus=false;
  this.projectnameuniqueerror=true;
  target.className.replace("ng-valid"," ");
  target.className=target.className +" ng-invalid";
}
}


checkuniquedatasetname(event){
  var val=event.target.value;
  if(val!=""){
      this.apiService.checkUniqueDatasetName(val).subscribe(
        logs => this.successUniquedatasetynamevalidation(logs,event.target),
        error => this.errorHandler(error)
      );
  }
}
datasetnameuniqueerror:any=false;

successUniquedatasetynamevalidation(data,target){
  console.log(data);
if(data.response=='false'){
  // this.errorStatus=false;
  this.datasetnameuniqueerror=true;
  target.className.replace("ng-valid"," ");
  target.className=target.className +" ng-invalid";
}
}

errorHandler(error) {
    console.log(error);
    this.toaster.error('Something went wrong','Error');
}

  save(){
    console.log("called")
  }

}
