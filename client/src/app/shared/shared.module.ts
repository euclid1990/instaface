import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormErrorComponent } from './form-error/form-error.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [FormErrorComponent],
  exports: [FormErrorComponent]
})
export class SharedModule { }
