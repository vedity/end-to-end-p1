import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { NgbModalModule } from '@ng-bootstrap/ng-bootstrap';

import { StatComponent } from './stat/stat.component';
import { TransactionComponent } from './transaction/transaction.component';
import { DataTablesModule } from 'angular-datatables';

@NgModule({
  declarations: [StatComponent, TransactionComponent],
  imports: [
    CommonModule,
    NgbModalModule,
    DataTablesModule
  ],
  exports: [StatComponent, TransactionComponent]
})
export class WidgetModule { }
