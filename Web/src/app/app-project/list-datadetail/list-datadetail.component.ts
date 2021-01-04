import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Subject } from 'rxjs';
import { DataTableDirective } from 'angular-datatables';

import { ApiService } from '../api.service';

@Component({
    selector: 'app-list-datadetail',
    templateUrl: './list-datadetail.component.html',
    styleUrls: ['./list-datadetail.component.scss']
})
export class ListDatadetailComponent implements OnInit {

    @ViewChild(DataTableDirective, { static: false })
    datatableElement: DataTableDirective;
    dtOptions: DataTables.Settings = {};
    filter: boolean = true;

    dtTrigger: Subject<any> = new Subject<any>();
    //   @Input() transactions: any;
    keys: any;
    values: any;
    finaldisplaykey: any;
    finaldisplayvalue: any;
    constructor(public apiService: ApiService, public router: Router, private toaster: ToastrService) { }
    transactions: any;

    ngOnInit() {
        var params = history.state;
        if (params.user_name != undefined)
            localStorage.setItem("params", JSON.stringify(params));
        else {
            params = localStorage.getItem("params");
            params = JSON.parse(params);
        }
        this.apiService.getDataDetails(params).subscribe(
            logs => this.successHandler(logs),
            error => this.errorHandler(error)
        );
    }


    successHandler(data) {
        if (data.status_code == "200") {
            this.transactions = data.response;

            this.keys = [];
            this.keys = Object.keys(this.transactions[0]);
            this.finaldisplaykey = [];
            this.finaldisplayvalue = [];
            this.transactions.forEach((element, index) => {
                var obj = element;
                var valueobj = Object.values(obj);
                var val = [];
                for (let i = 0; i < this.keys.length; i++) {
                    if (valueobj[i]["display"] == "true") {
                        if (index == 0)
                            this.finaldisplaykey.push(this.keys[i]);
                        val.push(valueobj[i]["values"]);
                    }
                    if (i == this.keys.length - 1) {
                        this.finaldisplayvalue.push(val);
                        val = [];
                    }
                }
            });



           // this.toaster.success('Data Load Successfully', 'Success');
        }
        else
            this.errorHandler(data);
    }

    errorHandler(error) {
        console.log(error);
        this.toaster.error('Something went wrong', 'Error');
    }

    mapping() {
        this.router.navigate(['schema/create']);
    }

    displayfilter() {
        this.filter = !this.filter;
        $('.filter').val('').trigger('change');
        // elem.value += ' NEW';
    }

    ngAfterViewInit(): void {
        setTimeout(() => {
            this.dtTrigger.next();

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
        }, 800);

    }

}