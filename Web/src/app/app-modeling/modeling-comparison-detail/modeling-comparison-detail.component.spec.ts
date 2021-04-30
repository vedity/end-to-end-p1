import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelingComparisonDetailComponent } from './modeling-comparison-detail.component';

describe('ModelingComparisonDetailComponent', () => {
  let component: ModelingComparisonDetailComponent;
  let fixture: ComponentFixture<ModelingComparisonDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelingComparisonDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelingComparisonDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
