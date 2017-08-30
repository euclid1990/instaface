import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ObjectToArrayPipe } from '../pipes/object-to-array.pipe';
import { PrettyPrintPipe } from './pretty-print.pipe';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [ObjectToArrayPipe, PrettyPrintPipe],
  exports: [ObjectToArrayPipe, PrettyPrintPipe]
})
export class PipesModule { }
