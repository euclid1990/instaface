import { Injectable } from '@angular/core';
import { AbstractControl, NG_VALIDATORS, Validator, ValidatorFn, Validators } from '@angular/forms';
import { Observable } from 'rxjs/Observable';
import { Api } from '../utils/api';

interface ValidationResult {
    [key: string]: any;
}

@Injectable()
export class EmailUniqueValidator {
    private uniqueEmail: string;

    constructor(private api: Api) {}

    check(c: AbstractControl): Promise<ValidationResult> {
        return new Promise((resolve, reject) => {
            this.api.request('validate.unique_email', 'POST', { email: c.value })
            .catch(this.handleError)
            .subscribe((response) => {
                if (response.data.exist == false) {
                    resolve(null);
                } else {
                    resolve({ "emailUnique": true });
                };
            });
        });
    }

    private handleError(error: any) {
        return Observable.throw(error.json().errors);
    }
}
