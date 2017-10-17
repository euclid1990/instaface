import { AbstractControl, NG_VALIDATORS, Validator, ValidatorFn, Validators } from '@angular/forms';

interface ValidationResult {
  [key: string]: any;
}

function isPresent(obj: any): boolean {
  return obj !== undefined && obj !== null;
}

export function BetweenValidator(min: number, max: number): ValidatorFn {
  return (control: AbstractControl): ValidationResult => {
    if (isPresent(Validators.required(control))) {
      return null;
    }
    const str = control.value;
    const no = (str !== null) && (min <= str.length) && (str.length <= max);
    return no ? null : { 'between': true };
  };
}
