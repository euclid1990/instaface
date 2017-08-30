import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Http, Headers } from '@angular/http';
import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

import { Helper } from '../../utils/helper';
import { Api } from '../../utils/api';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  public submitted: Boolean = false;
  public submitting: Boolean = false;
  public form: FormGroup;
  public formErrors: Object;
  public formMessages: Object = {};
  private formValidations: Object;

  constructor(
    private router: Router,
    private http: Http,
    private fb: FormBuilder,
    private api: Api) {
  }

  ngOnInit() {
    this.createForm();
    this.createFormValidations();
    this.createFormErrors();
  }

  createForm() {
    this.form = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
    this.form.valueChanges.subscribe(data => this.onValueChanged(data));
  }

  createFormValidations() {
    this.formValidations = {
      username: {
        required: 'Username/Email is required.'
      },
      password: {
        required: 'Password is required.'
      }
    };
  }

  createFormErrors() {
    this.formErrors = {
      username: '',
      password: ''
    };
  }

  onValueChanged(data?: any) {
    if (!this.form) { return; }
    const form = this.form;
    // Clear previous error message (if have any)
    this.createFormErrors();
    this.formErrors = Helper.getFormErrors(form, this.formValidations, this.formErrors);
  }

  redirect() {
    this.router.navigate(['/']);
  }

  onSubmit() {
    if (this.form.valid) {
      let body = JSON.stringify(this.form.value);
      let headers = new Headers();
      headers.append('Content-Type', 'application/json');
      this.http.post(this.api.get('user.login'), body, {
        headers: headers
      })
      .map(res => res.json())
      .catch(Helper.getFormHandleError)
      .subscribe((response: any) => {
        if (+response.status === 200) {
          this.submitted = true;
          this.redirect();
        } else {
          this.formMessages = response.errors;
          this.submitting = false;
        }
      });
      this.submitting = true;
    }
  }
}
