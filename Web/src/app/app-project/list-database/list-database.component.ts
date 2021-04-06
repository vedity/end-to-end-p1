import { Component, HostListener, OnInit, ViewChild } from '@angular/core';
import { DataTableDirective } from 'angular-datatables';
import { ToastrService } from 'ngx-toastr';
import { Subject } from 'rxjs';
import { ProjectApiService } from '../project-api.service';
import Swal from 'sweetalert2';
import bsCustomFileInput from 'bs-custom-file-input';
import { createdataset } from './dataset.model'
import { NgForm } from '@angular/forms';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Router } from '@angular/router';
@Component({
  selector: 'app-list-database',
  templateUrl: './list-database.component.html',
  styleUrls: ['./list-database.component.scss']
})

export class ListDatabaseComponent implements OnInit {
  @ViewChild(DataTableDirective, { static: false })
  datatableElement: DataTableDirective;
  dtOptions: DataTables.Settings = {
    scrollCollapse: true,
    scrollY: "calc(100vh - 520px)",
    autoWidth:false
  };
  dtTrigger: Subject<any> = new Subject<any>();
  data: createdataset = new createdataset();
  filter: boolean = true;
  loaderdiv = false;
  f: NgForm;
  constructor(public apiService: ProjectApiService, public toaster: ToastrService,private modalService: NgbModal,public router:Router) { }
  transactions: any = [];

	@HostListener('window:resize', ['$event'])
	onResize(event) {
    if (this.datatableElement.dtInstance) {
      this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
        dtInstance.columns.adjust().draw();
      })
    }
	}

  ngOnInit(): void {
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
    else {
      this.transactions = [];
    }
    if (!this.datatableElement.dtInstance) {
      this.dtTrigger.next();
      this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
        dtInstance.columns().every(function () {
          const that = this;
          
          $('#input_'+ this.index("visible")).on('keyup change', function () {
            console.log(this['value']);
            if (that.search() !== this['value']) {
              that
                .search(this['value'])
                .draw();
            }
          });
        });
        dtInstance.columns.adjust();
      });
    }
    else {
      this.rendered();
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

 

  displayfilter() {
    this.filter = !this.filter;
    $('.filter').val('').trigger('change');
  }

  confirm(id,name) {
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
        this.loaderdiv = true;
        this.apiService.deletedataset(id,name).subscribe(
          logs => {
            this.loaderdiv = false;
            if (logs.status_code == "200") {
              Swal.fire('Deleted!', logs.error_msg, 'success');
              this.getdataset();
            }
            else
              Swal.fire('Not Deleted!', logs.error_msg, 'error')
          },
          error => {
            this.loaderdiv = false;
            Swal.fire('Not Deleted!', 'Something went wrong', 'error')
          }
        )
      }
    });
  }

  

  rendered() {
    let currentUrl = this.router.url;
    this.router.routeReuseStrategy.shouldReuseRoute = () => false;
    this.router.onSameUrlNavigation = 'reload';
    this.router.navigate([currentUrl]);
  }

  // errorStatus: boolean = true
  // save() {
  //   let savedata = new FormData();
  //   var user = JSON.parse(localStorage.getItem("currentUser"));
  //   savedata.append('user_name', user.username)//.user_name="admin";
  //   savedata.append('dataset_name', this.data.datasetname);
  //   if (this.data.isprivate)
  //     savedata.append('visibility', "private");
  //   else
  //     savedata.append('visibility', "public");
  //   savedata.append('inputfile', this.datasetfile);
  //   savedata.append('dataset_description', this.data.datasetdescription);
  //   this.loaderdiv = true;
  //   this.modalService.dismissAll();
  //   this.apiService.savedataset(savedata).subscribe(
  //     logs => this.savesuccess(logs),
  //     error => this.errorHandler(error)
  //   )
  // }

  // savesuccess(data) {
  //   if (data.status_code == "200") {

  //     this.loaderdiv = false;
  //     this.getdataset();
  //   }
  //   else
  //     this.errorHandler(data);
  // }

  // smallModal(smallDataModal: any) {
  //   this.data = new createdataset();
  //   this.data.isprivate=true;
  //   this.datasetnameuniqueerror = false;
  //   this.errorStatus=true;
  //   this.modalService.open(smallDataModal, { size: 'sm',windowClass:'modal-holder', centered: true });
  //   bsCustomFileInput.init();

  // }
}