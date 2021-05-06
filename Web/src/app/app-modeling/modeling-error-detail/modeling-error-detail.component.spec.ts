import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelingErrorDetailComponent } from './modeling-error-detail.component';

describe('ModelingErrorDetailComponent', () => {
  let component: ModelingErrorDetailComponent;
  let fixture: ComponentFixture<ModelingErrorDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelingErrorDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelingErrorDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
