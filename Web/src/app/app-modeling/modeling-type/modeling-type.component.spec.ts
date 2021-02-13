import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelingTypeComponent } from './modeling-type.component';

describe('ModelingTypeComponent', () => {
  let component: ModelingTypeComponent;
  let fixture: ComponentFixture<ModelingTypeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelingTypeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelingTypeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
