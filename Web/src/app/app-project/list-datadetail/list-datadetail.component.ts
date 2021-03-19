import { Component, HostListener, Input, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Subject } from 'rxjs';
import { DataTableDirective } from 'angular-datatables';
import { HttpClient } from '@angular/common/http';
import { SchemaMappingApiService } from '../schema-mapping-api.service';
@Component({
    selector: 'app-list-datadetail',
    templateUrl: './list-datadetail.component.html',
    styleUrls: ['./list-datadetail.component.scss']
})
export class ListDatadetailComponent implements OnInit {
    @Input() public title: any;
    @Input() public dataset_id: any;
    @Input() public navigate_to: any;
    @Input() public displaytitle: any;
    @Input() public schema_id:any;
    @ViewChild(DataTableDirective, { static: false })
    datatableElement: DataTableDirective;
    dtOptions: DataTables.Settings = {};
    public columnlist: any;
    nodatafound = "";
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
    constructor(public apiService: SchemaMappingApiService, public router: Router, private toaster: ToastrService, private http: HttpClient) { }
    transactions: any;
    thead = "";
    dtRendered = false;

    @HostListener('window:resize', ['$event'])
	onResize(event) {
    if (this.datatableElement.dtInstance) {
      this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
        dtInstance.columns.adjust().draw();
      })
    }
	}

    ngOnInit(): void {
        const that = this;
        this.apiService.getColumnList(this.dataset_id,this.schema_id).subscribe(
            logs => {
                this.columnlist = logs.response;
            }
        )
        this.dtOptions = {
            pageLength: 10,
            serverSide: true,
             scrollCollapse: true,
             scrollX: true,
            scrollY: "calc(100vh - 450px)",
             //autoWidth:true,
            ajax: (dataTablesParameters: any, callback) => {
                let filtercolumns = {};
                this.columnlist.forEach((element, index) => {
                    filtercolumns[element.data] = $("#col-" + index).val();
                });
                dataTablesParameters.customfilter = filtercolumns;
                this.apiService.getDataDetails(dataTablesParameters, this.dataset_id,this.schema_id)
                    .subscribe(resp => {
                        this.transactions = resp.data;
                        if (this.transactions.length == 0) {
                            this.nodatafound = '<tr><td></td><td colspan="6" class="no-data-available">No data available in table</td></tr>';
                            $("#nodatafound").html(this.nodatafound);
                        }
                        callback({
                            recordsTotal: resp.recordsTotal,
                            recordsFiltered: resp.recordsFiltered,
                            data: []
                        });
                    });
            },
            drawCallback: (settings) => {
                setTimeout(() => {
                    $(".main-datatable").trigger('resize')
                });
            },
            initComplete: (settings, json) => {
                setTimeout(() => {
                    $(".main-datatable").trigger('resize')
                   setTimeout(() => {
                    this.contentloaded = true;
                   }, 100); 
                });
              
            }
        };
// setTimeout(() => {
//     // this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
//     //     dtInstance.draw();
//     // });
// }, 1000);
    }


    onFilterchange(event) {
        this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
            dtInstance.draw();
        });
    }

    mapping() {
        this.router.navigate(['schema/create']);
    }

    displayfilter() {
        this.filter = !this.filter;
        $('.filter').val('').trigger('keyup');
        this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
            dtInstance.draw();
        });
    }
}