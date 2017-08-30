import { TestBed, inject } from '@angular/core/testing';

import { Helper } from './helper';

describe('Helper', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [Helper]
    });
  });

  it('should be created', inject([Helper], (util: Helper) => {
    expect(util).toBeTruthy();
  }));
});
