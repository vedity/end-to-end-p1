import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiService } from './api.service';

@Component({
  selector: 'app-list-project',
  templateUrl: './list-project.component.html',
  styleUrls: ['./list-project.component.scss']
})
export class ListProjectComponent implements OnInit {

  constructor(private apiService:ApiService) {​​​​​ }​​​​​
  project_list=[];
    
  ngOnInit(): void {

    this.apiService.getproject().subscribe(
      logs =>{ this.project_list=logs.Data},
      error => console.log(error)
    );

  }

}