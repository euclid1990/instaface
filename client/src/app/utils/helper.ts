import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Http, Headers } from '@angular/http';
import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';

import * as Lodash from 'lodash';
import { Observable } from 'rxjs/Observable';

const HTTP_ERRORS = [
  {code: 400, message: 'Bad Request'},
  {code: 401, message: 'Unauthorized'},
  {code: 403, message: 'Forbidden'},
  {code: 404, message: 'Not Found'},
  {code: 405, message: 'Method Not Allowed'},
  {code: 500, message: 'Internal Server Error'},
  {code: 502, message: 'Bad Gateway'},
  {code: 503, message: 'Service Unavailable'},
];

@Injectable()
export class Helper {

  constructor() { }

  static getFormHandleError(error: any): any {
    let messages: any = {};
    if (error['status']) {
      const e = Lodash.find(HTTP_ERRORS, {'code': +error.status}); // Converted to a number with the JavaScript (+) operator.
      messages.server = [e.message];
    }
    return Observable.create(function (observer) {
      observer.next({ status: 500, errors: messages });
      observer.complete();
    });
  }

  static getFormErrors(form: FormGroup, formValidations: Object, formErrors: Object): Object {
    for (const field in formErrors) {
      const g = form.get(field);
      if (g instanceof FormGroup) {
        for (const name in g.controls) {
          const control = g.controls[name];
          if (control && control.dirty && !control.valid) {
            if (formValidations.hasOwnProperty(name)) {
              const messages = formValidations[name];
              for (const key in control.errors) {
                formErrors[name] = messages[key];
                break;
              }
            }
          }
        }
      }
      if (g && g.dirty && !g.valid) {
        const messages = formValidations[field];
        for (const key in g.errors) {
          formErrors[field] = messages[key];
        }
      }
    }
    return formErrors;
  }
}
