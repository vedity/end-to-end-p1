import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ActivatedRouteSnapshot, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { SchemaMappingApiService } from '../schema-mapping-api.service';
@Component({
  selector: 'app-manage-schema-mapping',
  templateUrl: './manage-schema-mapping.component.html',
  styleUrls: ['./manage-schema-mapping.component.scss']
})
export class ManageSchemaMappingComponent implements OnInit {
  displaytitle = false;
  schemamapping=false;
  navigate_to = "";
  activeId=1;
  constructor(public apiService: SchemaMappingApiService,public activatedroute: ActivatedRoute, public router: Router, private toaster: ToastrService, private http: HttpClient) { }
  title = "Data Detail List";
  dataset_id: any;
  columnlist: any = [];
  project_id: any;
  schema_id:any;
  activatedroutedata:any;
  async ngOnInit() {
   

    var params = history.state;
    let navigate=params.navigate_to;
    if (params.dataset_id != undefined)
      localStorage.setItem("params", JSON.stringify(params));
    else {
      params = localStorage.getItem("params");
      params = JSON.parse(params);
    }
    if (params.dataset_name != undefined) {
      this.title = params.dataset_name;
    }
    this.navigate_to = params.navigate_to;
    this.project_id = params.project_id;
    if (this.navigate_to == "/dataset") {
      this.displaytitle = true;
    }
    if(this.navigate_to==""){
    //  this.displaytitle=true;
      this.schemamapping=true;
      this.activeId=2
    }
    if(params.navigate=="explore"){
      //  this.displaytitle=true;
        this.activeId=3
      }
      
    if(navigate=="modeling"){
      this.activeId=5;
    }
    this.dataset_id = params.dataset_id;
    this.schema_id=params.schema_id;

    
    this.activatedroute.data.subscribe(data => {
      this.activatedroutedata=data;
      if(this.activatedroutedata.Activeid!=undefined)
      this.activeId=this.activatedroutedata.Activeid;
    })
  }
}