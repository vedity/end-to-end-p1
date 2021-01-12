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
import { LoaderInterceptorService } from '../core/services/interceptors/loader-interceptor.service';
import { AppProjectRoutingModule } from './app-project-routing.module';
import { ListDatabaseComponent } from './list-database/list-database.component';
import { ListDatadetailComponent } from './list-datadetail/list-datadetail.component';
import { ListProjectComponent } from './list-project/list-project.component';
import { CreateProjectComponent } from './create-project/create-project.component';
import { ManageProjectComponent } from './manage-project/manage-project.component';
import { DetailviewProjectComponent } from './detailview-project/detailview-project.component';
 import { DataTablesModule } from 'angular-datatables';
import { NgxSkeletonLoaderModule } from 'ngx-skeleton-loader';
import { DatadetailListComponent } from './datadetail-ist/datadetail-list.component';
const DEFAULT_PERFECT_SCROLLBAR_CONFIG: PerfectScrollbarConfigInterface = {
  suppressScrollX: true,
  wheelSpeed: 0.3
};

@NgModule({
  declarations: [ListDatabaseComponent,
     ListDatadetailComponent, 
     DatadetailListComponent,
     ListProjectComponent, CreateProjectComponent, ManageProjectComponent, DetailviewProjectComponent],
  imports: [
    CommonModule,
    FormsModule,
    NgbDropdownModule,
    NgbModalModule,
    AppProjectRoutingModule,
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
    PerfectScrollbarModule,
    NgxSkeletonLoaderModule.forRoot(),
    NgbNavModule
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

export class AppprojectModule { }