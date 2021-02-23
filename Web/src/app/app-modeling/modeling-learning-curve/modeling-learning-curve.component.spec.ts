import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelingLearningCurveComponent } from './modeling-learning-curve.component';

describe('ModelingLearningCurveComponent', () => {
  let component: ModelingLearningCurveComponent;
  let fixture: ComponentFixture<ModelingLearningCurveComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelingLearningCurveComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelingLearningCurveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
