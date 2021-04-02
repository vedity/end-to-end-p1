import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';
import { CdkDragDrop, moveItemInArray } from '@angular/cdk/drag-drop';


@Component({
  selector: 'app-modeling-comparison-grid',
  templateUrl: './modeling-comparison-grid.component.html',
  styleUrls: ['./modeling-comparison-grid.component.scss']
})
export class ModelingComparisonGridComponent implements OnInit {

  @Input() public compareIds: any;
  @Input() public model_type: any;
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
   this.getCompareExperimentGrid();
  }

  getCompareExperimentGrid(){
    this.apiservice.compareExperimentgrid("[" + this.compareIds + "]").subscribe(
      logs => this.manageGridCompareExperiment(logs),
      error => this.errorHandler(error)
    )
  }

  comparedata: any;
  manageGridCompareExperiment(data) {
    if (data.status_code == "200") {
      this.comparedata = data.response;
      //   this.modalService.open(modal, { size: 'xl', windowClass: 'modal-holder', centered: true });
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

  // drop(event: CdkDragDrop<string[]>) {
  //   moveItemInArray(this.compareIds, event.previousIndex, event.currentIndex);
  // }

  timePeriods = [
    'Bronze age',
    'Iron age',
    'Middle ages',
    'Early modern period',
    'Long nineteenth century'
  ];

  drop(event: CdkDragDrop<string[]>) {
    moveItemInArray(this.comparedata.responsedata, event.previousIndex, event.currentIndex);
  }

}
