import { Component, OnInit, ViewChild } from '@angular/core';
import { DataTableDirective } from 'angular-datatables';
import { ApiService } from '../api.service';
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
    constructor(public apiService:ApiService) { }
    transactions: any;
    ngOnInit(): void {
      this.apiService.getDataset().subscribe(
        logs =>{ this.transactions=logs.Data},
        error => console.log(error)
      );
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