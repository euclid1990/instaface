import { AppPage } from './app.po';

describe('instaface App', () => {
  let page: AppPage;

  beforeEach(() => {
    page = new AppPage();
  });

  it('should display footer', () => {
    page.navigateTo();
    expect(page.getFooterParagraphElements().count()).toBe(2);
    expect(page.getFooterParagraphElement().getText()).toBe('Hand crafted with love by euclid1990 and our awesome contributors.');
  });
});
