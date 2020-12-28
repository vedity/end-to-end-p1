import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { HttpClient, HttpParams } from '@angular/common/http';
import { DataTableDirective } from 'angular-datatables';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-list-project',
  templateUrl: './list-project.component.html',
  styleUrls: ['./list-project.component.scss']
})
export class ListProjectComponent implements OnInit {

  @ViewChild(DataTableDirective, { static: false })
  datatableElement: DataTableDirective;
  dtOptions: DataTables.Settings = {
    
  };
  filter: boolean = true;
  constructor(public router: Router, public http: HttpClient, public apiService: ApiService) { }
  transactions: any;
  ngOnInit(): void {
    this.apiService.getproject().subscribe(
      logs => { this.transactions = logs.Data },
      error => console.log(error)
    );
  }

  ngAfterViewInit(): void {
    this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
      dtInstance.columns().every(function () {
        const that = this;
        $('input', this.header()).on('keyup change', function () {
          if (that.search() !== this['value']) {
            that
              .search(this['value'])
              .draw();
          }
        });
      });
    });
  }

  displayfilter() {
    this.filter = !this.filter;
    console.log(this.filter);
    $('.filter').val('').trigger('change');
  }

  create() {
    this.router.navigate(['create']);
  }

  getUserNumber(): Observable<any> {
    return this.http.get<any>("http://127.0.0.1:8000/mlaas/ingest/create_project");
  }
}