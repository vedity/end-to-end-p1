import { Component, Input, OnInit, ViewChild } from '@angular/core';
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
  animation = "progress-dark";

  theme = {
    'border-radius': '5px',
    'height': '40px',
    'background-color': ' rgb(34 39 54)',
    'border': '1px solid #32394e',
    'animation-duration': '20s'
  };
  public chartOptions1: any;
  public chartOptions2: any;
  public chartOptions1_new: any;
  public chartOptions2_new: any;
  constructor(public router: Router, public apiservice: ModelingTypeApiService, public toaster: ToastrService) { }
  public simpleline: any;
  classname = "expand-block";
  @Input() public experiment_id: any;
  @Input() public model_type: any;
  public columnlabelChartexpand: any;
  responsedata: any;
  ngOnInit(): void {

    this.getActualVsPreidiction();

  }

  public generateDayWiseTimeSeries(baseval, count, yrange) {
    var i = 0;
    var series = [];
    while (i < count) {
      var x = baseval;
      var y =
        Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

      series.push([x, y]);
      baseval += 86400000;
      i++;
    }
    console.log(series);
    return series;
  }


  getActualVsPreidiction() {
    this.apiservice.getActualVsPreidiction(this.experiment_id, this.model_type).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));
  }
  public generateData(data) {
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
      // console.log(this.responsedata);
      this.chartOptions1_new = {
        series: [
          {
            name: "series1",
            data: this.generateDayWiseTimeSeries(
              new Date("11 Feb 2017").getTime(),
              185,
              {
                min: 30,
                max: 90
              }
            )
          }
        ],
        chart: {
          id: "chart2",
          type: "line",
          height: 230,
          toolbar: {
            autoSelected: "pan",
            show: false
          }
        },
        colors: ["#546E7A"],
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
          type: "datetime"
        }
      };

      this.chartOptions2_new = {
        series: [
          {
            name: "series1",
            data: this.generateDayWiseTimeSeries(
              new Date("11 Feb 2017").getTime(),
              185,
              {
                min: 30,
                max: 90
              }
            )
          }
        ],
        chart: {
          id: "chart1",
          height: 130,
          type: "area",
          brush: {
            target: "chart2",
            enabled: true
          },
          selection: {
            enabled: true,
            xaxis: {
              min: new Date("19 Jun 2017").getTime(),
              max: new Date("14 Aug 2017").getTime()
            }
          }
        },
        colors: ["#008FFB"],
        fill: {
          type: "gradient",
          gradient: {
            opacityFrom: 0.91,
            opacityTo: 0.1
          }
        },
        xaxis: {
          type: "datetime",
          tooltip: {
            enabled: false
          }
        },
        yaxis: {
          tickAmount: 2
        }
      };
      if (this.model_type == "Regression") {
        this.chartOptions1 = {
          series: [
            {
              name: "Actual",
              data: this.generateData(this.responsedata.price)
            },
            {
              name: "Prediction",
              data: this.generateData(this.responsedata.price_prediction)
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
          colors: ['#34c38f', '#c3c3c3'],
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
      }
      else {
        this.columnlabelChartexpand = {
          chart: {
            height: 450,
            width: '100%',
            type: 'bar',

            toolbar: {
              show: false
            },
            selection: {
              enabled: true
            }
          },
          // plotOptions: {
          //   bar: {
          //     distributed: true
          //   }
          // },
          plotOptions: {
            bar: {
              horizontal: false,
              columnWidth: "25%",
              // endingShape: "rounded"
            }
          },
          dataLabels: {
            enabled: false
          },
          //colors: ['#00e396d9','#008ffbd9'],
          series: [
            {
              name: 'actual',
              data: this.responsedata.actual,
              //color:'#00e396d9'
            },
            {
              name: 'prediction',
              data: this.responsedata.prediction,
              //color:'#008ffbd9'
            }
          ],
          xaxis: {
            categories: this.responsedata.keys,
            position: 'bottom',
            title: {
              text: 'Categories'
            }
          },
          yaxis: {
            categories: this.responsedata.keys,
            position: 'left',
            labels: {
              show: true,
              align: 'right',
              minWidth: 0,
              maxWidth: 160,
            },
            offsetX: 0,
            offsetY: 0,

          },
          legend: {
            show: true
          }

        };

      }
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
