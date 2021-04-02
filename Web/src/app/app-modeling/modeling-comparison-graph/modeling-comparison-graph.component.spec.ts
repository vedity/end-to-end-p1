import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelingComparisonGraphComponent } from './modeling-comparison-graph.component';

describe('ModelingComparisonGraphComponent', () => {
  let component: ModelingComparisonGraphComponent;
  let fixture: ComponentFixture<ModelingComparisonGraphComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelingComparisonGraphComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelingComparisonGraphComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
