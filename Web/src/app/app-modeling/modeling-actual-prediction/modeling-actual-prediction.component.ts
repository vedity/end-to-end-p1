import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';
import {
  ChartComponent
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
      if (this.model_type == "Regression") {
        localStorage.setItem('responsedata', JSON.stringify(this.responsedata));

        this.chartOptions1 = {
          series: [
            {
              name: "Actual",
              data: this.generateData(this.responsedata.actual)
            },
            {
              name: "Prediction",
              data: this.generateData(this.responsedata.prediction)
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
          },
          tooltip: {
            onDatasetHover: {
              highlightDataSeries: false,
            },
            fixed:true,
            custom: function ({ series, seriesIndex, dataPointIndex, w }) {

              var data = localStorage.getItem('responsedata');
              var responsedata = JSON.parse(data);
             var titlehtml = '<div class="apexcharts-tooltip-title" style="font-family: Helvetica, Arial, sans-serif; font-size: 12px;">' + responsedata.index[dataPointIndex] + '' +
                ' </div>';

                var html = '<div class="apexcharts-tooltip-series-group apexcharts-active" style="display: flex;"><span ' +
                'class="apexcharts-tooltip-marker" style="background-color: rgb(52, 195, 143);"></span>' +
                '<div class="apexcharts-tooltip-text" style="font-family: Helvetica, Arial, sans-serif; font-size: 12px;">' +
                '<div class="apexcharts-tooltip-y-group"><span class="apexcharts-tooltip-text-label">Actual: </span><span ' +
                'class="apexcharts-tooltip-text-value">' + series[0][dataPointIndex] + '</span></div>' +
                '</div>' +
                '</div>' +
                '<div class="apexcharts-tooltip-series-group apexcharts-active" style="display: flex;"><span ' +
                'class="apexcharts-tooltip-marker" style="background-color: rgb(195, 195, 195);"></span>' +
                '<div class="apexcharts-tooltip-text" style="font-family: Helvetica, Arial, sans-serif; font-size: 12px;">' +
                '<div class="apexcharts-tooltip-y-group"><span class="apexcharts-tooltip-text-label">Prediction: </span><span ' +
                'class="apexcharts-tooltip-text-value">' + series[1][dataPointIndex] + '</span></div>' +
                '</div>' +
                '</div>';
              var popupkeys = responsedata.popup_keys;
              var vals = responsedata.popup_values;
              var datahtml = '';
              popupkeys.forEach((element, index) => {
                datahtml = datahtml + '<div class="apexcharts-tooltip-series-group apexcharts-active" style="display: flex;"><span ' +
                  'class="apexcharts-tooltip-marker" style="background-color: #008FFB;"></span>' +
                  '<div class="apexcharts-tooltip-text" style="font-family: Helvetica, Arial, sans-serif; font-size: 12px;">' +
                  '<div class="apexcharts-tooltip-y-group"><span class="apexcharts-tooltip-text-label">' + element + ': </span><span ' +
                  'class="apexcharts-tooltip-text-value">' + vals[index][dataPointIndex] + '</span></div>' +
                  '</div>' +
                  '</div>';
              });
              var finalhtml = titlehtml+' <div class="apex-scroll">'+ html + datahtml+'</div>';
              //var finalhtml = titlehtml+ html + datahtml;
              return finalhtml;
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
