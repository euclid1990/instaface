import { Injectable } from '@angular/core';
import { Router, ActivatedRoute, NavigationStart } from '@angular/router';
import { Subject } from 'rxjs/Subject';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/filter';

@Injectable()
export class NavtabService {
  // Observable object sources
  private showNavtabSource: Subject<boolean>;
  // Observable object streams
  public showNavtab$: Observable<boolean> = new Subject<boolean>();

  constructor(private router: Router, private activeRoute: ActivatedRoute) {
    this.router = router;
    this.router.events
      .filter(event => event instanceof NavigationStart)
      .subscribe((event: any) => {
        this.toggle(event.url);
      });
    this.showNavtabSource = new Subject<boolean>();
    this.showNavtab$ = this.showNavtabSource.asObservable();
  }

  toggle(url: string) {
    if (['/auth/register', '/auth/login'].includes(url)) {
      this.showNavtabSource.next(false);
    } else {
      this.showNavtabSource.next(true);
    }
  }
}
