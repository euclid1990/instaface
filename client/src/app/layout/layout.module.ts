import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { NavtabComponent } from './navtab/navtab.component';

@NgModule({
  imports: [
    CommonModule,
    RouterModule // RouterModule contains the RouterLink directive. You need to add all modules to imports if you use directives, components, or pipes from these imports.
  ],
  declarations: [NavbarComponent, FooterComponent, NavtabComponent],
  exports: [NavbarComponent, FooterComponent, NavtabComponent]
})
export class LayoutModule { }
