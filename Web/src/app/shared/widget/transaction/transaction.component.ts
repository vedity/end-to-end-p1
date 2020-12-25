import { Component, OnInit, Input } from '@angular/core';

import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-transaction',
  templateUrl: './transaction.component.html',
  styleUrls: ['./transaction.component.scss']
})
export class TransactionComponent implements OnInit {

  // @Input() transactions: Array<{
  // id?: string;
  // index?: number,
  // name?: string,
  // date?: string,
  // total?: string,
  // status?: string,
  // payment?: string[],
  // }>;
  @Input() transactions: any;
  keys: any;
  values: any;
  finaldisplaykey: any;
  finaldisplayvalue: any;
  constructor(private modalService: NgbModal) { }

  ngOnInit() {
    console.log(this.transactions);
    
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
  }

  /**
  * Open modal
  * @param content modal content
  */
  openModal(content: any) {
    this.modalService.open(content, { centered: true });
  }

}