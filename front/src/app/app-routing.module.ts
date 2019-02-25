import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ManageUsersComponent } from './manage_users/manage_users.component';
import { LoginComponent } from './login/login.component';
import { AuthGuard, LoggedIn } from './services/auth.service';

const routes: Routes = [
  { path: 'home', component: HomeComponent, canActivate: [AuthGuard] },
  { path: 'users', component: ManageUsersComponent, canActivate: [AuthGuard]},
  { path: 'login', component: LoginComponent, canActivate: [LoggedIn]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
