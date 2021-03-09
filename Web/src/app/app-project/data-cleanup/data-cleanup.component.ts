import { Component, HostListener, Input, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { DataTableDirective } from 'angular-datatables';
import { ToastrService } from 'ngx-toastr';
import { DataCleanupApiService } from '../data-cleanup.service';
@Component({
  selector: 'app-data-cleanup',
  templateUrl: './data-cleanup.component.html',
  styleUrls: ['./data-cleanup.component.scss']
})
export class DataCleanupComponent implements OnInit {

  @ViewChild(DataTableDirective, { static: false })
  datatableElement: DataTableDirective;
  dtOptions: DataTables.Settings = {};
  activeId=1;
  constructor(public apiService: DataCleanupApiService, public toaster: ToastrService, private modalService: NgbModal, public router: Router) { }
  @Input() public dataset_id: any;
  @Input() public title: any;
  @Input() public project_id: any
  @Input() public schema_id: any
  loaderdiv = false;
  displaytitle = "false";
  errorStatus = true;
  operationList: any;
  columnList: any;
  splitmethodselection="crossvalidation";
  hyperparams='sklearn';
  animation = "progress-dark";
  theme = {
    'border-radius': '5px',
    'height': '40px',
    'background-color': ' rgb(34 39 54)',
    'border': '1px solid #32394e',
    'animation-duration': '20s'
  };

  ngOnInit(): void {
    this.dtOptions = {
      paging: false,
      ordering: false,
      scrollCollapse: true,
      info: false,
      searching: false,
      //scrollX: true,
      scrollY: "52vh",
    }
    this.loaderdiv = true;
    this.getOpertion();
    this.getColumnList();
  }


  successHandler(logs) {
    this.loaderdiv = false;
  }

  errorHandler(error) {
    this.loaderdiv = false;
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }

  getOpertion() {
    this.apiService.getOperation().subscribe(
      logs => this.operationlistsuccessHandler(logs),
      error => this.errorHandler(error)
    )
  }

  operationlistsuccessHandler(data) {
    if (data.status_code == "200") {
      this.operationList = data.response;
    }
    else {
      this.errorHandler(data);
    }
  }

  selectedcolumnswithoperation=[];
 // selectedoperations=[];
  selectedColumn = [];
  selectColumn(event) {
    if($(".radioitems:checked").length>0){
      let selectedoperations=[];
      $(".radioitems:checked").each(function(){
       selectedoperations.push($(this).val());
      $(this).prop("checked",false);
      })
      this.selectedcolumnswithoperation.push({ids:this.selectedColumn,operations:selectedoperations})
    }

    console.log("selectedcolumnswithoperation",this.selectedcolumnswithoperation);
   
   
    if (event.target.checked) {
      this.selectedColumn.push(event.target.value);
    }
    else {
      var index = this.selectedColumn.indexOf(event.target.value);
      if (index != -1) {
        this.selectedColumn.splice(index, 1);
      }
    }
    this.getColumnviseOperation();
  }

  getColumnviseOperation() {
    let obj = {
      dataset_id: this.dataset_id,
      schema_id: this.schema_id,
      column_ids: this.selectedColumn.toString()
    }
    this.apiService.getColumnviseOperations(obj).subscribe(
      logs => this.columnviseoperationsuccessHandler(logs),
      error => this.errorHandler(error)
    )
  }

  operationIds = [];
  columnviseoperationsuccessHandler(data) {
    this.operationIds = [];
    if (data.status_code == "200") {
      for (var i in data.response)
        this.operationIds.push(data.response[i].id);
    }
    $(".parentitem").removeClass('hidden');
    setTimeout(() => {
      this.operationList.forEach(element => {
        if ($(".parentitem_" + element.id).find(".displaychilditem").length == 0) {
          $(".parentitem_" + element.id).addClass("hidden");
        };
      });
    }, 10);
  }

  getColumnList() {
    this.apiService.getColumnList(this.schema_id).subscribe(
      logs => this.columnlistsuccessHandler(logs),
      error => this.errorHandler(error)
    )
  }

  columnlistsuccessHandler(data) {
    if (data.status_code == "200") {
      this.columnList = data.response;
      setTimeout(() => {
        this.loaderdiv = false;

      }, 10);
    }
    else {
      this.errorHandler(data);
    }
  }

handling=[];
  selectHandling(event,id,name){
    var item=this.handling.find(s=>s.column.toString()==this.selectedColumn.toString());
   if($("#"+event.target.id).data("waschecked")){
     $("#"+event.target.id).prop('checked',false);
     $("#"+event.target.id).data('waschecked',false);
     this.selectedColumn.forEach(element => {
      $("#handling_"+element).find($("#handlingitem_"+id)).remove();
     });
   }
   else{
    $("#"+event.target.id).prop('checked',true);
    $("#"+event.target.id).data('waschecked',true);
    this.selectedColumn.forEach(element => {
      console.log(element);
      var html='<div class="handling" id="handlingitem_'+id+'"><p>'+name+'&nbsp;<a href="javascript:void(0);"  id="trash_'+id+'"> <i class=" bx bx-trash" (click)="removeHandling('+id+','+element+','+event.target.id+');"></i></a></p></div>'
      $("#handling_"+element).append(html);
    });
if(item==undefined){
  this.handling.push({column:this.selectedColumn,operation:[id]})
}
else{
  item.operation.push(id);
}
   }
  }


  removeHandling(handling,column,target){
    $("#handling_"+column).find($("#handlingitem_"+handling)).remove();
    $("#"+target).prop('checked',false);
    $("#"+target).data('waschecked',false);
   }
  
}