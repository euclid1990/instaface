import { Injectable } from '@angular/core';
import { Subject } from 'rxjs/Subject';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class AuthService {
  public user: any;
  public accessToken: string;
  public refreshToken: string;
  public isLoggedIn: boolean = false;

  // Observable object sources
  public authSource = new Subject<Object>();
  // Observable object streams
  public auth$ = this.authSource.asObservable();

  // Store the URL so we can redirect after logging in
  redirectUrl: string = '/';

  constructor() {
    let auth = JSON.parse(localStorage.getItem('auth'));
    if (auth) {
      this.setUser(auth.user);
      this.setAccessToken(auth.accessToken);
      this.setRefreshToken(auth.refreshToken);
      this.setIsLoggedIn(true);
    }
  }

  authenticated() {
    let auth = JSON.parse(localStorage.getItem('auth'));
    return auth ? true : false;
  }

  store(user: any, accessToken: string, refreshToken: string) {
    this.setUser(user);
    this.setAccessToken(accessToken);
    this.setRefreshToken(refreshToken);
    this.setIsLoggedIn(true);
    let auth: Object = { user: this.user, accessToken: this.accessToken, refreshToken: this.refreshToken };
    localStorage.setItem('auth', JSON.stringify(auth));
    this.authSource.next(auth);
  }

  destroy() {
    this.setUser(null);
    this.setAccessToken(null);
    this.setRefreshToken(null);
    this.setIsLoggedIn(false);
    localStorage.removeItem('auth');
    let auth: Object = { user: null, accessToken: null, refreshToken: null };
    this.authSource.next(auth);
  }

  getAccessToken() {
    return this.accessToken;
  }

  setAccessToken(token: string) {
    this.accessToken = token;
  }

  getRefreshToken() {
    return this.refreshToken;
  }

  setRefreshToken(token: string) {
    this.refreshToken = token;
  }

  getUser() {
    return this.user;
  }

  setUser(user: any) {
    this.user = user;
  }

  getIsLoggedIn() {
    return this.isLoggedIn;
  }

  setIsLoggedIn(isLoggedIn: boolean) {
    this.isLoggedIn = isLoggedIn;
  }

  getHeaders() {
      let headers = new Headers({ Authorization: 'Bearer ' + this.accessToken });
      return headers;
  }
}
