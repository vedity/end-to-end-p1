import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import bsCustomFileInput from 'bs-custom-file-input';
import { ToastrService } from 'ngx-toastr';
import { createdataset } from '../list-database/dataset.model';
import { ProjectApiService } from '../project-api.service';
@Component({
  selector: 'app-manage-dataset',
  templateUrl: 'manage-dataset.component.html',
  styleUrls: ['./manage-dataset.component.scss']
})
export class ManageDatasetComponent implements OnInit {
  active = 1;
  data: createdataset = new createdataset();
  loaderdiv = false;
  f: NgForm;
  constructor(public router: Router, public toaster: ToastrService,private modalService: NgbModal, public apiService: ProjectApiService) { }

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

  rendered() {
    let currentUrl = this.router.url;
    this.router.routeReuseStrategy.shouldReuseRoute = () => false;
    this.router.onSameUrlNavigation = 'reload';
    this.router.navigate([currentUrl]);
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
    this.modalService.dismissAll();
    this.apiService.savedataset(savedata).subscribe(
      logs => this.savesuccess(logs),
      error => this.errorHandler(error)
    )
  }

  savesuccess(data) {
    if (data.status_code == "200") {

      this.loaderdiv = false;
      this.rendered();
    }
    else
      this.errorHandler(data);
  }

  smallModal(smallDataModal: any) {
    this.data = new createdataset();
    this.data.isprivate=true;
    this.datasetnameuniqueerror = false;
    this.errorStatus=true;
    this.modalService.open(smallDataModal, { size: 'sm',windowClass:'modal-holder', centered: true });
    bsCustomFileInput.init();

  }
}