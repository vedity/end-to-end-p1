import { Component, OnInit, ViewChild } from '@angular/core';
import { DataTableDirective } from 'angular-datatables';

@Component({
    selector: 'app-list-database',
    templateUrl: './list-database.component.html',
    styleUrls: ['./list-database.component.scss']
})
export class ListDatabaseComponent implements OnInit {
    @ViewChild(DataTableDirective, {static: false})
    datatableElement: DataTableDirective;
    dtOptions: DataTables.Settings = {};
    filter:boolean=true;
    constructor() { }
    transactions: any;
    ngOnInit(): void {
        this.transactions = [
            {
                "dataset_id": 1,
                "dataset_name": "Pima Indians diabetes Dataset",
                "file_name": "pima_indians_diabetes_2020_12_22_09_04_23.csv",
                "file_size": "24.05 kb",
                "dataset_table_name": "di_pima_indians_diabetes_2020_12_22_09_04_23_tbl",
                "dataset_visibility": "public",
                "user_name": "Neha",
                "created_on": "2020-12-22T09:04:23.921Z"
            },
            {
                "dataset_id": 2,
                "dataset_name": "Iris Dataset",
                "file_name": "iris_2020_12_22_09_05_20.csv",
                "file_size": "4.7 kb",
                "dataset_table_name": "di_iris_2020_12_22_09_05_20_tbl",
                "dataset_visibility": "public",
                "user_name": "Neha",
                "created_on": "2020-12-22T09:05:20.355Z"
            },
            {
                "dataset_id": 3,
                "dataset_name": "CarPrice Assignment Dataset",
                "file_name": "CarPrice_Assignment_2020_12_22_09_06_24.csv",
                "file_size": "26.72 kb",
                "dataset_table_name": "di_carprice_assignment_2020_12_22_09_06_24_tbl",
                "dataset_visibility": "public",
                "user_name": "Rahul",
                "created_on": "2020-12-22T09:06:24.169Z",
            },
            {
                "dataset_id": 4,
                "dataset_name": "CC General Dataset",
                "file_name": "CC_GENERAL_2020_12_22_09_08_34.csv",
                "file_size": "0.9 Mb",
                "dataset_table_name": "di_cc_general_2020_12_22_09_08_34_tbl",
                "dataset_visibility": "public",
                "user_name": "Ketan",
                "created_on": "2020-12-22T09:08:34.307Z"
            }
        ];
    }

    displayfilter(){
        this.filter=!this.filter;
        console.log(this.filter);
        $('.filter').val('').trigger('change');
       // elem.value += ' NEW';
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
}