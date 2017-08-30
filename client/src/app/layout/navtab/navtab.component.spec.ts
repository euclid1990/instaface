import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';

import { NavtabComponent } from './navtab.component';

describe('NavtabComponent', () => {
  let component: NavtabComponent;
  let fixture: ComponentFixture<NavtabComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [RouterTestingModule],
      declarations: [ NavtabComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NavtabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });

  it('should render nav tab', async(() => {
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('ul.nav-tabs > li > a').textContent).toContain('News Feed');
  }));
});
