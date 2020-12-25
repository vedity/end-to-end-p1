import { Component, OnInit } from '@angular/core';
import { ApiService } from '../list-project/api.service';
@Component({
  selector: 'app-list-database',
  templateUrl: './list-database.component.html',
  styleUrls: ['./list-database.component.scss']
})
export class ListDatabaseComponent implements OnInit {
  constructor(private apiService:ApiService) { }
  dataset_list=[];
  
  ngOnInit(): void {

    this.apiService.getDataset().subscribe(
        logs =>{ this.dataset_list=logs.Data},
        error => console.log(error)
      );

 }
}