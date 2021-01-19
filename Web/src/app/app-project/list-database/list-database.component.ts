import { Component, OnInit, ViewChild } from '@angular/core';
import { DataTableDirective } from 'angular-datatables';
import { ToastrService } from 'ngx-toastr';
import { Subject } from 'rxjs';
import { ProjectApiService } from '../project-api.service';
import Swal from 'sweetalert2';
import bsCustomFileInput from 'bs-custom-file-input';
import { createdataset } from './dataset.model'

@Component({
  selector: 'app-list-database',
  templateUrl: './list-database.component.html',
  styleUrls: ['./list-database.component.scss']
})
export class ListDatabaseComponent implements OnInit {
  @ViewChild(DataTableDirective, { static: false })
  datatableElement: DataTableDirective;
  dtOptions: DataTables.Settings = {};
  dtTrigger: Subject<any> = new Subject<any>();
  data: createdataset = new createdataset();
  filter: boolean = true;
  constructor(public apiService: ProjectApiService, public toaster: ToastrService) { }
  transactions: any=[];
  ngOnInit(): void {
    this.data.isprivate = true;
    bsCustomFileInput.init();
    this.getdataset();
  }

  getdataset() {
    this.apiService.getDataset().subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error)
    );
  }
  
  successHandler(data) {
    if (data.status_code == "200") {
      this.transactions = data.response;
    }
    else{
      this.transactions=[];
    }
    console.log(this.datatableElement.dtInstance);
    
    if(!this.datatableElement.dtInstance){
      this.dtTrigger.next();
    this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
      dtInstance.columns().every(function () {
        const that = this;
        $('input', this.header()).on('keyup change', function () {
          if (that.search() !== this['value']) {
            that
              .search(this['value'])
              .draw();
          }
        });
        $('select', this.header()).on('change', function () {
          if (that.search() !== this['value']) {
            that
              .search(this['value'])
              .draw();
          }
        });
      });
    });
    }
    else{
      this.rendered();
      this.dtTrigger.next();

    }
  }

  errorHandler(error) {
    console.log(error);
    if(error.error_msg)
    this.toaster.error(error.error_msg, 'Error');
    else
    {
      console.log(error);
    this.toaster.error('Something went wrong', 'Error');
    }
  }

  datasetfile: File;
  handleFileInput(data: FileList) {
    if (data.length > 0) {
      console.log(data);
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
    else{
      this.datasetnameuniqueerror = false;

    }
  }
  datasetnameuniqueerror: any = false;

  successUniquedatasetynamevalidation(data, target) {
    if (data.response == 'false') {
      // this.errorStatus=false;
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

  displayfilter() {
    this.filter = !this.filter;
    console.log(this.filter);
    $('.filter').val('').trigger('change');
    // elem.value += ' NEW';
  }

  confirm(id) {
    Swal.fire({
      title: 'Are you sure?',
      text: 'You won\'t be able to revert this!',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#34c38f',
      cancelButtonColor: '#f46a6a',
      confirmButtonText: 'Yes, delete it!'
    }).then(result => {
      if (result.value) {
        this.apiService.deletedataset(id).subscribe(
          logs => {
            if (logs.status_code == "200") {
              Swal.fire('Deleted!', logs.error_msg, 'success');
              this.getdataset();
              
            }
            else
              Swal.fire('Not Deleted!', logs.error_msg, 'error')
          },
          error => Swal.fire('Not Deleted!', 'Something went wrong', 'error')
        )

      }
    });
  }

  rendered() {
    this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
      dtInstance.columns().every(function () {
        const that = this;
        $('input', this.header()).on('keyup change', function () {
          if (that.search() !== this['value']) {
            that
              .search(this['value'])
              .draw();
          }
        });
        $('select', this.header()).on('change', function () {
          if (that.search() !== this['value']) {
            that
              .search(this['value'])
              .draw();
          }
        });
      });
      dtInstance.destroy();
    });
  }

 
  errorStatus: boolean = true
  save() {
    let savedata = new FormData();
    var user=JSON.parse(localStorage.getItem("currentUser"));
    savedata.append('user_name', user.username)//.user_name="admin";
    savedata.append('dataset_name', this.data.datasetname);
    if (this.data.isprivate)
      savedata.append('visibility', "private");
    else
      savedata.append('visibility', "public");

    savedata.append('inputfile', this.datasetfile);
    this.apiService.savedataset(savedata).subscribe(
      logs => this.savesuccess(logs),
      error => this.errorHandler(error)
    )
  }

  savesuccess(data) {
    if (data.status_code == "200") {
      this.getdataset();
    }
    else
      this.errorHandler(data);
  }
}