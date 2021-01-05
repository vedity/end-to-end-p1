import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AuthGuard } from './core/guards/auth.guard';
import { LayoutComponent } from './layouts/layout.component';
import { CyptolandingComponent } from './cyptolanding/cyptolanding.component';

const routes: Routes = [
  { path: 'account', loadChildren: () => import('./account/account.module').then(m => m.AccountModule) },
  // tslint:disable-next-line: max-line-length
  { path: '', component: LayoutComponent, loadChildren: () => import('./app-project/app-project-routing.module').then(m => m.AppProjectRoutingModule), canActivate: [AuthGuard]},
  { path: 'schema', component: LayoutComponent, loadChildren: () => import('./app-schema-mapping/app-schema-mapping-routing.module').then(m => m.AppSchemaMappingRoutingModule), canActivate: [AuthGuard]},
  // { path: '', component: LayoutComponent, loadChildren: () => import('./pages/pages.module').then(m => m.PagesModule), canActivate: [AuthGuard] },
  // { path: 'pages', loadChildren: () => import('./extrapages/extrapages.module').then(m => m.ExtrapagesModule), canActivate: [AuthGuard] },
  // { path: 'dev',component: LayoutComponent, loadChildren: () => import('./dev/dev.module').then(m => m.DevModule), canActivate: [AuthGuard] },
  
  { path: 'crypto-ico-landing', component: CyptolandingComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { scrollPositionRestoration: 'top' })],
  exports: [RouterModule]
})

export class AppRoutingModule { }
// canActivate: [AuthGuard]
