import { Injectable } from '@angular/core';
import { Http, Headers, URLSearchParams } from '@angular/http';
import * as Lodash from 'lodash';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

const ENDPOINTS = {
  'user': {
    'create': '/api/user/create',
    'store': '/api/user',
    'show': '/api/user/{user}',
    'edit': '/api/user/{user}/edit',
    'update': '/api/user/{user}',
    'destroy': '/api/user/{user}',
    'login': '/api/user/login',
    'logout': '/api/user/logout',
    'password': '/api/user/password'
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
    return Lodash.get(this._config, key);
  }

  request(route: string, method: string, parameters: Object): Observable<any> {
    const body = JSON.stringify(parameters);
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    let params = new URLSearchParams(body);
    switch (method) {
      case METHOD_GET:
        return this.http.get(this.get(route), {headers: headers, params: params}).map(res => res.json());
      case METHOD_POST:
        return this.http.post(this.get(route), body, {headers: headers}).map(res => res.json());
      case METHOD_PUT:
        return this.http.put(this.get(route), body, {headers: headers}).map(res => res.json());
      case METHOD_PATCH:
        return this.http.patch(this.get(route), body, {headers: headers}).map(res => res.json());
      case METHOD_DELETE:
        return this.http.delete(this.get(route), {headers: headers, params: params}).map(res => res.json());
      default:
        return this.http.get(this.get(route), {headers: headers, params: params}).map(res => res.json());
    }
  }
}
