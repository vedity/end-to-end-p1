import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Observable, Subject } from 'rxjs';
import { HttpClient, HttpParams } from '@angular/common/http';
import { DataTableDirective } from 'angular-datatables';
import { ApiService } from '../api.service';
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
  dtOptions: DataTables.Settings = {};
   
  dtTrigger: Subject<any> = new Subject<any>();
  filter: boolean = true;
  constructor(public router: Router, public http: HttpClient, public apiService: ApiService,public toaster:ToastrService) { }
  transactions: any;
  ngOnInit(): void {
    this.apiService.getproject().subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error)
    );
  }

  successHandler(data){
    if(data.status_code=="200"){
      this.transactions=data.response;
     // this.toaster.success( 'Data Load Successfully','Success');
    }
    else
        this.errorHandler(data);
}

errorHandler(error) {
    console.log(error);
    this.toaster.error('Something went wrong','Error');
}

  ngAfterViewInit(): void {
  //  this.dtTrigger.next();

    setTimeout(() => {
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
        });
      });
   
    }, 700);
    }

    confirm() {
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
          Swal.fire('Deleted!', 'Project has been deleted.', 'success');
        }
      });
    }

  displayfilter() {
    this.filter = !this.filter;
    console.log(this.filter);
    $('.filter').val('').trigger('change');
  }

  create() {
    this.router.navigate(['create']);
  }

  getUserNumber(): Observable<any> {
    return this.http.get<any>("http://127.0.0.1:8000/mlaas/ingest/create_project");
  }
}