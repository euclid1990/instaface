import { Injectable } from '@angular/core';
import { Http, Headers, URLSearchParams } from '@angular/http';
import * as Lodash from 'lodash';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

const ENDPOINTS = {
  'auth': {
    'register': '/api/auth/register',
    'login': '/api/auth/login',
    'logout': '/api/auth/logout',
    'refresh': '/api/auth/refresh',
    'active': '/api/auth/active',
    'forgot': '/api/auth/forgot',
    'reset': '/api/auth/reset/:token',
    'password': '/api/auth/password',
  },
  'validate': {
    'unique_email': '/api/validate/unique_email'
  }
};

const METHOD_GET = 'GET';
const METHOD_POST = 'POST';
const METHOD_PUT = 'PUT';
const METHOD_PATCH = 'PATCH';
const METHOD_DELETE = 'DELETE';

@Injectable()
export class Api {

  private _config: Object = ENDPOINTS;

  constructor(private http: Http) { }

  get(key: any): any {
    return Lodash.get(this._config, key) || key;
  }

  request(route: string, method: string, parameters: Object): Observable<any> {
    const body = JSON.stringify(parameters);
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    let authInfo = JSON.parse(localStorage.getItem('auth'));
    if (authInfo) {
      headers.append('Authorization', 'Bearer ' + authInfo.accessToken);
    }
    let params = new URLSearchParams(body);
    let options: Object = {headers: headers};
    switch (method) {
      case METHOD_GET:
        if (parameters) {
          options = {headers: headers, params: params};
        }
        return this.http.get(this.get(route), options).map(res => res.json());
      case METHOD_POST:
        return this.http.post(this.get(route), body, options).map(res => res.json());
      case METHOD_PUT:
        return this.http.put(this.get(route), body, options).map(res => res.json());
      case METHOD_PATCH:
        return this.http.patch(this.get(route), body, options).map(res => res.json());
      case METHOD_DELETE:
        if (parameters) {
          options = {headers: headers, params: params};
        }
        return this.http.delete(this.get(route), options).map(res => res.json());
      default:
        if (parameters) {
          options = {headers: headers, params: params};
        }
        return this.http.get(this.get(route), options).map(res => res.json());
    }
  }
}
