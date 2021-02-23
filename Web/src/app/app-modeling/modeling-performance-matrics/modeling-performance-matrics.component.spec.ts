import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelingPerformanceMatricsComponent } from './modeling-performance-matrics.component';

describe('ModelingPerformanceMatricsComponent', () => {
  let component: ModelingPerformanceMatricsComponent;
  let fixture: ComponentFixture<ModelingPerformanceMatricsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelingPerformanceMatricsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelingPerformanceMatricsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
