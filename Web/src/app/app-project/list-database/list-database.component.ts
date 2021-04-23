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
  classfilter:any="nofilter"
  dtOptions: DataTables.Settings = {
    scrollCollapse: true,
    scrollY: "calc(100vh - 520px)",
    autoWidth:false,
    preDrawCallback:function(e){
      $(".filter-box").on("click",function(event){
        event.stopPropagation();
      })

    },
    drawCallback:function(e){
      $("#datatablepagelength").val(e._iDisplayLength);
    },
     pageLength:10
  };
  
  dtTrigger: Subject<any> = new Subject<any>();
  filter: boolean = true;
  loaderdiv = false;
  isloaderdiv:boolean=true;
  animation = "progress-dark";
  theme = {
    'border-radius': '5px',
    'height': '40px',
    'background-color': ' rgb(34 39 54)',
    'border': '1px solid #32394e',
    'animation-duration': '20s'
  };
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
    setTimeout(() => {
      this.isloaderdiv=false;
    }, 0);
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
    $(".filter-tr").toggleClass("nofilter");
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
    this.dtOptions.pageLength=parseInt($("#datatablepagelength").val().toString());
    this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
      dtInstance.columns().every(function () {
        const that = this;
        $('#input_'+ this.index("visible")).on('keyup change', function () {
          if (that.search() !== this['value']) {
            that
              .search(this['value'])
              .draw();
          }
        });
      });
      dtInstance.destroy();
    });
    this.dtTrigger.next();
  }

}