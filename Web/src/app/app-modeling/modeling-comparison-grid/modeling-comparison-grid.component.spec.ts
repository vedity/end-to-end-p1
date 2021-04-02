import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelingComparisonGridComponent } from './modeling-comparison-grid.component';

describe('ModelingComparisonGridComponent', () => {
  let component: ModelingComparisonGridComponent;
  let fixture: ComponentFixture<ModelingComparisonGridComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelingComparisonGridComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelingComparisonGridComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
