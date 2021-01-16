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
    // @Input() public columnlist: any;
    @Input() public title: any;
    @Input() public dataset_id: any;
    @Input() public navigate_to: any;


    @ViewChild(DataTableDirective, { static: false })
    datatableElement: DataTableDirective;
    dtOptions: DataTables.Settings = {};
    public columnlist: any;
    nodatafound="";
    filtercolumns;
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
    thead = "";
    dtRendered=false;
    ngOnInit(): void {
        const that = this;
        this.apiService.getColumnList(this.dataset_id).subscribe(
            logs=>{
                this.columnlist=logs.response;
                // this.columnlist.forEach(element => {
                //     filtercolumns[element.data]="";
                // });
            }
        )

        

        this.dtOptions = {
            pageLength: 10,
            serverSide: true,
            //processing: true,
            autoWidth: false,
            ajax: (dataTablesParameters: any, callback) => {
                let filtercolumns={};
                this.columnlist.forEach(element => {
                    filtercolumns[element.data]=$("#"+element.data).val();
                });
               dataTablesParameters.customfilter=filtercolumns;
                this.apiService.getDataDetails(dataTablesParameters,this.dataset_id)
                    .subscribe(resp => {
                        this.transactions = resp.data;
                        if(this.transactions.length==0){
                            this.nodatafound='<tr><td colspan='+this.columnlist.length+' class="no-data-available">No data!</td></tr>';
                            $("#nodatafound").html(this.nodatafound);
                        }
                        callback({
                            recordsTotal: resp.recordsTotal,
                            recordsFiltered: resp.recordsFiltered,
                            data: []
                        });
                        setTimeout(() => {
                             this.contentloaded = true;
                        }, 100);

                    });
            }
        };
       
    }

    onFilterchange(event){
        console.log(event.target.id);
        console.log(event.target.value);
        this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
            dtInstance.draw();
          });
    }

    mapping() {
        this.router.navigate(['schema/create']);
    }

    displayfilter() {
        this.filter = !this.filter;
        $('.filter').val('').trigger('change');
    }
}