import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LayoutModule } from '../layout/layout.module';

import { HomeRoutingModule } from './home-routing.module';
import { HomeComponent } from './home.component';
import { NewsComponent } from './news/news.component';
import { SavedComponent } from './saved/saved.component';

@NgModule({
  imports: [
    CommonModule,
    LayoutModule,
    HomeRoutingModule
  ],
  declarations: [HomeComponent, NewsComponent, SavedComponent]
})
export class HomeModule { }
