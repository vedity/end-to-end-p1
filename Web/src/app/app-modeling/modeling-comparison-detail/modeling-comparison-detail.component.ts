import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-comparison-detail',
  templateUrl: './modeling-comparison-detail.component.html',
  styleUrls: ['./modeling-comparison-detail.component.scss']
})
export class ModelingComparisonDetailComponent implements OnInit {

  @Input() public compareIds: any;
  @Input() public compareExps: any;
  @Input() public model_type: any;
  constructor(public router: Router, public apiservice: ModelingTypeApiService, public toaster: ToastrService) { }
  ngOnInit(): void {
    console.log(this.model_type);
    
   
  }
}
