import { Title } from '@angular/platform-browser';
import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';

import { Helper } from '../../utils/helper';
import { Api } from '../../utils/api';

import { BetweenValidator } from '../../validators/between.validator';
import { PasswordConfirmValidator } from '../../validators/password-confirm.validator';

@Component({
  selector: 'app-reset',
  templateUrl: './reset.component.html',
  styleUrls: ['./reset.component.scss']
})
export class ResetComponent implements OnInit {
  public token: string = '';
  public second: number = 3;
  public submitted: Boolean = false;
  public submitting: Boolean = false;
  public form: FormGroup;
  public formErrors: Object;
  public formMessages: Object = {};
  public serverMessage: string = '';

  constructor(
    private titleSv: Title,
    private router: Router,
    private route: ActivatedRoute,
    private fb: FormBuilder,
    private api: Api) {
  }

  ngOnInit() {
    this.titleSv.setTitle("Reset Password");
    this.token = this.route.snapshot.paramMap.get('token');
    this.createForm();
    this.createFormErrors();
  }

  createForm() {
    this.form = this.fb.group({
      passwords: this.fb.group({
        password: ['', Validators.compose([
            Validators.required,
            BetweenValidator(6, 30)
          ])
        ],
        password_confirmation: ['', Validators.required]
      }, {validator: PasswordConfirmValidator})
    });
  }

  createFormErrors() {
    this.formErrors = {
      password: {
        required: "New password is required.",
        between: "New password must be between 6 and 30 characters",
      },
      password_confirmation: {
        required: "New password confirmation is required.",
      },
      passwords: {
        passwordConfirm: "New password & password confirmation does not match.",
      }
    };
  }

  redirect() {
    this.second -= 1;
    if (this.second > 0) {
        window.setTimeout(() => this.redirect(), 1000);
    } else {
        this.router.navigate(['auth/login']);
    }
  }

  onSubmit() {
    if (this.form.valid) {
      this.form.value['password'] = this.form.value.passwords['password'];
      this.form.value['password_confirm'] = this.form.value.passwords['password_confirmation'];
      let url = this.api.get('auth.reset').replace(':token', this.token);
      this.api.request(url, 'POST', this.form.value)
      .catch(Helper.getFormHandleError)
      .subscribe((response: any) => {
        if (response.success) {
          this.submitted = true;
          this.redirect();
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
