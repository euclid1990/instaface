import { Injectable } from '@angular/core';
import { CanActivate, Router, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { AuthService }      from './auth.service';

@Injectable()
export class GuardService implements CanActivate {

  constructor(
    private authSv: AuthService,
    private router: Router) {}

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    if (this.authSv.isLoggedIn) { return true; }
    // Store the attempted URL for redirecting
    let url: string = state.url;
    this.authSv.redirectUrl = url;
    // Navigate to the login page with extras
    this.router.navigate(['/auth/login']);
    return true;
  }
}

@Injectable()
export class UnguardService implements CanActivate {

  constructor(
    private authSv: AuthService,
    private router: Router) {}

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    if (!this.authSv.isLoggedIn) { return true; }
    // Navigate to the home page with extras
    this.router.navigate(['/']);
    return true;
  }
}
