import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListDatabaseComponent } from './list-database.component';

describe('ListDatabaseComponent', () => {
  let component: ListDatabaseComponent;
  let fixture: ComponentFixture<ListDatabaseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListDatabaseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListDatabaseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
