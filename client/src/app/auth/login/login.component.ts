import { Title } from '@angular/platform-browser';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Http, Headers } from '@angular/http';
import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';

import { AuthService } from '../../services/auth.service';
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
  public serverMessage: string = '';

  constructor(
    private titleSv: Title,
    private router: Router,
    private http: Http,
    private fb: FormBuilder,
    private api: Api,
    private authSv: AuthService) {
  }

  ngOnInit() {
    this.titleSv.setTitle("Login");
    this.createForm();
    this.createFormErrors();
  }

  createForm() {
    this.form = this.fb.group({
      email: ['', Validators.required],
      password: ['', Validators.required]
    });
  }

  createFormErrors() {
    this.formErrors = {
      email: {
        required: 'Username/Email is required.'
      },
      password: {
        required: 'Password is required.'
      }
    };
  }

  redirect() {
    this.router.navigate([this.authSv.redirectUrl]);
  }

  onSubmit() {
    if (this.form.valid) {
      this.api.request('auth.login', 'POST', this.form.value)
      .catch(Helper.getFormHandleError)
      .subscribe((response: any) => {
        if (response.success) {
          let data = response.data
          this.submitted = true;
          this.authSv.store(data.user, data.access_token, data.refresh_token);
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
