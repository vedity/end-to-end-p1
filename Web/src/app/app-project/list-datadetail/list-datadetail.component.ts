import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Subject } from 'rxjs';
import { DataTableDirective } from 'angular-datatables';

import { ProjectApiService } from '../project-api.service';

@Component({
    selector: 'app-list-datadetail',
    templateUrl: './list-datadetail.component.html',
    styleUrls: ['./list-datadetail.component.scss']
})
export class ListDatadetailComponent implements OnInit {

    @ViewChild(DataTableDirective, { static: false })
    datatableElement: DataTableDirective;
    dtOptions: DataTables.Settings = {


    };
    animation = "progress-dark";
    theme={
        'border-radius': '5px',
        'height': '40px',
        'background-color':' rgb(34 39 54)',
        'border': '1px solid #32394e',
        'animation-duration': '20s'
    
      };
    contentloaded=false;
    filter: boolean = true;
    navigate_to="";
    dtTrigger: Subject<any> = new Subject<any>();
    //   @Input() transactions: any;
    keys: any;
    values: any;
    finaldisplaykey: any;
    finaldisplayvalue: any;
    constructor(public apiService: ProjectApiService, public router: Router, private toaster: ToastrService) { }
    transactions: any;
    title = "Data Detail List";
    ngOnInit() {
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
           var tbody="";
            this.transactions.forEach((element, index) => {
                var obj = element;
                var valueobj = Object.values(obj);
                var val = [];
                tbody=tbody+"<tr>";
                for (let i = 0; i < this.keys.length; i++) {
                    if (valueobj[i]["display"] == "true") {
                        if (index == 0)
                            this.finaldisplaykey.push(this.keys[i]);
                            tbody=tbody+"<td>"+valueobj[i]["values"]+"</td>";
                    }
                }
                tbody=tbody+"</tr>"
            });
            $("#tbody").html(tbody);
            this.rendered();
        }
        else
            this.errorHandler(data);
    }

    errorHandler(error) {
        console.log(error);
        if(error.error_msg)
        this.toaster.error(error.error_msg, 'Error');
        else
        {
          console.log(error);
        this.toaster.error('Something went wrong', 'Error');
        }
      }

    mapping() {
        this.router.navigate(['schema/create']);
    }

    displayfilter() {
        this.filter = !this.filter;
        $('.filter').val('').trigger('change');
        // elem.value += ' NEW';
    }

    rendered() {
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
            setTimeout(() => {
            this.contentloaded=true;
            });

        }, 100);

    }

}