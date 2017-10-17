import { AbstractControl, NG_VALIDATORS, Validator, ValidatorFn, Validators } from '@angular/forms';

interface ValidationResult {
    [key: string]: any;
}

export function CheckboxRequiredValidator(c: AbstractControl): ValidationResult {
  return c.value ? null : { 'checkboxRequired': true };
}
