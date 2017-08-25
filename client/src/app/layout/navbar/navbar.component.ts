import { Component, OnInit, Injector } from '@angular/core';
import { Router, RouterState, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  public user: Object = null;

  constructor(public router: Router, public active: ActivatedRoute) {
  }

  ngOnInit() {
  }

}
