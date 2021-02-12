import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ListProjectComponent } from './list-project/list-project.component';
import { ListDatabaseComponent } from './list-database/list-database.component';
import { ListDatadetailComponent } from './list-datadetail/list-datadetail.component';
import { ManageProjectComponent } from './manage-project/manage-project.component';
import { DetailviewProjectComponent } from './detailview-project/detailview-project.component';
import { CreateProjectComponent } from './create-project/create-project.component';
import { ManageSchemaMappingComponent } from './manage-schema-mapping/manage-schema-mapping.component';

const routes: Routes = [
  { path: '', redirectTo: 'project' },
  { path: 'manage', component: ListProjectComponent },
  {path: 'dataset', component: ListDatabaseComponent},
  {path: 'datadetail', component: ListDatadetailComponent},
  {path: 'project', component: ManageProjectComponent},
  {path: 'upload', component: DetailviewProjectComponent},
  {path: 'create', component: CreateProjectComponent},
  {path: 'schema', component: ManageSchemaMappingComponent},
];
@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})

export class AppProjectRoutingModule { }