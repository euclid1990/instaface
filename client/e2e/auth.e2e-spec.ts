import { AuthPage } from './auth.po';

describe('instaface App', () => {
  let page: AuthPage;

  beforeEach(() => {
    page = new AuthPage();
  });

  it('should not be able to submit login form', () => {
    page.navigateToLogin();
    expect(page.getSubmitButton().isEnabled()).toEqual(false);
  });
});
