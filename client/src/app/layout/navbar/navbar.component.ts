import { Component, OnInit, Injector } from '@angular/core';
import { Router, RouterState, ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  router: Router;
  active: ActivatedRoute;

  constructor(router: Router, active: ActivatedRoute) {
    this.router = router;
    this.active = active;
  }

  ngOnInit() {
  }

}
