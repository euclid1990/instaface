import { Title } from '@angular/platform-browser';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Http, Headers } from '@angular/http';
import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';

import { Helper } from '../../utils/helper';
import { Api } from '../../utils/api';

import { EmailUniqueValidator } from '../../validators/email-unique.validator';
import { EmailFormatValidator } from '../../validators/email-format.validator';

@Component({
  selector: 'app-forgot',
  templateUrl: './forgot.component.html',
  styleUrls: ['./forgot.component.scss']
})
export class ForgotComponent implements OnInit {
  public submitted: Boolean = false;
  public submitting: Boolean = false;
  public form: FormGroup;
  public formErrors: Object;
  public formMessages: Object = {};
  public serverMessage: string = '';

  constructor(
    private titleSv: Title,
    private router: Router,
    private http: Http,
    private fb: FormBuilder,
    private api: Api) {
  }

  ngOnInit() {
    this.titleSv.setTitle("Forgot Password");
    this.createForm();
    this.createFormErrors();
  }

  createForm() {
    this.form = this.fb.group({
      email: ['', Validators.compose([
          Validators.required,
          EmailFormatValidator
        ])
      ]
    });
  }

  createFormErrors() {
    this.formErrors = {
      email: {
        required: "Email is required.",
        emailFormat: "Email is invalid format",
      }
    };
  }

  onSubmit() {
    if (this.form.valid) {
      this.api.request('auth.forgot', 'POST', this.form.value)
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
