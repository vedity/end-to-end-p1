import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelingViewDetailComponent } from './modeling-view-detail.component';

describe('ModelingViewDetailComponent', () => {
  let component: ModelingViewDetailComponent;
  let fixture: ComponentFixture<ModelingViewDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelingViewDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelingViewDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
