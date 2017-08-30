import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { FocusDirective } from './focus.directive';


@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [FocusDirective],
  exports: [FocusDirective]
})
export class DirectivesModule { }
