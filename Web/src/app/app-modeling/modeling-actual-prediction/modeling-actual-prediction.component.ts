import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';
import {
  ChartComponent,
  ApexAxisChartSeries,
  ApexChart,
  ApexXAxis,
  ApexDataLabels,
  ApexYAxis,
  ApexFill,
  ApexMarkers,
  ApexStroke
} from "ng-apexcharts";

@Component({
  selector: 'app-modeling-actual-prediction',
  templateUrl: './modeling-actual-prediction.component.html',
  styleUrls: ['./modeling-actual-prediction.component.scss']
})
export class ModelingActualPredictionComponent implements OnInit {
  @ViewChild("chart") chart: ChartComponent;
  public chartOptions1: any;
  public chartOptions2: any;
  constructor(public router: Router, public apiservice: ModelingTypeApiService, public toaster: ToastrService) { }
  public simpleline: any;
  classname = "expand-block";
  experiment_id:any;
  responsedata:any;
  ngOnInit(): void {
    this.getActualVsPreidiction();
   
  }

  getActualVsPreidiction() {
    this.apiservice.getActualVsPreidiction(this.experiment_id).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));
  }
  public generateDayWiseTimeSeries(data) {
    var i = 0;
    var series = [];
    while (i < this.responsedata.index.length) {
      var x = this.responsedata.index[i];
      var y = data[i];
      series.push([x, y]);
      i++;
    }
    return series;
  }

  successHandler(data) {
    if (data.status_code == "200") {
      this.responsedata = data.response;
      console.log(this.responsedata);

      this.chartOptions1 = {
        series: [
          {
            name: "Actual",
            data: this.generateDayWiseTimeSeries(this.responsedata.price)
          },
          {
            name: "Prediction",
            data: this.generateDayWiseTimeSeries(this.responsedata.price_prediction)
          }
        ],
        chart: {
          id: "chart2",
          type: "line",
          height: 350,
          toolbar: {
            show: true
          }
        },
        colors: ['#c3c3c3', '#34c38f'],
        stroke: {
          width: 3
        },
        dataLabels: {
          enabled: false
        },
        fill: {
          opacity: 1
        },
        markers: {
          size: 0
        },
        xaxis: {
          labels: {
            show: false
          }
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

  allowExpand() {
    this.classname == '' ? this.classname = 'expand-block' : this.classname = '';
    window.dispatchEvent(new Event('resize'));
  }
}
