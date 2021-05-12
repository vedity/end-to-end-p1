import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ProjectApiService } from '../project-api.service';
import { createdataset } from './dataset.model'
import bsCustomFileInput from 'bs-custom-file-input';
import { NgForm } from '@angular/forms';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
@Component({
  selector: 'app-create-dataset',
  templateUrl: './create-dataset.component.html',
  styleUrls: ['./create-dataset.component.scss']
})
export class CreateDatasetComponent implements OnInit {
  constructor(public router: Router, public apiService: ProjectApiService, public toaster: ToastrService,private modalService: NgbModal) { }
  data: createdataset = new createdataset();
  filter: boolean = true;
  loaderdiv = false;
  f: NgForm;

  ngOnInit() {
    this.data.isprivate = true;
    bsCustomFileInput.init();
  }

  datasetfile: File;
  handleFileInput(data: FileList) {
    if (data.length > 0) {
      this.datasetfile = data.item(0);
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
      this.datasetnameuniqueerror = false;
    }
  }

  datasetnameuniqueerror: any = false;
  successUniquedatasetynamevalidation(data, target) {
    if (data.response == 'false') {
      this.datasetnameuniqueerror = true;
      target.className = target.className.replace("ng-valid", " ");
      target.className = target.className + " ng-invalid";
    }
    else {
      this.datasetnameuniqueerror = false;
      target.className = target.className.replace("ng-invalid", " ");
      target.className = target.className + " ng-valid";
    }
  }

  errorHandler(error) {
    this.loaderdiv = false;
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }

  errorStatus: boolean = true
  save() {
    let savedata = new FormData();
    var user = JSON.parse(localStorage.getItem("currentUser"));
    savedata.append('user_name', user.username)//.user_name="admin";
    savedata.append('dataset_name', this.data.datasetname);
    if (this.data.isprivate)
      savedata.append('visibility', "private");
    else
      savedata.append('visibility', "public");

    savedata.append('inputfile', this.datasetfile);
    savedata.append('dataset_description', this.data.datasetdescription);
    this.loaderdiv = true;
    this.apiService.savedataset(savedata).subscribe(
      logs => this.savesuccess(logs),
      error => this.errorHandler(error)
    )
  }

  savesuccess(data) {
    if (data.status_code == "200") {
      this.loaderdiv = false;
      this.data = new createdataset();
      this.data.isprivate=true;
      bsCustomFileInput.init();
      $(".custom-file-label").text("Choose file");

    }
    else
      this.errorHandler(data);
  }

 
}