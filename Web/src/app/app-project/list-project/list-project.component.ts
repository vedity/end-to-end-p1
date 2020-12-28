import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { HttpClient, HttpParams } from '@angular/common/http';
import { DataTableDirective } from 'angular-datatables';

@Component({
  selector: 'app-list-project',
  templateUrl: './list-project.component.html',
  styleUrls: ['./list-project.component.scss']
})
export class ListProjectComponent implements OnInit {

  @ViewChild(DataTableDirective, {static: false})
  datatableElement: DataTableDirective;
  dtOptions: DataTables.Settings = {};
  filter:boolean=true;
  constructor(public router:Router,public http:HttpClient) { }
  transactions: any;
  ngOnInit(): void {
    this.transactions = [
      {
          "project_id": 1,
          "project_name":"Pima Indians diabetes Project",
          "project_desc": "Pima Indians diabetes Data",
          "dataset_status" :0,
          "model_status": 1,
          "deployment_status":  1,
          "user_name":"Neha",
          "dataset_id":  1,
          "created_on": "2020-12-22T09:04:23.923Z",
      },
      {
          "project_id":  2,
          "project_name": "Iris Data Project",
          "project_desc": "Iris Data ",
          "dataset_status":0,
          "model_status":  1,
          "deployment_status": 1,
          "user_name":  "Neha",
          "dataset_id":  2,
          "created_on":  "2020-12-22T09:05:20.359Z"
      },
      {
          "project_id": 3,
          "project_name": "CarPrice Assignment Project",
          "project_desc":  "CarPrice Assignment Data ",
          "dataset_status":  0,
          "model_status":1,
          "deployment_status":  1,
          "user_name":"Rahul",
          "dataset_id":  3,
          "created_on":"2020-12-22T09:06:24.172Z"
      },
      {
          "project_id": 4,
          "project_name": "CC General Project",
          "project_desc": "CC General  Data ",
          "dataset_status":  0,
          "model_status": 1,
          "deployment_status":1,
          "user_name": "Ketan",
          "dataset_id":  4,
          "created_on": "2020-12-22T09:08:34.310Z"
      }
  ];
}

  

  ngAfterViewInit(): void {
    this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
      dtInstance.columns().every(function () {
        const that = this;
        $('input',this.header()).on('keyup change', function () {
          if (that.search() !== this['value']) {
            that
              .search(this['value'])
              .draw();
          }
        });
      });
    });
  }

  displayfilter(){
    this.filter=!this.filter;
    console.log(this.filter);
    $('.filter').val('').trigger('change');
   // elem.value += ' NEW';
  }

  create(){
    this.router.navigate(['create']);
  }


  getUserNumber(): Observable<any> {
    return this.http.get<any>("http://127.0.0.1:8000/mlaas/ingest/create_project");
  }
}