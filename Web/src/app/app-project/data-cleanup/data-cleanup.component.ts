import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { DataTableDirective } from 'angular-datatables';
import { ToastrService } from 'ngx-toastr';
import { DataCleanupApiService } from '../data-cleanup.service';
@Component({
  selector: 'app-data-cleanup',
  templateUrl: './data-cleanup.component.html',
  styleUrls: ['./data-cleanup.component.scss']
})
export class DataCleanupComponent implements OnInit {
  @ViewChild(DataTableDirective, { static: false })
  datatableElement: DataTableDirective;
  dtOptions: DataTables.Settings = {};
  constructor(public apiService: DataCleanupApiService, public toaster: ToastrService, private modalService: NgbModal, public router: Router) { }
  @Input() public dataset_id: any;
  @Input() public title: any;
  @Input() public project_id: any
  @Input() public schema_id: any
  loaderdiv = false;
  displaytitle = "false";
  errorStatus = true;
  operationList: any;
  columnList: any;
  animation = "progress-dark";
  theme = {
    'border-radius': '5px',
    'height': '40px',
    'background-color': ' rgb(34 39 54)',
    'border': '1px solid #32394e',
    'animation-duration': '20s'
  };

  ngOnInit(): void {
    this.dtOptions = {
      paging: false,
      ordering: false,
      scrollCollapse: true,
      info: false,
      searching: false,
      //scrollX: true,
      scrollY: "52vh",
    }
    this.loaderdiv=true;
    this.getOpertion();
    this.getColumnList();
  }


  successHandler(logs) {
    this.loaderdiv = false;
  }

  errorHandler(error) {
    this.loaderdiv = false;
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }

  getOpertion() {
    this.apiService.getOperation().subscribe(
      logs => this.operationlistsuccessHandler(logs),
      error => this.errorHandler(error)
    )
  }

  operationlistsuccessHandler(data) {
    if (data.status_code == "200") {
      this.operationList = data.response;
    }
    else {
      this.errorHandler(data);
    }
  }

  getColumnList() {
    this.apiService.getColumnList(this.schema_id).subscribe(
      logs => this.columnlistsuccessHandler(logs),
      error => this.errorHandler(error)
    )
  }

  columnlistsuccessHandler(data) {
    if (data.status_code == "200") {
      this.columnList = data.response;
      setTimeout(() => {
      this.loaderdiv=false;
        
      }, 10);
    }
    else {
      this.errorHandler(data);
    }
  }
}