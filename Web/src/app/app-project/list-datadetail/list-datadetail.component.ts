import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Subject } from 'rxjs';
import { DataTableDirective } from 'angular-datatables';

import { ProjectApiService } from '../project-api.service';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-list-datadetail',
    templateUrl: './list-datadetail.component.html',
    styleUrls: ['./list-datadetail.component.scss']
})
export class ListDatadetailComponent implements OnInit {

    navigate_to="";
    constructor(public apiService: ProjectApiService, public router: Router, private toaster: ToastrService,private http: HttpClient) { }
    title = "Data Detail List";
    dataset_id:any;
    columnlist:any=[];
   async ngOnInit() {
        
        var params = history.state;
        if (params.dataset_id != undefined)
            localStorage.setItem("params", JSON.stringify(params));
        else {
            params = localStorage.getItem("params");
            params = JSON.parse(params);
        }
        if (params.dataset_name != undefined) {
            this.title = params.dataset_name;
        }
        this.navigate_to=params.navigate_to;
        this.dataset_id=params.dataset_id;
       
    }

   
}
