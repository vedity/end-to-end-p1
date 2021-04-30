import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';
import { ChartComponent } from "ng-apexcharts";

@Component({
  selector: 'app-modeling-confusion-matrics',
  templateUrl: './modeling-confusion-matrics.component.html',
  styleUrls: ['./modeling-confusion-matrics.component.scss']
})
export class ModelingConfusionMatricsComponent implements OnInit {
  @Input() public experiment_id: any;
  @ViewChild("chart") chart: ChartComponent;

  responsedata: any;
  chartOptions:any;
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
    this.setConfusionMatrix();
   // this.getConfusionMatrics();
  }

  getConfusionMatrics() {
    this.apiservice.getConfusionMatrix(this.experiment_id).subscribe(
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

  setConfusionMatrix(){
    this.chartOptions = {

      series: [
        {
          name: "Metric1",
          data: this.generateData(5, {
            min: 0,
            max: 90
          })
        },
        {
          name: "Metric2",
          data: this.generateData(5, {
            min: 0,
            max: 90
          })
        },
        {
          name: "Metric3",
          data: this.generateData(5, {
            min: 0,
            max: 90
          })
        },
        {
          name: "Metric4",
          data: this.generateData(5, {
            min: 0,
            max: 90
          })
        },
        {
          name: "Metric5",
          data: this.generateData(5, {
            min: 0,
            max: 90
          })
        } 
      ],
      chart: {
        height: 450,
        width:450,
        type: "heatmap",
        toolbar: {
          show: false
        }
      },
      dataLabels: {
        enabled: true
      },
      plotOptions: {
        heatmap: {
          shadeIntensity: 0.5,
          colorScale: {
            ranges: [
              
              {
                from: 0,
                to: 100,
                color: "#128FD9"
              },{
                  from:101,
                  to:1000,
                  color:"#00A100"
              }

            ]
          }
        }
      }
      
    };
  

  
  }



  public generateData(count, yrange) {
    var i = 0;
    var series = [];
    while (i < count) {
      var x = "Metric" + (i + 1).toString();
      var y =
        Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

      series.push({
        x: x,
        y: y
      });
      i++;
    }
    console.log(series)
    return series;
  }
}
