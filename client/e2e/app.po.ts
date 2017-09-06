import { browser, by, element } from 'protractor';

export class AppPage {
  navigateTo() {
    return browser.get('/');
  }

  getFooterParagraphElements() {
    return element.all(by.css('app-footer p'));
  }

  getFooterParagraphElement() {
    return element(by.css('app-footer p'));
  }
}
