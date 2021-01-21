import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ManageSchemaMappingComponent } from './manage-schema-mapping.component';

describe('ManageSchemaMappingComponent', () => {
  let component: ManageSchemaMappingComponent;
  let fixture: ComponentFixture<ManageSchemaMappingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ManageSchemaMappingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ManageSchemaMappingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
