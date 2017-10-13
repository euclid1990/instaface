import { Component, OnInit, Input } from '@angular/core';
import { FormControl, FormGroup, AbstractControl } from '@angular/forms';
import { Helper } from '../../utils/helper';

@Component({
  selector: 'app-form-error',
  templateUrl: './form-error.component.html',
  styleUrls: ['./form-error.component.scss']
})
export class FormErrorComponent implements OnInit {

  @Input() control: FormControl;
  @Input() group: FormGroup;
  @Input() overrideMsg: Object;

  constructor() { }

  ngOnInit() { }

  getControlName(c: AbstractControl): string | null {
    const formGroup = c.parent.controls;
    return Object.keys(formGroup).find(name => c === formGroup[name]) || null;
  }

  get errorMsg(): string {
    if (this.control) {
      for (const propertyName in this.control.errors) {
        if (this.control.errors.hasOwnProperty(propertyName) && this.control.errors[propertyName] && this.control.touched) {
          return Helper.getFormErrorMessages(this.getControlName(this.control), propertyName, this.overrideMsg);
        }
      }
    } else if (this.group) {
      for (const propertyName in this.group.errors) {
        if (this.group.errors.hasOwnProperty(propertyName) && this.group.errors[propertyName]) {
          return Helper.getFormErrorMessages(null, propertyName, this.overrideMsg);
        }
      }
    }
    return null;
  }
}
