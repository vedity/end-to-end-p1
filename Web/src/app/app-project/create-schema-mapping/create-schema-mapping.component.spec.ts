import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateSchemaMappingComponent } from './create-schema-mapping.component';

describe('CreateSchemaMappingComponent', () => {
  let component: CreateSchemaMappingComponent;
  let fixture: ComponentFixture<CreateSchemaMappingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateSchemaMappingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateSchemaMappingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
