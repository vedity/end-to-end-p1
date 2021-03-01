import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ToastrService } from 'ngx-toastr';
import { DataExplorationApiService } from '../data-exploration.service';
@Component({
  selector: 'app-data-cleanup',
  templateUrl: './data-cleanup.component.html',
  styleUrls: ['./data-cleanup.component.scss']
})
export class DataCleanupComponent implements OnInit {

  constructor(public apiService: DataExplorationApiService, public toaster: ToastrService, private modalService: NgbModal, public router: Router) { }
  @Input() public dataset_id: any;
  @Input() public title: any;
  @Input() public project_id: any
  loaderdiv = false;
  displaytitle = "false";
  errorStatus = true;
 
  animation = "progress-dark";
  theme = {
    'border-radius': '5px',
    'height': '40px',
    'background-color': ' rgb(34 39 54)',
    'border': '1px solid #32394e',
    'animation-duration': '20s'
  };

  ngOnInit(): void {

  }


  successHandler(logs) {
    this.loaderdiv = false;
  }

  errorHandler(error) {
    this.loaderdiv = false;
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }

  

  // gotoModeling() {
  // //   let user=localStorage.getItem("currentUser")
  // //   //console.log(user);
  // //   this.data.project_id=this.project_id;
  // //   this.data.dataset_id=this.dataset_id;
  // //   this.data.user_id=JSON.parse(user).id;
  // //   console.log(this.data);
  // //   //localStorage.setItem("Modeling",JSON.stringify(this.data));
  // //  // this.data.model_mode="auto";
  // //   this.router.navigate(["modeling"]);

  // }

  // smallModal(modelingmodal: any) {
  //   this.modalService.open(modelingmodal, { size: 'md', windowClass: 'modal-holder', centered: true });
  // }
}