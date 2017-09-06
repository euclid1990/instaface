import { browser, by, element } from 'protractor';

export class AuthPage {
  navigateToLogin() {
    return browser.get('/auth/login');
  }

  getSubmitButton() {
    return element(by.css('button[type=submit]'));
  }
}
