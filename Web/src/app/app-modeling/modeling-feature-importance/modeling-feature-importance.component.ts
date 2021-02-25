import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-feature-importance',
  templateUrl: './modeling-feature-importance.component.html',
  styleUrls: ['./modeling-feature-importance.component.scss']
})
export class ModelingFeatureImportanceComponent implements OnInit {
  public barChart: any;
  experiment_id:any;
  responsedata:any;
  animation = "progress-dark";
  theme = {
    'border-radius': '5px',
    'height': '40px',
    'background-color': ' rgb(34 39 54)',
    'border': '1px solid #32394e',
    'animation-duration': '20s'
  };
  constructor(public router: Router, public apiservice: ModelingTypeApiService, public toaster: ToastrService) { }
 
  ngOnInit(): void {

    this.getFutureImportance();
   
  }
  
  getFutureImportance() {
    this.apiservice.getFeatureImportance(this.experiment_id).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));
  }

  successHandler(data) {
    if (data.status_code == "200") {
      this.responsedata = data.response;
      // console.log(this.responsedata);
      this.barChart = {
        chart: {
          height: 400,
          type: 'bar',
          toolbar: {
            show: false
          }
        },
        plotOptions: {
          bar: {
            horizontal: true,
          }
        },
        dataLabels: {
          enabled: false
        },
        series: [{
          data: this.responsedata.norm_importance
        }],
        colors: ['#34c38f'],
        xaxis: {
          // tslint:disable-next-line: max-line-length
          categories: this.responsedata.features_name,
        },
        grid: {
          borderColor: '#f1f1f1'
        },
      };
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
