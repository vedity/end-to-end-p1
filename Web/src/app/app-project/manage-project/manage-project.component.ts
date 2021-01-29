import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ProjectApiService } from '../project-api.service';

@Component({
  selector: 'app-manage-project',
  templateUrl: 'manage-project.component.html',
  styleUrls: ['./manage-project.component.scss']
})
export class ManageProjectComponent implements OnInit {
  active = 1;
  classname = "";
  transactions: any;
  currentDate:any;
  
  constructor(public router: Router, public toaster: ToastrService, public apiService: ProjectApiService) { }

  ngOnInit() {
    this.currentDate=new Date();
    
  console.log(this.currentDate);

    this.getactivivtyTimeline();
  }

  getactivivtyTimeline() {
    this.apiService.getActivityTimeline().subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error)
    );
  }
   keys:any=[];
  successHandler(data) {
    if (data.status_code == "200") {
      console.log(data.response);
      this.transactions = this.groupBy(data.response, 'date');
      console.log(this.transactions);
      this.keys=Object.keys(this.transactions);
    }
    else {
      this.transactions = []
    }
  }

  groupBy(xs, key) {
    return xs.reduce(function (rv, x) {
      (rv[x[key]] = rv[x[key]] || []).push(x);
      return rv;
    }, {});
  };


  errorHandler(error) {
    console.log(error);
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      console.log(error);
      this.toaster.error('Something went wrong', 'Error');
    }
  }



  create() {
    this.router.navigate(['create']);
  }

  toggleTimeline() {
    if (this.classname == "")
      this.classname = "red";
    else
      this.classname = "";
  }
}
