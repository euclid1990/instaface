import { TestBed, inject } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';

import { NavtabService } from './navtab.service';

describe('NavtabService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [RouterTestingModule],
      providers: [NavtabService]
    });
  });

  it('should be created', inject([NavtabService], (service: NavtabService) => {
    expect(service).toBeTruthy();
  }));
});
