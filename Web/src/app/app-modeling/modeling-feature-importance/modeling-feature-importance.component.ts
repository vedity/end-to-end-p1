import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-feature-importance',
  templateUrl: './modeling-feature-importance.component.html',
  styleUrls: ['./modeling-feature-importance.component.scss']
})
export class ModelingFeatureImportanceComponent implements OnInit {
  public barChart: any;
  public chartOptions:any;
  @Input() public experiment_id: any;
  @Input() public model_type: any;
  
  responsedata:any;
  searchdata:any;
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

    this.getFutureImportance();
   
  }
  
  getFutureImportance() {
    this.apiservice.getFeatureImportance(this.experiment_id).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error));
  }

  successHandler(data) {
    if (data.status_code == "200") {
      this.responsedata = data.response;
      this.searchdata=data.response;
      this.getPDPCurve(this.responsedata.features_name[0],0);
      $("."+this.responsedata.features_name[0]).addClass('selected');
      // this.barChart = {
      //   chart: {
      //     height: 400,
      //     type: 'bar',
      //     toolbar: {
      //       show: false
      //     }
      //   },
      //   plotOptions: {
      //     bar: {
      //       horizontal: true,
      //     }
      //   },
      //   dataLabels: {
      //     enabled: false
      //   },
      //   series: [{
      //     data: this.responsedata.norm_importance
      //   }],
      //   colors: ['#34c38f'],
      //   xaxis: {
      //     // tslint:disable-next-line: max-line-length
      //     categories: this.responsedata.features_name,
      //   },
      //   grid: {
      //     borderColor: '#f1f1f1'
      //   },
      // };
      // this.toaster.success(data.error_msg, 'Success');
    }
    else {
      this.errorHandler(data);
    }
  }

  isChartLoaded=false;
  currentFeature:any;
  currentIndex:any;
  getPDPCurve(feature,i){
    this.isChartLoaded=true;
    this.currentFeature=feature;
    this.currentIndex=i;
    this.apiservice.getPDPCurve(this.experiment_id,1,feature,this.selectedClass).subscribe(
      logs=>this.successPDPCurve(logs,feature,i),
      error=>this.errorHandler(error)
    )
  }

  resetChart(item){
    this.selectedClass=item;
    this.getPDPCurve(this.currentFeature,this.currentIndex);
  }

  public radioClassList:any=[];
  public selectedClass:any=''; 
  successPDPCurve(data,feature,i){
    console.log(i);
    
    $(".filterli").removeClass("selected");
    $(".filterli_"+i).addClass("selected");
    
    if(data.status_code=="200"){
      let yaxistitle=''
      if(data.response.classes.length==0){
        yaxistitle=data.response.target_feature[0]
      }
      if(data.response.classes.length==1)
      {
        yaxistitle=data.response.classes[0]
      }
      if(data.response.classes.length>1)
      {
        yaxistitle=data.response.classes[0];
        this.radioClassList=data.response.classes;
        if(this.selectedClass=='')
        this.selectedClass=data.response.classes[0];
        yaxistitle=this.selectedClass;

      }

      this.chartOptions = {
        series: [
          {
            name: "pdp_values",
            data: data.response.pdp_values
          }
        ],
        chart: {
          height: 430,
          type: "line",
          zoom: {
            enabled: false
          },
          toolbar: {
            show: false
          }
        },
        dataLabels: {
          enabled: false
        },
        colors: ['#008ffb'],
        stroke: {
          curve: "smooth"
        },
        title: {
          text: "PDP Curve",
          align: "left"
        },
        xaxis: {
         
          title:{
            text:feature
          },
          categories: data.response.feature_values,
          labels: {
            show: true,
            formatter: function(value){
              console.log(value);
              if(value)
              return value.toFixed(2).toString();
              else
              return value
            }
          },
        },
        yaxis: {
          title:{
            text:"prediction for "+yaxistitle
          }
        }
      };
      this.isChartLoaded=false;
    }
    else{
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

  filterdata(search) {
    var result = this.searchdata.features_name.filter(function (element) {
      var display = $("."+element).text().toLowerCase().includes(search);
      $("."+element).prop('hidden',!display)
    })
    
   // this.responsedata = result;
  }
}
