import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-view-detail',
  templateUrl: './modeling-view-detail.component.html',
  styleUrls: ['./modeling-view-detail.component.scss']
})
export class ModelingViewDetailComponent implements OnInit {

  @Input() public experiment_id: any;
  @Input() public model_type: any;
  constructor(public router: Router, public apiservice: ModelingTypeApiService, public toaster: ToastrService) { }
  ngOnInit(): void {
   
  }
}
