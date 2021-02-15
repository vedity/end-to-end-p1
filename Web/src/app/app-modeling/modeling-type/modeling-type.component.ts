import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-modeling-type',
  templateUrl: './modeling-type.component.html',
  styleUrls: ['./modeling-type.component.scss']
})
export class ModelingTypeComponent implements OnInit {

  constructor(public router:Router) { }
 params:any;
  ngOnInit(): void {
if(localStorage.getItem("Modeling")){
  this.params=JSON.parse(localStorage.getItem("Modeling"));
console.log(this.params);

}
  }
}
