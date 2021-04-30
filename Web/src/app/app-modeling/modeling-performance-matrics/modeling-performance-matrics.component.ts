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
  @Input() public model_type: any;
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
console.log(this.model_type);
    
    this.getPerformanceMatrics();
    if(this.model_type=='Classification'){
    this.getConfusionMatrics();
    this.getRocCurve();
    }
    else{
    }
  }

  getPerformanceMatrics() {
    this.apiservice.getPerformanceMatrics(this.experiment_id).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));
  }

  successHandler(data) {
    if (data.status_code == "200") {
      this.responsedata = data.response;
    }
    else {
      this.errorHandler(data);
    }
  }

  getRocCurve(){
    this.apiservice.getRocCurve(this.experiment_id).subscribe(
      logs => this.rocCurveSuccessHandler(logs),
      error => this.errorHandler(error));
  }

  rocCurveSuccessHandler(data){
    if(data.status_code=="200"){
      // let series=this.generateROCData(data.response);
      this.lineColumAreaChart = {
        series: this.generateROCData(data.response),
        chart: {
          id: "chart2",
          type: "line",
          height: 350,
          toolbar: {
            show: true
          }
        },
        stroke: {
          width: 4,
          curve: "smooth"
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
          title:{
            text:'FPR'
          },
          labels: {
            show: true,
            formatter: function(value){
              return value.toFixed(2).toString();
            }
          },
        },
        yaxis: {
          title:{
            text:'TPR'
          },
          labels: {
            show: true,
            formatter: function(value){
              return value.toFixed(2).toString();
            }
          },
        }
      };
    }
    else{
      this.errorHandler(data);
    }
  }

  generateROCData(data){
    var keys=data.classes;
    var xaxis=data.FPR;
    var yaxis=data.TPR;var serieslist=[];
    keys.forEach(element => {
      var x=xaxis[element]
      var y=yaxis[element]
      var series=[]
      x.forEach((elem,index) => {
        series.push([elem, y[index]]);
      });
      serieslist.push({name:element,data:series})
    });
    return serieslist;
  }

  getConfusionMatrics(){
 this.apiservice.getConfusionMatrics(this.experiment_id).subscribe(
  logs => this.confusionMatricsSuccessHandler(logs),
  error => this.errorHandler(error));
  }

  confusionMatricsSuccessHandler(data){
    if(data.status_code=="200"){
      var matricsdata=data.response;
      this.chartOptions = {
        series: this.geneateConfusionmatricsdata(matricsdata),
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
        xaxis:{
          position: 'top',
          title: {
            text: 'Actual',
            offsetY: -65,
          },
          labels: {
            offsetY: 14,
          }
        },
        yaxis:{
          title: {
            text: 'Prediction'
          }
        },
        
        legend: {
          show: false}
          ,
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
    else{
      this.errorHandler(data);
    }
  }

  geneateConfusionmatricsdata(data){
    let serieslist=[];
    data.key_val.forEach((element,index) => {
      let series=[];
      data.key.forEach((elem,i) => {
        series.push({x:elem.toString(),y:element[i]})
      });
      serieslist.push({name: data.key[index],data: series});
    });
    console.log(serieslist);
    let finalserislist=serieslist.reverse();
    return finalserislist;
    
  }

  errorHandler(error) {
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }

  allowExpand(type) {
    if(type=='right')
    this.expandclass==''?this.expandclass='right-expand':this.expandclass='';
    if(type=='left')
    this.expandclass==''?this.expandclass='left-expand':this.expandclass='';
    
    window.dispatchEvent(new Event('resize'));
  }
}
