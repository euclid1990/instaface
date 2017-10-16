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

const VALIDATOR_MESSAGES = {
  'required': 'The :attribute field is required.',
  'unique': 'The :attribute has already been taken.',
}

@Injectable()
export class Helper {

  constructor() { }

  static getFormHandleError(error: any): any {
    let message: string = '';
    if (error['status']) {
      const e = Lodash.find(HTTP_ERRORS, {'code': +error.status}); // Converted to a number with the JavaScript (+) operator.
      message = e.message;
    }
    let errors: Object = {}
    if (error['_body']) {
      let body = JSON.parse(error['_body']);
      errors = body['errors'];
    }
    return Observable.create(function (observer) {
      observer.next({ success: false, message: message, errors: errors });
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

  static ucfirst(str: string) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }

  static getFormErrorMessages(controlName: string, validatorName: string, overrideMsg: Object): string {
    const config = Lodash.assign({}, VALIDATOR_MESSAGES, overrideMsg);
    if (config.hasOwnProperty(validatorName)) {
      if (!controlName) {
        return config[validatorName];
      }
      let replacers = {
        ':attribute': controlName,
        ':ATTRIBUTE': controlName.toUpperCase(),
        ':Attribute': Helper.ucfirst(controlName)
      };
      let msg = config[validatorName].replace(/(\:attribute|\:ATTRIBUTE|\:Attribute)/g, function(match) {
        return replacers[match];
      });
      return msg;
    }
    return null;
  }

  static markFormAsTouched(form: FormGroup): void {
    for (const field in form.controls) {
      if (form.controls.hasOwnProperty(field)) {
        let control: any = form.controls[field];
        // If field control is formGroup
        if (control.controls) {
          Helper.markFormAsTouched(control);
        } else {
          control.markAsTouched();
        };
      }
    }
  }
}
