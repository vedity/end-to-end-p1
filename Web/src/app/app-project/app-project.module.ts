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
import { ManageSchemaMappingComponent } from './manage-schema-mapping/manage-schema-mapping.component';
import { DetailviewProjectComponent } from './detailview-project/detailview-project.component';
import { DetailviewDatasetComponent } from './detailview-dataset/detailview-dataset.component';
import { DataTablesModule } from 'angular-datatables';
import { NgxSkeletonLoaderModule } from 'ngx-skeleton-loader';
import { CreateSchemaMappingComponent } from './create-schema-mapping/create-schema-mapping.component';
import { DataExplorationComponent } from './data-exploration/data-exploration.component';
import { DataVisualizationComponent } from './data-visualization/data-visualization.component';
import { NgSelectModule } from '@ng-select/ng-select';
import { DataCleanupComponent } from './data-cleanup/data-cleanup.component';
import { ChartModule,HIGHCHARTS_MODULES } from 'angular-highcharts';
import * as more from 'highcharts/highcharts-more.src';
import * as exporting from 'highcharts/modules/exporting.src';
import * as theme from 'highcharts/themes/dark-unica.src';
import { CreateDatasetComponent } from './create-dataset/create-dataset.component';
import { Ng5SliderModule } from 'ng5-slider';
import { ManageDatasetComponent } from './manage-dataset/manage-dataset.component';

const DEFAULT_PERFECT_SCROLLBAR_CONFIG: PerfectScrollbarConfigInterface = {
  suppressScrollX: true,
  wheelSpeed: 0.3
};
@NgModule({
  declarations: [ListDatabaseComponent,
    ListDatadetailComponent,
    ListProjectComponent, 
    CreateProjectComponent, 
    ManageProjectComponent, 
    DetailviewProjectComponent,
    CreateSchemaMappingComponent, 
    DataExplorationComponent, 
    DataVisualizationComponent,
    DataCleanupComponent,
    ManageSchemaMappingComponent,
    CreateDatasetComponent,
    ManageDatasetComponent,
    DetailviewDatasetComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    NgbDropdownModule,
    NgbModalModule,
    AppProjectRoutingModule,
    NgApexchartsModule,
    ChartsModule,
    NgxChartistModule,
    NgxEchartsModule,
    NgSelectModule,
    ReactiveFormsModule,
    DataTablesModule,
    UIModule,
    WidgetModule,
    ChartModule,
    
    FullCalendarModule,
    NgbNavModule,
    NgbTooltipModule,
    PerfectScrollbarModule,
    NgxSkeletonLoaderModule.forRoot(),
    NgbNavModule,
    Ng5SliderModule
  ],
  providers: [
    {
      provide: PERFECT_SCROLLBAR_CONFIG,
      useValue: DEFAULT_PERFECT_SCROLLBAR_CONFIG,
      
    },  { provide: HIGHCHARTS_MODULES, useFactory: () => [ more, exporting ,theme] },
    LoaderService,
    { provide: HTTP_INTERCEPTORS, useClass: LoaderInterceptorService, multi: true }
  ]
})

export class AppprojectModule { }