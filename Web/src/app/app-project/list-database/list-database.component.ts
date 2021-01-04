import { Component, OnInit, ViewChild } from '@angular/core';
import { DataTableDirective } from 'angular-datatables';
import { ToastrService } from 'ngx-toastr';
import { Subject } from 'rxjs';
import { ApiService } from '../api.service';
import Swal from 'sweetalert2';
import bsCustomFileInput from 'bs-custom-file-input';


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

  filter: boolean = true;
  constructor(public apiService: ApiService, public toaster: ToastrService) { }
  transactions: any;
  ngOnInit(): void {
    this.apiService.getDataset().subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error)
    );
    bsCustomFileInput.init();

  }

  successHandler(data) {
    if (data.status_code == "200") {
      this.transactions = data.response;
      // this.toaster.success( 'Data Load Successfully','Success');
    }
    else
      this.errorHandler(data);
  }

  errorHandler(error) {
    console.log(error);
    this.toaster.error('Something went wrong', 'Error');
  }


  checkuniquedatasetname(event) {
    var val = event.target.value;
    if (val != "") {
      this.apiService.checkUniqueDatasetName(val).subscribe(
        logs => this.successUniquedatasetynamevalidation(logs, event.target),
        error => this.errorHandler(error)
      );
    }
  }
  datasetnameuniqueerror: any = false;

  successUniquedatasetynamevalidation(data, target) {
    console.log(data);
    if (data.response == 'false') {
      // this.errorStatus=false;
      this.datasetnameuniqueerror = true;
      target.className.replace("ng-valid", " ");
      target.className = target.className + " ng-dirty ng-invalid";
    }
  }

  displayfilter() {
    this.filter = !this.filter;
    console.log(this.filter);
    $('.filter').val('').trigger('change');
    // elem.value += ' NEW';
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
  ngAfterViewInit(): void {
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
}