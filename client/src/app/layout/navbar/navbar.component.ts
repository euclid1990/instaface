import { Component, OnInit, Injector } from '@angular/core';
import { Router, RouterState, ActivatedRoute } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  public user: Object = null;

  constructor(public router: Router, public active: ActivatedRoute, private authSv: AuthService) {
  }

  ngOnInit() {
    this.user = this.authSv.getUser();
    this.authSv.auth$.subscribe((authInfo: any) => {
      this.user = authInfo.user;
    });
  }

}
