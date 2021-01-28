import { Component, OnInit } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import Swal from 'sweetalert2';
import { ProjectApiService } from '../project-api.service';

@Component({
  selector: 'app-detailview-project',
  templateUrl: './detailview-project.component.html',
  styleUrls: ['./detailview-project.component.scss']
})
export class DetailviewProjectComponent implements OnInit {
  transactions: any;
  tabledata: any;
  constructor(public toaster: ToastrService, public apiService: ProjectApiService) { }

  ngOnInit() {
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
      this.tabledata = data.response;
      console.log(this.transactions);

    }
    else {
      this.transactions = []
    }
  }

  errorHandler(error) {
    console.log(error);
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      console.log(error);
      this.toaster.error('Something went wrong', 'Error');
    }
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

  filterdata(search) {
    var result = this.tabledata.filter(function (element) {
      var display = $("#project-card-" + element.project_id).text().toLowerCase().includes(search);
      element.display = display;
      return element;
    })
    this.transactions = result;
  }
}
