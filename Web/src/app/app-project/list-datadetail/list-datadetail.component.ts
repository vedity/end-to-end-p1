import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
    selector: 'app-list-datadetail',
    templateUrl: './list-datadetail.component.html',
    styleUrls: ['./list-datadetail.component.scss']
})
export class ListDatadetailComponent implements OnInit {


    constructor(public apiService:ApiService,public router:Router) { }
    transactions: any;
    ngOnInit() {
        this.apiService.getDataDetails().subscribe(
            logs =>{ this.transactions=logs.Dataset},
            error => console.log(error)
          );
    }

    mapping(){
        this.router.navigate(['schema/create']);
    }
    
}