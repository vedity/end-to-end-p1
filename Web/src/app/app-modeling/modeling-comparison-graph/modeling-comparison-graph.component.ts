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
  public columnlabelChartexpand: any;
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
      series: series,
      xaxis: {
        categories: this.comparegraphdata.key,
        position: 'bottom',
        title: {
          text: 'Categories'
        }
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

      },
      legend: {
        show: true
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
