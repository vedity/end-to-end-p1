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
    this.getConfusionMatrics();
  }

  getConfusionMatrics(){
    this.apiservice.getConfusionMatrics(this.experiment_id).subscribe(
     logs => this.confusionMatricsSuccessHandler(logs),
     error => this.errorHandler(error));
     }
 
  errorHandler(error) {
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
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
  
}
