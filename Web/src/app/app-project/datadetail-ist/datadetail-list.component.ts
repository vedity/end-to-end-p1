import { Component, Input, OnInit, SimpleChanges, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Subject } from 'rxjs';
import { DataTableDirective } from 'angular-datatables';

import { ProjectApiService } from '../project-api.service';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-datadetail-list',
    templateUrl: './datadetail-list.component.html',
    styleUrls: ['./datadetail-list.component.scss']
})
export class DatadetailListComponent implements OnInit {
    @Input() public columnlist: any;
    @Input() public title: any;
    @Input() public dataset_id: any;
    

    @ViewChild(DataTableDirective, { static: false })
    datatableElement: DataTableDirective;
    dtOptions: DataTables.Settings = {};

    animation = "progress-dark";
    theme = {
        'border-radius': '5px',
        'height': '40px',
        'background-color': ' rgb(34 39 54)',
        'border': '1px solid #32394e',
        'animation-duration': '20s'

    };
    contentloaded = false;
    filter: boolean = true;
    dtTrigger: Subject<any> = new Subject<any>();
    constructor(public apiService: ProjectApiService, public router: Router, private toaster: ToastrService, private http: HttpClient) { }
    transactions: any;
    thead="";
    ngOnChanges(changes: SimpleChanges) {
        console.log(changes);
      this.columnlist=changes.columnlist.currentValue;
      console.log(this.columnlist);
  
    this.columnlist.forEach(element => {
       this.thead="<th>"+element.data+"</th>"
    });
   // $(".thead").html(thead);
    }

    ngOnInit(): void {
        const that = this;
        this.dtOptions = {
            pageLength: 10,
            serverSide: true,
            processing: true,
            ajax: (dataTablesParameters: any, callback) => {
                that.http
                    .post<any>(
                        'http://127.0.0.1:8000/mlaas/ingest/data_detail/?dataset_id='+this.dataset_id,
                        dataTablesParameters, {}
                    ).subscribe(resp => {
                        this.transactions = resp.data;
                        console.log(this.transactions);
                       
                            callback({
                                recordsTotal: resp.recordsTotal,
                                recordsFiltered: resp.recordsFiltered,
                                data: []
                            });
                        this.contentloaded=true;
                    });
            },
        };
    }

    displayfilter() {
        this.filter = !this.filter;
        $('.filter').val('').trigger('change');
        // elem.value += ' NEW';
    }
}