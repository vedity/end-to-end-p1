import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelingActualPredictionComponent } from './modeling-actual-prediction.component';

describe('ModelingActualPredictionComponent', () => {
  let component: ModelingActualPredictionComponent;
  let fixture: ComponentFixture<ModelingActualPredictionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelingActualPredictionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelingActualPredictionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
