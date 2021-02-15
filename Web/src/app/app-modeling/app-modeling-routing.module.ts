import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ModelingTypeComponent } from './modeling-type/modeling-type.component';


const routes: Routes = [
   { path: '', redirectTo: 'type' },
  { path: 'type', component: ModelingTypeComponent },
];
@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})

export class AppModelingRoutingModule { }