import { TestBed, inject } from '@angular/core/testing';
import { NavtabService } from './navtab.service';

describe('NavtabService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [NavtabService]
    });
  });

  it('should be created', inject([NavtabService], (service: NavtabService) => {
    expect(service).toBeTruthy();
  }));
});
