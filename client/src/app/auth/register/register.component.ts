import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Http, Headers } from '@angular/http';
import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';

import { UserModel, GENDERS } from '../../models/user.model';
import { AuthService } from '../../services/auth.service';
import { Helper } from '../../utils/helper';
import { Api } from '../../utils/api';

import { AsyncValidator } from '../../validators/async.validator';
import { BetweenValidator } from '../../validators/between.validator';
import { PasswordConfirmValidator } from '../../validators/password-confirm.validator';
import { CheckboxRequiredValidator } from '../../validators/checkbox-required.validator';
import { EmailUniqueValidator } from '../../validators/email-unique.validator';
import { EmailFormatValidator } from '../../validators/email-format.validator';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
  providers: [EmailUniqueValidator]
})
export class RegisterComponent implements OnInit {
  public second: number = 3;
  public submitted: Boolean = false;
  public submitting: Boolean = false;
  public form: FormGroup;
  public formErrors: Object;
  public formMessages: Object = {};
  public serverMessage: string = '';
  public genders: Array<Object> = GENDERS;

  constructor(
    private router: Router,
    private http: Http,
    private fb: FormBuilder,
    private api: Api,
    private authSv: AuthService,
    private emailUniqueValidator: EmailUniqueValidator) {
  }

  ngOnInit() {
    this.createForm();
    this.createFormErrors();
  }

  createForm() {
    this.form = this.fb.group({
      name: ['', Validators.compose([
          Validators.required,
          BetweenValidator(3, 50)
        ])
      ],
      gender: ['', Validators.required],
      email: ['', Validators.compose([
          Validators.required,
          EmailFormatValidator
        ]),
        AsyncValidator.debounce(this.emailUniqueValidator.check.bind(this.emailUniqueValidator))
      ],
      passwords: this.fb.group({
        password: ['', Validators.compose([
            Validators.required,
            BetweenValidator(6, 30)
          ])
        ],
        password_confirmation: ['', Validators.required]
      }, {validator: PasswordConfirmValidator}),
      agreed: [true, CheckboxRequiredValidator],
    });
  }

  createFormErrors() {
    this.formErrors = {
      name: {
        required: "Name is required.",
        between: "Name must be between 3 and 50 characters.",
      },
      email: {
        required: "Email is required.",
        emailFormat: "Email is invalid format",
        emailUnique: "Email has already been taken",
      },
      password: {
        required: "Password is required.",
        between: "Password must be between 6 and 30 characters",
      },
      password_confirmation: {
        required: "Password confirmation is required.",
      },
      passwords: {
        passwordConfirm: "Password & Password confirmation does not match.",
      },
      agreed: {
        checkboxRequired: "You must agree to the terms of use.",
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
      this.api.request('auth.register', 'POST', this.form.value)
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
