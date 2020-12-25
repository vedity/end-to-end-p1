import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListDatadetailComponent } from './list-datadetail.component';

describe('ListDatadetailComponent', () => {
  let component: ListDatadetailComponent;
  let fixture: ComponentFixture<ListDatadetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListDatadetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListDatadetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
