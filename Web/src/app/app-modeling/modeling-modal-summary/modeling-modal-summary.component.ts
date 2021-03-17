import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-modal-summary',
  templateUrl: './modeling-modal-summary.component.html',
  styleUrls: ['./modeling-modal-summary.component.scss']
})
export class ModelingModalSummaryComponent implements OnInit {

  constructor(public router: Router, public apiservice: ModelingTypeApiService, public toaster: ToastrService) { }
  experiment_id: any;
  responsedata: any;
  animation = "progress-dark";
  theme = {
    'border-radius': '5px',
    'height': '40px',
    'background-color': ' rgb(34 39 54)',
    'border': '1px solid #32394e',
    'animation-duration': '20s'
  };
  ngOnInit(): void {
    this.getModelSummary();
  }

  getModelSummary() {
    this.apiservice.getModelSummary(this.experiment_id).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));
  }

  successHandler(data) {
    if (data.status_code == "200") {
      this.responsedata = data.response;
      // console.log(this.responsedata);
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
