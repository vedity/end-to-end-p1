import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelingConfusionMatricsComponent } from './modeling-confusion-matrics.component';

describe('ModelingConfusionMatricsComponent', () => {
  let component: ModelingConfusionMatricsComponent;
  let fixture: ComponentFixture<ModelingConfusionMatricsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelingConfusionMatricsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelingConfusionMatricsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
