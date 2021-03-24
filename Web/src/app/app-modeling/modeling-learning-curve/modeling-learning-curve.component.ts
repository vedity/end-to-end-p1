import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-learning-curve',
  templateUrl: './modeling-learning-curve.component.html',
  styleUrls: ['./modeling-learning-curve.component.scss']
})
export class ModelingLearningCurveComponent implements OnInit {

  constructor(public router: Router, public apiservice: ModelingTypeApiService, public toaster: ToastrService) { }
  public lineColumAreaChart: any;
  @Input() public experiment_id: any;
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

    this.getLearningCureve();
    
  }

  getLearningCureve() {
    this.apiservice.getLearningCurves(this.experiment_id).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));
  }

  successHandler(data) {
    if (data.status_code == "200") {
      this.responsedata =data.response;
      // console.log(this.responsedata);
      this.lineColumAreaChart = {
        chart: {
          height: 400,
          type: 'line',
          stacked: false,
          toolbar: {
            show: false
          }
        },
        stroke: {
          width: [2, 2, 4],
          //   curve: 'smooth'
        },
        //   plotOptions: {
        //       bar: {
        //           columnWidth: '50%'
        //       }
        //   },
        colors: ['#f46a6a', '#34c38f'],
        series: [{
          name: 'Test Score',
          //   type: 'line',
          data: this.responsedata.test_score
        }, {
          name: 'Train Score',
          //   type: 'line',
          data: this.responsedata.train_score
        }],
        fill: {
          opacity: [0.85, 1],
          gradient: {
            inverseColors: false,
            shade: 'light',
            type: 'vertical',
            opacityFrom: 0.85,
            opacityTo: 0.55,
            stops: [0, 100, 100, 100]
          }
        },
        // tslint:disable-next-line: max-line-length
        //labels: ['01/01/2003', '02/01/2003', '03/01/2003', '04/01/2003', '05/01/2003', '06/01/2003', '07/01/2003', '08/01/2003', '09/01/2003', '10/01/2003', '11/01/2003'],
        markers: {
          size: [0, 2]
        },
        legend: {
          offsetY: 5,
        },
        xaxis: {
          categories:this.responsedata.train_size
         // type: 'datetime',
        },
        yaxis: {
         
        },
        tooltip: {
          shared: true,
          intersect: false,
         
        },
        grid: {
          borderColor: '#f1f1f1'
        }
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
