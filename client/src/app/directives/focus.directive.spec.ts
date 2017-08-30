import { TestBed, inject } from '@angular/core/testing';
import { NgZone, ElementRef } from '@angular/core';
import { FocusDirective } from './focus.directive';

class MockElementRef extends ElementRef {
  constructor() {
    super(null);
  }
}

describe('FocusDirective', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [FocusDirective, {provide: ElementRef, useClass: MockElementRef}]
    });
  });

  it('should be created', inject([FocusDirective], (directive: FocusDirective) => {
    expect(directive).toBeTruthy();
  }));
});
