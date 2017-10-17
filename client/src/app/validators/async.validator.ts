import { AbstractControl } from '@angular/forms';
import { Observer } from 'rxjs/Observer';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/debounceTime';
import 'rxjs/add/operator/distinctUntilChanged';

const DEBOUNCE_TIME = 500;

export class AsyncValidator {
    private _validate;

    constructor(validator: (control: AbstractControl) => any, debounceTime = DEBOUNCE_TIME) {
        let source: any = Observable.create((observer: Observer<AbstractControl>) => {
            this._validate = (control) => observer.next(control);
        });

        source.debounceTime(debounceTime)
        //.distinctUntilChanged(null, (x) => x.control.value)
        .map(x => { return { promise: validator(x.control), resolver: x.promiseResolver }; })
        .subscribe((x) => {
            x.promise.then(
                resultValue => x.resolver(resultValue),
                (e) => { console.log('Async validator error: %s', e); }
            );
        });
    }

    private _getValidator() {
        return (control: AbstractControl) => {
            let promiseResolver;
            let p = new Promise((resolve) => {
                promiseResolver = resolve;
            });
            this._validate({ control: control, promiseResolver: promiseResolver });
            return p;
        };
    }

    static debounce(validator: (control: AbstractControl) => any, debounceTime = DEBOUNCE_TIME) {
        var asyncValidator = new this(validator, debounceTime);
        // Return origin validator function
        return asyncValidator._getValidator();
    }
}
