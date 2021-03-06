import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';

import { SharedModule } from '../shared/shared.module';
import { LayoutModule } from '../layout/layout.module';
import { DirectivesModule } from '../directives/directives.module';
import { PipesModule } from '../pipes/pipes.module';
import { Api } from '../utils/api';

import { AuthRoutingModule } from './auth-routing.module';
import { AuthComponent } from './auth.component';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { ForgotComponent } from './forgot/forgot.component';
import { ResetComponent } from './reset/reset.component';
import { PasswordComponent } from './password/password.component';

@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    SharedModule,
    LayoutModule,
    DirectivesModule,
    PipesModule,
    AuthRoutingModule
  ],
  declarations: [RegisterComponent, LoginComponent, LogoutComponent, ForgotComponent, ResetComponent, AuthComponent, PasswordComponent],
  providers: [Api]
})
export class AuthModule { }
