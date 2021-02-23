import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelingModalSummaryComponent } from './modeling-modal-summary.component';

describe('ModelingModalSummaryComponent', () => {
  let component: ModelingModalSummaryComponent;
  let fixture: ComponentFixture<ModelingModalSummaryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelingModalSummaryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelingModalSummaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
