import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { PerfectScrollbarModule } from 'ngx-perfect-scrollbar';
import { PERFECT_SCROLLBAR_CONFIG } from 'ngx-perfect-scrollbar';
import { PerfectScrollbarConfigInterface } from 'ngx-perfect-scrollbar';

import { NgbNavModule, NgbDropdownModule, NgbModalModule, NgbTooltipModule } from '@ng-bootstrap/ng-bootstrap';
import { NgApexchartsModule } from 'ng-apexcharts';
import { NgxChartistModule } from 'ngx-chartist';

import { ChartsModule } from 'ng2-charts';
import { NgxEchartsModule } from 'ngx-echarts';


import { WidgetModule } from '../shared/widget/widget.module';
import { UIModule } from '../shared/ui/ui.module';

import { FullCalendarModule } from '@fullcalendar/angular';


import { LoaderService } from '../core/services/loader.service';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import {LoaderInterceptorService} from '../core/services/interceptors/loader-interceptor.service';
import { AppSchemaMappingRoutingModule } from './app-schema-mapping-routing.module';
import { DataTablesModule } from 'angular-datatables';
import { CreateSchemaMappingComponent } from './create-schema-mapping/create-schema-mapping.component';
const DEFAULT_PERFECT_SCROLLBAR_CONFIG: PerfectScrollbarConfigInterface = {
  suppressScrollX: true,
  wheelSpeed: 0.3
};

@NgModule({
  declarations: [
    CreateSchemaMappingComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    NgbDropdownModule,
    NgbModalModule,
    AppSchemaMappingRoutingModule,
    NgApexchartsModule,
    ChartsModule,
    NgxChartistModule,
    ReactiveFormsModule,
    DataTablesModule,
    UIModule,
    WidgetModule,
    FullCalendarModule,
    NgbNavModule,
    NgbTooltipModule,
    PerfectScrollbarModule
  ],
  providers: [
    {
      provide: PERFECT_SCROLLBAR_CONFIG,
      useValue: DEFAULT_PERFECT_SCROLLBAR_CONFIG
    },
    LoaderService,
    { provide: HTTP_INTERCEPTORS, useClass: LoaderInterceptorService, multi: true }
  ]
})

export class AppschemamappingModule { }
