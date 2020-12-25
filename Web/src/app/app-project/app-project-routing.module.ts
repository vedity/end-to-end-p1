import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LayoutComponent } from '../layouts/layout.component';
import { ListProjectComponent } from './list-project/list-project.component';
import { ListDatabaseComponent } from './list-database/list-database.component';
import { ListDatadetailComponent } from './list-datadetail/list-datadetail.component';
import { ManageDatasetComponent } from './manage-dataset/manage-dataset.component';
import { UploadDatasetComponent } from './upload-dataset/upload-dataset.component';
import { CreateProjectComponent } from './create-project/create-project.component';
// import { AdvancedSortableDirective } from '../shared/widget/transaction/advanced-sortable.directive';
//import { CyptolandingComponent } from './cyptolanding/cyptolanding.component';

const routes: Routes = [
  { path: '', redirectTo: 'project' },
  { path: 'project', component: ListProjectComponent },
  {path: 'dataset', component: ListDatabaseComponent},
  {path: 'datadetail', component: ListDatadetailComponent},
  {path: 'manage', component: ManageDatasetComponent},
  {path: 'upload', component: UploadDatasetComponent},
  {path: 'create', component: CreateProjectComponent},

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})

export class AppProjectRoutingModule { }
// canActivate: [AuthGuard]
