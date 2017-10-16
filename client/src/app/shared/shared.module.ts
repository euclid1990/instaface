import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormErrorComponent } from './form-error/form-error.component';
import { FormMessageComponent } from './form-message/form-message.component';
import { PipesModule } from '../pipes/pipes.module';

@NgModule({
  imports: [
    CommonModule,
    PipesModule
  ],
  declarations: [FormErrorComponent, FormMessageComponent],
  exports: [FormErrorComponent, FormMessageComponent]
})
export class SharedModule { }
