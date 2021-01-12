import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailviewProjectComponent } from './detailview-project.component';

describe('DetailviewProjectComponent', () => {
  let component: DetailviewProjectComponent;
  let fixture: ComponentFixture<DetailviewProjectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DetailviewProjectComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DetailviewProjectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
