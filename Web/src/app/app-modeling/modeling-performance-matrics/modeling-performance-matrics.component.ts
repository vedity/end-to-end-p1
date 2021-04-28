import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-performance-matrics',
  templateUrl: './modeling-performance-matrics.component.html',
  styleUrls: ['./modeling-performance-matrics.component.scss']
})
export class ModelingPerformanceMatricsComponent implements OnInit {
  @Input() public experiment_id: any;
  responsedata: any;

  expandclass:any = "";
  public lineColumAreaChart: any;
  public chartOptions: any;

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
    this.getPerformanceMatrics();
    this.getConfusionMatrics();
  }

  getPerformanceMatrics() {
    this.apiservice.getPerformanceMatrics(this.experiment_id).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));
  }

  successHandler(data) {
    if (data.status_code == "200") {
      this.responsedata = data.response;
      // console.log(this.responsedata);
      // this.toaster.success(data.error_msg, 'Success');
      this.lineColumAreaChart = {
        series: [
          {
            name: "Likes",
            data: [4, 3, 10, 9, 29, 19, 22, 9, 12, 7, 19, 5, 13, 9, 17, 2, 7, 5]
          }
        ],
        chart: {
          height: 300,
          type: "line"
        },
        stroke: {
          width: 7,
          curve: "smooth"
        },
        xaxis: {
          type: "datetime",
          categories: [
            "1/11/2000",
            "2/11/2000",
            "3/11/2000",
            "4/11/2000",
            "5/11/2000",
            "6/11/2000",
            "7/11/2000",
            "8/11/2000",
            "9/11/2000",
            "10/11/2000",
            "11/11/2000",
            "12/11/2000",
            "1/11/2001",
            "2/11/2001",
            "3/11/2001",
            "4/11/2001",
            "5/11/2001",
            "6/11/2001"
          ]
        },
        title: {
          text: "Social Media",
          align: "left",
          style: {
            fontSize: "16px",
            color: "#666"
          }
        },
        fill: {
          type: "gradient",
          gradient: {
            shade: "dark",
            gradientToColors: ["#34c38f"],
            shadeIntensity: 1,
            type: "horizontal",
            opacityFrom: 1,
            opacityTo: 1,
            stops: [0, 100, 100, 100]
          }
        },
        markers: {
          size: 4,
          colors: ["#FFA41B"],
          strokeColors: "#fff",
          strokeWidth: 2,
          hover: {
            size: 7
          }
        },
        yaxis: {
          min: -10,
          max: 40,
          title: {
            text: "Engagement"
          }
        }
      };
     

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
          height: 300,
        
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
                  color: "#34c38f"
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
    else {
      this.errorHandler(data);
    }
  }

  getConfusionMatrics(){
 this.apiservice.getConfusionMatrics(this.experiment_id).subscribe(
  logs => this.confusionMatricsSuccessHandler(logs),
  error => this.errorHandler(error));
  }

  matricsdata:any;
  confusionMatricsSuccessHandler(data){
    if(data.status_code=="200"){
      this.matricsdata=data.response;
      console.log(this.matricsdata);
    }
    else{
      this.errorHandler(data);
    }
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

  errorHandler(error) {
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }
}
