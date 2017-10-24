import { Title } from '@angular/platform-browser';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';

import { Helper } from '../../utils/helper';
import { Api } from '../../utils/api';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.scss']
})
export class LogoutComponent implements OnInit {

  constructor(private titleSv: Title, private router: Router, private api: Api, private authSv: AuthService) { }

  ngOnInit() {
    this.titleSv.setTitle("Logout");
    this.api.request('auth.logout', 'GET', null)
      .catch(Helper.getFormHandleError)
      .subscribe((response: any) => {
        if (response.success) {
          this.redirect();
        }
      });
    this.authSv.destroy();
    this.redirect();
  }

  redirect() {
    this.router.navigate(["/"]);
  }

}
