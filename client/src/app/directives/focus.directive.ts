import { Directive, NgZone, ElementRef } from '@angular/core';

@Directive({
  selector: '[appFocus]'
})
export class FocusDirective {

  constructor(private zone: NgZone, private el: ElementRef) {
    // Angular will get notified that a task is done and change detection will be performed.
    this.zone.run(() => {
      setTimeout(() => this.el.nativeElement.focus());
    });
  }

}
