import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-comparison-graph',
  templateUrl: './modeling-comparison-graph.component.html',
  styleUrls: ['./modeling-comparison-graph.component.scss']
})
export class ModelingComparisonGraphComponent implements OnInit {

  @Input() public compareIds: any;
  @Input() public model_type: any;
  public lineColumAreaChart: any;
  public linechart:any;
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
    this.getComparisonGraph();
    console.log(this.model_type);
    
  }

  getComparisonGraph() {
    this.apiservice.compareExperimentgraph("[" + this.compareIds + "]").subscribe(
      logs => this.manageGraphCompareExperiment(logs),
      error => this.errorHandler(error)
    )
  }

  comparegraphdata: any;
  manageGraphCompareExperiment(data) {
    if (data.status_code == "200") {
      this.comparegraphdata = data.response;
      if (this.model_type == "Classification") {
        this.drawColumnChart();
      }
      else {
        this.drawLineChart();
      }
    }
    else {
      this.errorHandler(data);
    }

  }

  isChart=false;
  drawColumnChart() {
  this.isChart=false;

    let series = [];
    let makrkerssize = []
    series.push({ name: "ACTUAL", data: this.comparegraphdata.actual });
    makrkerssize.push(2);
    this.comparegraphdata.predicted.forEach(element => {
      series.push({ name: element.exp_name, data: element.values });
      makrkerssize.push(0);

    });

    this.lineColumAreaChart = {
      chart: {
        height: 450,
        type: 'line',
        stacked: false,
        toolbar: {
          show: false
        }
      },
      stroke: {
        width: [2, 2, 4],
      },
      //colors: ['#f46a6a', '#34c38f'],
      series: series,
      fill: {
        // opacity: [0.85, 1],
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
      labels: this.comparegraphdata.index,
      // ['01/01/2003', '02/01/2003', '03/01/2003', '04/01/2003', '05/01/2003', '06/01/2003', '07/01/2003', '08/01/2003', '09/01/2003', '10/01/2003', '11/01/2003'],
      markers: {
        size: makrkerssize
      },
      legend: {
        offsetY: 5,
      },
      xaxis: {
        //type: 'datetime',
      },
      yaxis: {
        // title: {
        //   text: 'Points',
        // },
      },
      tooltip: {
        shared: true,
        intersect: false,
        y: {
          formatter(y) {
            if (typeof y !== 'undefined') {
              return y.toFixed(0);
            }
            return y;
          }
        }
      },
      grid: {
        borderColor: '#f1f1f1'
      }
    };
    this.isChart=true;
  }

  drawLineChart() {
    this.isChart=false;
    let series = [];
    let makrkerssize = []
    series.push({ name: "ACTUAL", data: this.comparegraphdata.actual });
    makrkerssize.push(2);
    this.comparegraphdata.predicted.forEach(element => {
      series.push({ name: element.exp_name, data: element.values });
      makrkerssize.push(0);

    });
    this.linechart = {
      series: series,
      chart: {
        id: "chart2",
        type: "line",
        height: 350,
        toolbar: {
          show: true
        }
      },
     // colors: ['#34c38f','#c3c3c3'],
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
    this.isChart=true;
  }

  errorHandler(error) {
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }



}
