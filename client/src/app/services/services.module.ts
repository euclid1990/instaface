import { NgModule, ModuleWithProviders, APP_INITIALIZER } from '@angular/core';
import { AuthService } from './auth.service';
import { GuardService, UnguardService } from './guard.service';

@NgModule({
  imports: [],
  declarations: [],
  exports: []
})
export class ServicesModule {
  static forRoot(): ModuleWithProviders {
    return {
      ngModule: ServicesModule,
      providers: [
        AuthService,
        GuardService,
        UnguardService
      ]
    };
  }
}
