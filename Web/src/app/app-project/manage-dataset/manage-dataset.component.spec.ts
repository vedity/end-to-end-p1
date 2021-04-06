import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ManageDatasetComponent } from './manage-dataset.component';

describe('ManageDatasetComponent', () => {
  let component: ManageDatasetComponent;
  let fixture: ComponentFixture<ManageDatasetComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ManageDatasetComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ManageDatasetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
