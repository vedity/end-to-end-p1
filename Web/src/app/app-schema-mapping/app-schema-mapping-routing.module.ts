import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LayoutComponent } from '../layouts/layout.component';
import { CreateSchemaMappingComponent } from './create-schema-mapping/create-schema-mapping.component';

const routes: Routes = [
  { path: '', redirectTo: 'project' },
  {path: 'create', component: CreateSchemaMappingComponent},

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})

export class AppSchemaMappingRoutingModule { }
// canActivate: [AuthGuard]
