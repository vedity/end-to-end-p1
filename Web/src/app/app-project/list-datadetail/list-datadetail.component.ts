import { Component, OnInit } from '@angular/core';
import { ApiService } from '../list-project/api.service';
@Component({
  selector: 'app-list-datadetail',
  templateUrl: './list-datadetail.component.html',
  styleUrls: ['./list-datadetail.component.scss']
})
export class ListDatadetailComponent implements OnInit {
  constructor(private apiService:ApiService) { }
  transactions: any;
  ngOnInit() {
    this.apiService.getDataDetails().subscribe(
        logs =>{ this.transactions=logs.Dataset},
        error => console.log(error)
      );
}
}