import { Component, OnInit } from '@angular/core';
import { NavtabService } from './navtab.service';

@Component({
  selector: 'app-navtab',
  templateUrl: './navtab.component.html',
  styleUrls: ['./navtab.component.scss'],
  providers: [NavtabService]
})
export class NavtabComponent implements OnInit {
  public showNavtab: boolean = true;

  constructor(private navtabSv: NavtabService) {
  }

  ngOnInit() {
    this.navtabSv.showNavtab$.subscribe((flag: boolean) => {
      this.showNavtab = flag;
    });
  }

}
