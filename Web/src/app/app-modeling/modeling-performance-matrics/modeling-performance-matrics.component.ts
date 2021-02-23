import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-performance-matrics',
  templateUrl: './modeling-performance-matrics.component.html',
  styleUrls: ['./modeling-performance-matrics.component.scss']
})
export class ModelingPerformanceMatricsComponent implements OnInit {
  experiment_id: any;
  responsedata: any;
  constructor(public router: Router, public apiservice: ModelingTypeApiService, public toaster: ToastrService) { }

  ngOnInit(): void {
    this.getPerformanceMatrics();
  }

  getPerformanceMatrics() {
    this.apiservice.getPerformanceMatrics(this.experiment_id).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));
  }

  successHandler(data) {
    if (data.status_code == "200") {
      this.responsedata = data.response;
      console.log(this.responsedata);
      // this.toaster.success(data.error_msg, 'Success');
    }
    else {
      this.errorHandler(data);
    }
  }

  errorHandler(error) {
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }
}
