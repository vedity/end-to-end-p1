import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelingFeatureImportanceComponent } from './modeling-feature-importance.component';

describe('ModelingFeatureImportanceComponent', () => {
  let component: ModelingFeatureImportanceComponent;
  let fixture: ComponentFixture<ModelingFeatureImportanceComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelingFeatureImportanceComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelingFeatureImportanceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
