import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DatadetailListComponent } from './datadetail-list.component';

describe('DatadetailListComponent', () => {
  let component: DatadetailListComponent;
  let fixture: ComponentFixture<DatadetailListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DatadetailListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DatadetailListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
