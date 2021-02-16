import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-view-detail',
  templateUrl: './modeling-view-detail.component.html',
  styleUrls: ['./modeling-view-detail.component.scss']
})
export class ModelingViewDetailComponent implements OnInit {

  constructor(public router: Router, public apiservice: ModelingTypeApiService, public toaster: ToastrService) { }
  selectValue: string[];
  public barChart: any;
  public lineColumAreaChart: any;
  public columnlabelChartexpand: any;
  public simpleline: any;


  ngOnInit(): void {

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
        data: [380, 430, 450, 475, 550, 584, 780, 1100, 1220, 1365]
      }],
      colors: ['#34c38f'],
      xaxis: {
        // tslint:disable-next-line: max-line-length
        categories: ['South Korea', 'Canada', 'United Kingdom', 'Netherlands', 'Italy', 'France', 'Japan', 'United States', 'China', 'Germany'],
      },
      grid: {
        borderColor: '#f1f1f1'
      },
    };

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
        name: 'Team A',
        //   type: 'line',
        data: [23, 11, 50, 70, 13, 56, 37, 78, 44, 22, 30]
      }, {
        name: 'Team B',
        //   type: 'line',
        data: [23, 10, 22, 30, 13, 20, 31, 21, 40, 20, 32]
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
      labels: ['01/01/2003', '02/01/2003', '03/01/2003', '04/01/2003', '05/01/2003', '06/01/2003', '07/01/2003', '08/01/2003', '09/01/2003', '10/01/2003', '11/01/2003'],
      markers: {
        size: [0, 2]
      },
      legend: {
        offsetY: 5,
      },
      xaxis: {
        type: 'datetime',
      },
      yaxis: {
        title: {
          text: 'Points',
        },
      },
      tooltip: {
        shared: true,
        intersect: false,
        y: {
          formatter(y) {
            if (typeof y !== 'undefined') {
              return y.toFixed(0) + ' points';
            }
            return y;
          }
        }
      },
      grid: {
        borderColor: '#f1f1f1'
      }
    };
    this.columnlabelChartexpand = {
      chart: {
        height: '400px',
        width: '100%',
        type: 'bar',
        // offsetX: 0,
        // offsetY: 0,
        toolbar: {
          show: false
        },
        selection: {
          enabled: true
        }
      },
      dataLabels: {
        enabled: false,
      },
      colors: ['#34c38f'],

      series: [{
        name: 'Yearly Income',
        data: [5383083166.0, 2383083166.0, 5383083166.0, 5383083166.0, 4583083166.0, 6783083166.0, 1983083166.0, 2383083166.0, 5383083166.0, 5383083166.0, 3783083166.0, 7889081942.0]
      }],
      xaxis: {
        categories: ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
        position: 'bottom',



      },
      yaxis: {
        categories: [5383083166.0, 2383083166.0, 5383083166.0, 5383083166.0, 4583083166.0, 6783083166.0, 1983083166.0, 2383083166.0, 5383083166.0, 5383083166.0, 3783083166.0, 7889081942.0],
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
        show: true,
        offsetX: 0,
        offsetY: 0,
      }

    };


    this.simpleline = {
      series: [{
        name: "Actual",
        data: [10, 12, 15, 17, 19, 20, 22, 25, 30]
      }, {
        name: "Prediction",
        data: [10, 13, 14, 16, 20, 21, 24, 25, 29]
      }
      ],
      chart: {
        height: 400,
        type: 'line',
        zoom: {
          enabled: false
        }
      },
      dataLabels: {
        enabled: false
      },
      colors: ['#c3c3c3', '#34c38f'],
      stroke: {
        curve: 'straight'
      },
      title: {
        text: 'Product Trends by Month',
        align: 'left'
      },
      // grid: {
      //   row: {
      //     colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
      //     opacity: 0.5
      //   },
      // },
      xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
      }

    };
  }

  classname = "";
  allowExpand() {
    this.classname == '' ? this.classname = 'expand-block' : this.classname = '';
    window.dispatchEvent(new Event('resize'));
  }
}
