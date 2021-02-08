import { Component, Input, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ToastrService } from 'ngx-toastr';
import { DataExplorationApiService } from '../data-exploration.service';
import { Chart } from 'angular-highcharts';
import * as Highcharts from 'highcharts';
// require('highcharts/themes/dark-unica')(Highcharts);
Highcharts.setOptions({
  colors: ['#058DC7', '#50B432', '#ED561B', '#DDDF00', '#24CBE5', '#64E572',
    '#FF9655', '#FFF263', '#6AF9C4'],
  chart: {
    backgroundColor: {
      // linearGradient: [0, 0, 500, 500],

      stops: [
        [0, 'rgb(255, 255, 255)'],
        [1, 'rgb(240, 240, 255)']
      ]
    },
  },
  title: {
    style: {
      display: 'none',
      color: '#fff',
      font: 'bold 16px "Trebuchet MS", Verdana, sans-serif'
    }
  },
  subtitle: {
    style: {
      color: '#fff',
      font: 'bold 12px "Trebuchet MS", Verdana, sans-serif'
    }
  },
  legend: {
    itemStyle: {
      font: '9pt Trebuchet MS, Verdana, sans-serif',
      color: '#fff'
    },
    itemHoverStyle: {
      color: '#fff'
    }
  },
  credits: {
    style: {
      display: 'none'
    }
  },
  xAxis: {
    gridLineColor: '#32394e',
    labels: {
      style: {
        color: '#bfc8e2'
      }
    },
    lineColor: '#32394e',
    minorGridLineColor: '#505053',
    tickColor: '#32394e',
    tickWidth: 1,

  },
  yAxis: {
    gridLineColor: '#32394e',
    labels: {
      style: {
        color: '#bfc8e2'
      }
    },
    lineColor: '#32394e',
    minorGridLineColor: '#505053',
    tickColor: '#707073',
    tickWidth: 0,

  },
});



// import * as Highcharts from 'angular-highcharts';
@Component({
  selector: 'app-data-exploration',
  templateUrl: './data-exploration.component.html',
  styleUrls: ['./data-exploration.component.scss']
})

export class DataExplorationComponent implements OnInit {



  constructor(public apiService: DataExplorationApiService, public toaster: ToastrService, private modalService: NgbModal,) { }
  @Input() public dataset_id: any;
  @Input() public title: any;
  @Input() public project_id: any
  chart: Chart;
  loaderdiv = false;
  displaytitle = "false";
  exploredData: any = [];
  finaldata: any = [];
  columnlabelChart: any;
  columnlabelChartexpand: any;
  boxplotChartexpand: any;
  animation = "progress-dark";
  theme = {
    'border-radius': '5px',
    'height': '40px',
    'background-color': ' rgb(34 39 54)',
    'border': '1px solid #32394e',
    'animation-duration': '20s'
  };
  displayselectedtitle = "Continous";

  ngOnInit(): void {
    this.loaderdiv = true;
    this.columnlabelChart = {
      chart: {
        width: '100%',
        type: 'bar',
        offsetX: 0,
        offsetY: -26,
        toolbar: {
          show: false
        },
      },
      grid: {
        xaxis: {
          lines: {
            show: false
          }
        },
        yaxis: {
          lines: {
            show: false
          }
        },
        padding: {
          left: 0,
          right: 0,
          top: 0,
          bottom: 0
        },
      },
      colors: ['#34c38f'],
      dataLabels: {
        enabled: false
      },
      yaxis: {
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false,
        },
        labels: {
          show: false,
          formatter: (val) => {
            return val;
          }
        }
      },
      xaxis: {
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false,
        },
        labels: {
          show: false,
          formatter: (val) => {
            return val;
          }
        }
      },
    };


    this.getExplorationData(this.dataset_id);
  }

  getExplorationData(datasetid) {
    this.apiService.getExplorationData(datasetid).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error)
    )
  }

  continuousexploredata: any;
  categoricalexploredata: any;
  successHandler(logs) {
    if (logs.status_code == "200") {
      this.exploredData = logs.response;
      var data = this.groupBy(this.exploredData, "Datatype");
      this.continuousexploredata = data["Continuous"];
      this.categoricalexploredata = data["Categorical"];
      this.loaderdiv = false;
      this.finaldata = logs.response;
    }
    else {
      this.errorHandler(logs)
    }
  }

  groupBy(xs, key) {
    return xs.reduce(function (rv, x) {
      (rv[x[key]] = rv[x[key]] || []).push(x);
      return rv;
    }, {});
  };

  errorHandler(error) {
    this.loaderdiv = false;
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }

  modeltitle: any;
  hideboxplot = true;
  modalobj: any;
  centerModal(centerDataModal: any, obj) {
    this.modalobj = obj;
    this.modeltitle = obj["Column Name"];
    this.columnlabelChartexpand = {
      chart: {
        height: '500px',
        width: '100%',
        type: 'bar',
        toolbar: {
          show: true
        },
      },
      dataLabels: {
        enabled: false
      },
      colors: ['#34c38f', 'red', 'red'],
      series: [{
        data: obj["Plot Values"][1]
      }
        // ,{
        //   data:obj["Left Outlier Values"][1]
        // },
        // {
        //   data:obj["Right Outlier Values"][1]
        // }
      ],
      xaxis: {
        categories: obj["Plot Values"][0],
        position: 'bottom',
      },
      yaxis: {
        position: 'left',
        labels: {
          show: true,
          align: 'right',
          minWidth: 0,
          maxWidth: 160,
        },
        offsetX: 0,
        offsetY: 0,
      }
    };



    let outliers = [];
    if (obj["Left Outlier Values"].length > 0) {
      if (obj["Left Outlier Values"][0].length > 0) {
        let leftoutlier = obj["Left Outlier Values"][0];
        leftoutlier.forEach(element => {
          outliers.push([0, element])
        });
      }
    }

    if (obj["Right Outlier Values"].length > 0) {
      if (obj["Right Outlier Values"][0].length > 0) {
        let rightoutlier = obj["Right Outlier Values"][0];
        rightoutlier.forEach(element => {
          outliers.push([0, element])
        });
      }
    }

console.log(outliers);

    if (obj["open"] != null) {
      let chart = new Chart({

        chart: {
          type: 'boxplot'

        },

        // title: {
        //    text: 'Highcharts Box Plot Example'
        // },

        legend: {
          enabled: false
        },

        xAxis: {
          categories: [obj["Column Name"]],
          title: {
            //   text: 'Experiment No.'
          }
        },
        yAxis: {
          title: {
            text: ''
          }
        },
        exporting: {
          enabled: false
        },
        series: [{
          name: 'Observations',
          type: 'boxplot',
          color: "#34c38f",
          data: [
            // [-102, 51, 102, 153, 306]
            [obj["open"], obj["25%"], obj["50%"], obj["75%"], obj["close"]]
          ],
          tooltip: {
            headerFormat: ''
            // headerFormat: '<em>Experiment No {point.key}</em><br/>'
          }
        },
        {
          name: 'Outliers',
          color: "#34c38f",
          type: 'scatter',
          data: outliers,
          // [ // x, y positions where 0 is the first category
          //   [obj["Column Name"], obj["close"]+10],

          // ],
          marker: {
            fillColor: '#34c38f',
            lineWidth: 1,
            lineColor: "#34c38f"
          },
          tooltip: {
            pointFormat: '{point.y}'
            // pointFormat: 'Observation: {point.y}'
          },

        }]

      });
      this.chart = chart;


      // this.boxplotChartexpand = {
      //   series: [
      //     {
      //       name: "candle",
      //       data: 
      //       [
      //         {
      //           x: new Date(1538778600000),
      //           y: [obj["open"], obj["25%"], obj["75%"], obj["close"]]
      //         },
      //         {
      //           x: new Date(1538780400000),
      //           y: [obj["open"], obj["25%"], obj["50%"], obj["75%"]]
      //         },
      //         {
      //           x:new Date(1538780400000),
      //           y: [obj["close"], obj["25%"], obj["50%"], obj["75%"]]
      //         },
      //         {
      //           x: new Date(1538784000000),
      //           y: [obj["25%"], obj["open"], obj["close"], obj["75%"]]
      //         }


      //       ]
      //     }
      //   ],
      //   chart: {
      //     type: "candlestick",
      //     height: '500px'
      //   },
      //   title: {
      //     text: "CandleStick Chart",
      //     align: "left"
      //   },
      //   xaxis: {
      //     type: "datetime"
      //   },
      //   yaxis: {
      //     tooltip: {
      //       enabled: true
      //     }
      //   }
      // };

      this.hideboxplot = false
    }
    else {
      this.hideboxplot = true;
    }
    this.modalService.open(centerDataModal, { centered: true, windowClass: 'modal-holder' });
  }
}