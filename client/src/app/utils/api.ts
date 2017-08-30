import { Injectable } from '@angular/core';
import * as Lodash from 'lodash';

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

@Injectable()
export class Api {

  private _config: Object = ENDPOINTS;

  constructor() { }

  get(key: any): any {
    return Lodash.get(this._config, key);
  }
}
