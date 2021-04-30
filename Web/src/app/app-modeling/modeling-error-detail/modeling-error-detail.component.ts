import { Component, ErrorHandler, Input, OnInit } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ModelingTypeApiService } from '../modeling-type.service';

@Component({
  selector: 'app-modeling-error-detail',
  templateUrl: './modeling-error-detail.component.html',
  styleUrls: ['./modeling-error-detail.component.scss']
})
export class ModelingErrorDetailComponent implements OnInit {

  @Input() public experiment_id: any;
  @Input() public model_type: any;
  constructor(public router: Router, public apiservice: ModelingTypeApiService, public toaster: ToastrService, private sanitizer: DomSanitizer) { }
  ngOnInit(): void {
    this.getModelFailedReason();
  }

  getModelFailedReason(){
    this.apiservice.getModelFailedReason(this.experiment_id).subscribe(
      logs=>this.successHnadler(logs),
      error=>this.errorHandler(error)
    )
  }

  errorResponse="";
  successHnadler(data){
    if(data.status_code=="200"){
      this.errorResponse=data.response;
      console.log(this.errorResponse);
      
    }
    else{
      this.errorHandler(data);
    }
  }

  filename="";
  fileUrl:any;
  download(){
    const data =JSON.stringify(this.errorResponse);
    var date=new Date();
    this.filename='error_'+date.getTime()+'.json';
    var uri = this.sanitizer.bypassSecurityTrustUrl("data:application/json;charset=UTF-8," + encodeURIComponent(data));
    this.fileUrl = uri;
      setTimeout(() => {
      $("#download-error")[0].click();
      }, 30);
  }

  errorHandler(error) {
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }

}
