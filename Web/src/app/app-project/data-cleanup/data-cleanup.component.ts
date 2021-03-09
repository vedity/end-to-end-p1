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
  activeId = 1;
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
  splitmethodselection = "crossvalidation";
  scaleOperations:any;
  hyperparams = 'sklearn';
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
    this.getScalingOperations();
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

  selectedcolumnswithoperation = [];
  // selectedoperations=[];
  selectedColumn = [];
  selectColumn(event) {
    // if ($(".radioitems:checked").length > 0) {
    //   let selectedoperations = [];
    //   $(".radioitems:checked").each(function () {
    //     selectedoperations.push($(this).val());
    //     $(this).prop("checked", false);
    //   })
    //   this.selectedcolumnswithoperation.push({ ids: this.selectedColumn, operations: selectedoperations })
    // }
    if (event.target.checked) {
      this.selectedColumn.push(event.target.value);
    }
    else {
      var index = this.selectedColumn.indexOf(event.target.value);
      if (index != -1) {
        this.selectedColumn.splice(index, 1);
      }
    }
    $(".radiobutton:checked").prop('checked', false);
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
      console.log(this.columnList);
      setTimeout(() => {
        this.loaderdiv = false;
      }, 10);
    }
    else {
      this.errorHandler(data);
    }
  }

  handling = [];
  selectHandling(event, id) {
    var item = this.handling.find(s => s.column.toString() == this.selectedColumn.toString());
    $("#" + event.target.id).prop('checked', true);
    if (item == undefined) {
      this.handling.push({ column: this.selectedColumn, operation: [id] })
    }
    else {
      item.operation.push(id);
    }
    this.setHandlers();
  }

  setHandlers() {
    let tabid = this.activeId;
    this.selectedColumn.forEach(element => {
      var selectedelem = this.columnList.filter(function (e) {
        if (e.column_id == element) {
          e["handling_" + tabid] = [];
          e["handlingname_" + tabid] = [];
          e["handlingtarget_" + tabid] = [];
          if ($(".radiobutton:checked").length > 0) {
            $(".radiobutton:checked").each(function () {
              e["handling_" + tabid].push($(this).val().toString());
              e["handlingname_" + tabid].push($(this).attr('title'));
              e["handlingtarget_" + tabid].push($(this).prop('id'));
            })
          }
        }
        return e;
      });
      console.log(selectedelem);

    });
  }


  removeHandlers(id, columnid) {
    let tabid = this.activeId;
    var selectedelem = this.columnList.filter(function (e) {
      if (e.column_id == columnid) {
        let val = $("#" + id).val();
        console.log(val);
        e["handling_" + tabid].splice(e["handling_" + tabid].indexOf(val), 1);
        e["handlingname_" + tabid].splice( e["handlingname_" + tabid].indexOf($("#" + id).attr('title')), 1);
        e["handlingtarget_" + tabid].splice(e["handlingtarget_" + tabid].indexOf(id), 1);
      }
      return e;
    });
    console.log(selectedelem);
  }

  removeHandling(id, column) {
    if (this.selectedColumn.length == 1)
      $("#" + id).prop('checked', false);
    this.removeHandlers(id, column);
  }

  tabchange(tabid) {
    $(".checkbox:checked").prop("checked", false);
    this.selectedColumn = [];
    this.getColumnviseOperation();
  }

  getScalingOperations(){
    this.apiService.getScalingOperations().subscribe(
      logs=>this.scaleSuccessHandler(logs),
      error=>this.errorHandler(error)
    )
  }

  scaleSuccessHandler(data)
  {
    if (data.status_code == "200") {
      this.scaleOperations = data.response;
      console.log(this.scaleOperations);
      
    }
    else {
      this.errorHandler(data);
    }
  }

}