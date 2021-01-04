import { Component, OnInit, Input, ViewChild } from '@angular/core';

import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

import { Subject } from 'rxjs';
import { DataTableDirective } from 'angular-datatables';


@Component({
  selector: 'app-transaction',
  templateUrl: './transaction.component.html',
  styleUrls: ['./transaction.component.scss']
})
export class TransactionComponent implements OnInit {

  @ViewChild(DataTableDirective, {static: false})
  datatableElement: DataTableDirective;
  dtOptions: DataTables.Settings = {};
  filter:boolean=true;
  
  dtTrigger: Subject<any> = new Subject<any>();
  @Input() transactions: any;
  keys: any;
  values: any;
  finaldisplaykey: any;
  finaldisplayvalue: any;
  constructor(private modalService: NgbModal) { }

  ngOnInit() {
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
    setTimeout(() => {
    this.dtTrigger.next();
    }, 10);
  }

  /**
  * Open modal
  * @param content modal content
  */
  openModal(content: any) {
    this.modalService.open(content, { centered: true });
  }

  displayfilter(){
    this.filter=!this.filter;
    $('.filter').val('').trigger('change');
  }

  ngAfterViewInit(): void {
    setTimeout(() => {
    // this.dtTrigger.next();

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
    }, 100);
   
  }

}