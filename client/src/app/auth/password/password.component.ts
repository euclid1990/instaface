import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';

import { Helper } from '../../utils/helper';
import { Api } from '../../utils/api';

import { BetweenValidator } from '../../validators/between.validator';
import { PasswordConfirmValidator } from '../../validators/password-confirm.validator';

@Component({
  selector: 'app-password',
  templateUrl: './password.component.html',
  styleUrls: ['./password.component.scss']
})
export class PasswordComponent implements OnInit {
  public submitted: Boolean = false;
  public submitting: Boolean = false;
  public form: FormGroup;
  public formErrors: Object;
  public formMessages: Object = {};
  public serverMessage: string = '';

  constructor(
    private router: Router,
    private fb: FormBuilder,
    private api: Api) {
  }

  ngOnInit() {
    this.createForm();
    this.createFormErrors();
  }

  createForm() {
    this.form = this.fb.group({
      current_password: ['', Validators.required],
      passwords: this.fb.group({
        new_password: ['', Validators.compose([
            Validators.required,
            BetweenValidator(6, 30)
          ])
        ],
        new_password_confirmation: ['', Validators.required]
      }, {validator: PasswordConfirmValidator})
    });
  }

  createFormErrors() {
    this.formErrors = {
      current_password: {
        required: "Current password is required.",
      },
      new_password: {
        required: "New password is required.",
        between: "New password must be between 6 and 30 characters",
      },
      new_password_confirmation: {
        required: "New password confirmation is required.",
      },
      passwords: {
        passwordConfirm: "New password & password confirmation does not match.",
      }
    };
  }

  onSubmit() {
    if (this.form.valid) {
      this.form.value['new_password'] = this.form.value.passwords['new_password'];
      this.form.value['new_password_confirm'] = this.form.value.passwords['new_password_confirmation'];
      this.api.request('auth.password', 'POST', this.form.value)
      .catch(Helper.getFormHandleError)
      .subscribe((response: any) => {
        if (response.success) {
          this.submitted = true;
        } else {
          this.formMessages = response.errors || {};
          this.serverMessage = response.message || '';
          this.submitting = false;
        }
      });
      this.submitting = true;
    } else {
      Helper.markFormAsTouched(this.form);
    }
  }
}
