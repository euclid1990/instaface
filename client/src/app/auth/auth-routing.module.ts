import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { GuardService, UnguardService } from '../services/guard.service';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { ForgotComponent } from './forgot/forgot.component';
import { ResetComponent } from './reset/reset.component';
import { PasswordComponent } from './password/password.component';
import { AuthComponent } from './auth.component';

const routes: Routes = [
  {
    path: '',
    component: AuthComponent,
    children: [
      {
        path: 'register',
        canActivate: [UnguardService],
        component: RegisterComponent
      },
      {
        path: 'login',
        canActivate: [UnguardService],
        component: LoginComponent
      },
      {
        path: 'logout',
        canActivate: [GuardService],
        component: LogoutComponent
      },
      {
        path: 'forgot',
        canActivate: [UnguardService],
        component: ForgotComponent
      },
      {
        path: 'reset/:token',
        canActivate: [UnguardService],
        component: ResetComponent
      },
      {
        path: 'password',
        canActivate: [GuardService],
        component: PasswordComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AuthRoutingModule { }
