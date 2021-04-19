import { Component, HostListener, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Subject } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { DataTableDirective } from 'angular-datatables';
import { ProjectApiService } from '../project-api.service';
import { ToastrService } from 'ngx-toastr';
import Swal from 'sweetalert2';
@Component({
  selector: 'app-list-project',
  templateUrl: './list-project.component.html',
  styleUrls: ['./list-project.component.scss']
})
export class ListProjectComponent implements OnInit {
  @ViewChild(DataTableDirective, { static: false })
  datatableElement: DataTableDirective;
  pagelength=10;
  dtOptions: DataTables.Settings = {
    scrollCollapse: true,
    scrollY: "calc(100vh - 420px)",
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
  isloaderdiv:boolean=true;
  animation = "progress-dark";
  theme = {
    'border-radius': '5px',
    'height': '40px',
    'background-color': ' rgb(34 39 54)',
    'border': '1px solid #32394e',
    'animation-duration': '20s'
  };
  dtTrigger: Subject<any> = new Subject<any>();
  filter: boolean = true;
  constructor(public router: Router, public http: HttpClient, public apiService: ProjectApiService, public toaster: ToastrService) { }
  transactions: any = [];
  @HostListener('window:resize', ['$event'])
	onResize(event) {
    if (this.datatableElement.dtInstance) {
      this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
        dtInstance.columns.adjust().draw();
      })
    }
	}

//   $('.main-datatable').on( 'length.dt', function ( e, settings, len ) {
//     console.log( 'New page length: '+len );
// } );

  ngOnInit(): void {
    this.getproject();
  }

  getproject() {
    
    this.apiService.getproject().subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error)
    );
  }

  successHandler(data) {
    if (data.status_code == "200") {
      this.transactions = data.response;
    }
    else {
      this.transactions = []
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
      });
    }
    else {
      this.rendered();
      this.dtTrigger.next();
    }
    setTimeout(() => {
    this.isloaderdiv=false;
    }, 0);
  }

  errorHandler(error) {
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
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
  }

  confirm(id) {
    console.log($("#datatablepagelength").val());
    
    this.pagelength=parseInt($("#datatablepagelength").val().toString());
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
        this.apiService.deleteproject(id).subscribe(
          logs => {
            if (logs.status_code == "200") {
              Swal.fire('Deleted!', logs.error_msg, 'success');
              this.getproject();
            }
            else {
              Swal.fire('Not Deleted!', logs.error_msg, 'error')
            }
          },
          error => Swal.fire('Not Deleted!', 'Something went wrong', 'error')
        )
      }
    });
  }

  displayfilter() {
    this.filter = !this.filter;
    $('.filter').val('').trigger('change');
  }
}