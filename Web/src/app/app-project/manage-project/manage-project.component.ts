import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-manage-project',
  templateUrl: 'manage-project.component.html',
  styleUrls: ['./manage-project.component.scss']
})
export class ManageProjectComponent implements OnInit {
active=1;
  constructor(public router:Router) { }

  ngOnInit() {
  }

  create() {
    this.router.navigate(['create']);
  }
}
