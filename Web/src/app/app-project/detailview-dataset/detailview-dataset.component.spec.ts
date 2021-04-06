import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailviewDatasetComponent } from './detailview-dataset.component';

describe('DetailviewDatasetComponent', () => {
  let component: DetailviewDatasetComponent;
  let fixture: ComponentFixture<DetailviewDatasetComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DetailviewDatasetComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DetailviewDatasetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
