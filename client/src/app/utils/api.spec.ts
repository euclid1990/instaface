import { TestBed, inject } from '@angular/core/testing';
import { HttpModule } from '@angular/http';

import { Api } from './api';

describe('Api', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpModule],
      providers: [Api]
    });
  });

  it('should be created', inject([Api], (util: Api) => {
    expect(util).toBeTruthy();
  }));
});
