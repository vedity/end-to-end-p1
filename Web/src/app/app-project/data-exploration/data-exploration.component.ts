import { Component, ErrorHandler, Input, OnInit } from '@angular/core';
import { arrayToHash } from '@fullcalendar/core/util/object';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ToastrService } from 'ngx-toastr';
import { DataExplorationApiService } from '../data-exploration.service';

@Component({
  selector: 'app-data-exploration',
  templateUrl: './data-exploration.component.html',
  styleUrls: ['./data-exploration.component.scss']
})
export class DataExplorationComponent implements OnInit {

  constructor(public apiService: DataExplorationApiService, public toaster: ToastrService,private modalService: NgbModal) { }
  @Input() public dataset_id: any;
  @Input() public title: any;
  @Input() public project_id: any
  loaderdiv=false;
  displaytitle = "false";
  exploredData: any = [];
  finaldata:any=[];

  columnlabelChart: any;
  columnlabelChartexpand:any;
 animation = "progress-dark";
 theme = {
     'border-radius': '5px',
     'height': '40px',
     'background-color': ' rgb(34 39 54)',
     'border': '1px solid #32394e',
     'animation-duration': '20s'

 };
 displayselectedtitle="Continous";
  ngOnInit(): void {
this.loaderdiv=true;
    this.columnlabelChart=  {
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
          padding :{
              left:0,
              right:0,
              top:0,
              bottom:0
  
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



  continuousexploredata:any;
  categoricalexploredata:any;
  successHandler(logs) {

      if(logs.status_code=="200"){
        console.log(logs.response);
        this.exploredData = logs.response;
       var data= this.groupBy(this.exploredData,"Datatype");
       this.continuousexploredata=data["Continious"];
       this.categoricalexploredata=data["Categorical"];
       console.log(this.continuousexploredata);
       console.log(this.categoricalexploredata);
       this.loaderdiv=false;

        this.finaldata=logs.response;
      }
  else{
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
    this.loaderdiv=false;
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      console.log(error);
      this.toaster.error('Something went wrong', 'Error');
    }
  }

  modeltitle:any;
  centerModal(centerDataModal: any,obj) {
    this.modeltitle=obj["Column Name"];
    console.log(obj);
    
    this.columnlabelChartexpand = {
      chart: {
          height:'500px',
          width: '100%',
          type: 'bar',
          // offsetX: 0,
          // offsetY: 0,
          toolbar: {
              show: true
          },
      },
      dataLabels: {
          enabled: false
      },
      colors: ['#34c38f'],
      series: [{
          data: obj["Plot Values"][1]
      }],
      xaxis: {
          categories: obj["Plot Values"][0],
          position: 'bottom',
      },
      yaxis: {
         // categories: obj["Plot Values"][0],
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
    this.modalService.open(centerDataModal, { centered: true,windowClass:'modal-holder' });
  }
}


