import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {createproject} from './project.model'

@Component({
  selector: 'app-create-project',
  templateUrl: './create-project.component.html',
  styleUrls: ['./create-project.component.scss']
})
export class CreateProjectComponent implements OnInit {

  constructor(public router:Router) { }
 public data:createproject =  new createproject();
 errorStatus:boolean=true;
  ngOnInit() {

  }

  save(){

  }

}
