import { Component, HostListener, Input, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { DataTableDirective } from 'angular-datatables';
import { ToastrService } from 'ngx-toastr';
import { DataCleanupApiService } from '../data-cleanup.service';
import { Options } from 'ng5-slider';
import { scaleandsplit, saveAsModal } from './data-cleanup.model';
import { NgForm } from '@angular/forms';
import { isInteractionValid } from '@fullcalendar/core/validation';
@Component({
  selector: 'app-data-cleanup',
  templateUrl: './data-cleanup.component.html',
  styleUrls: ['./data-cleanup.component.scss']
})
export class DataCleanupComponent implements OnInit {
  numberrangeregex = "^[1-9][0]?$|^10$"
  randomstateregex = "^[0-9]{1,5}$"
  f: NgForm;
  @ViewChild(DataTableDirective, { static: false })
  datatableElement: DataTableDirective;
  dtOptions: DataTables.Settings = {};
  activeId = 1;
  scaldata: scaleandsplit = {
    test_ratio: 20,
    split_method: 'cross_validation',
    scaling_op: '0'
  };
  saveAs = new saveAsModal();
  constructor(public apiService: DataCleanupApiService, public toaster: ToastrService, private modalService: NgbModal, public router: Router) { }
  @Input() public dataset_id: any;
  @Input() public title: any;
  @Input() public project_id: any
  @Input() public schema_id: any
  @Input() public project_name: any;
  loaderbox = false;
  loaderdiv = false;

  displaytitle = "false";
  errorStatus = true;
  operationList: any;
  columnList: any;
  holdoutList: any;
  splitmethodselection = "cross_validation";
  scaleOperations: any;
  hyperparams = 'sklearn';
  animation = "progress-dark";
  theme = {
    'border-radius': '5px',
    'height': '40px',
    'background-color': ' rgb(34 39 54)',
    'border': '1px solid #32394e',
    'animation-duration': '20s'
  };

  setCleanUpInterval: any;
  setModelingInterval: any;

  //visibleSelection = 20;
  visibleBarOptions: Options = {
    floor: 0,
    ceil: 100,
    showSelectionBar: true,

  };

  @HostListener('window:resize', ['$event'])
  onResize(event) {
    if (this.datatableElement.dtInstance) {
      this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
        dtInstance.columns.adjust().draw();
      })
    }
  }

  checkvalidation(event, type) {
    let value=event.target.value.toString().trim();
 
    var match = true;
    var regexfortypeinteger = /^[0-9]{1,50}$/;
    var regexfortypefloat = /^([0-9]*[.])?[0-9]+$/;
    var regexfortypefloatbutnotzero = /^-?(?!0)\d+(\.\d+)?$/;
    var regexfortext = /^[A-Za-z]+$/;
    $("#" + event.target.id).removeClass("errorstatus")
    if (value != "") {
      if (type == 1) {
        match = regexfortypeinteger.test(value);
      }
      if (type == 2) {
        match = regexfortypefloat.test(value);
      }
      if (type == 4) {
        match = regexfortext.test(value);
      }
      if (type == 5) {
        if (value != 0)
          match = regexfortypefloat.test(value);
        else
          match = false
      }
      if (!match) {
        $("#" + event.target.id).addClass("errorstatus")
      }
    }
    else{
      $("#" + event.target.id).addClass("errorstatus")
      $("#" + event.target.id).val('');
    }
  }

  ngOnInit(): void {
    if (this.setCleanUpInterval) {
      clearInterval(this.setCleanUpInterval);
    }
    if (this.setModelingInterval) {
      clearInterval(this.setModelingInterval);
    }
    // this.getCheckSplit();
    this.getCldagStatus();
    this.dtOptions = {
      paging: false,
      orderFixed:[[0,'desc']],
     // ordering:false,
      scrollCollapse: true,
      info: false,
      searching: false,
      //scrollX: true,
      scrollY: "57.5vh",
    }
    this.loaderbox = true;
    this.getOpertion();
    this.getColumnList();
    this.getScalingOperations();
    this.getHoldoutList();
    // this.scaldata.test_ratio = 20;
    // this.scaldata.split_method = 'cross_validation';
    // this.scaldata.scaling_op='0'
  }

  getCheckSplit() {

    this.apiService.getCheckSplit(this.project_id, this.schema_id).subscribe(
      logs => this.checksplitSuccessHandler(logs),
      error => this.errorHandler(error)
    )
  }

  getCldagStatus() {

    this.apiService.getCldagStatus(this.project_id).subscribe(
      logs => this.CldagSuccessHandler(logs)
    )
  }

  isEnableCleanup = true;
  CldagSuccessHandler(data) {
    if (data.status_code == "200") {
      this.isEnableCleanup = data.response;
      if (this.isEnableCleanup) {
        if (!this.setCleanUpInterval) {
          this.setCleanUpInterval = setInterval(() => {
            this.getCldagStatus();
          }, 10000);
        }
      }
      else {
        if (this.setCleanUpInterval) {
          clearInterval(this.setCleanUpInterval);
        }
      }
    }
  }

  isEnableModeling = true;
  checksplitSuccessHandler(data) {
    if (data.status_code == "200") {
      this.isEnableModeling = data.response;
      if (this.isEnableModeling) {
        $("#modeling-btn")[0].click();
      }
      else {
        this.errorHandler(data);
      }
      // if (!this.isEnableModeling) {
      //   if (!this.setModelingInterval) {
      //     this.setModelingInterval = setInterval(() => {
      //       this.getCheckSplit();
      //     }, 10000);
      //   }
      // }
      // else {
      //   if (this.setModelingInterval) {
      //     clearInterval(this.setModelingInterval);
      //   }
      // }
    }
    else {
      this.errorHandler(data);
    }
  }

  successHandler(logs) {
    this.loaderbox = false;
  }

  errorHandler(error) {
    this.loaderbox = false;
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

  getHoldoutList() {
    this.apiService.getHoldoutList().subscribe(
      logs => this.holdoutlistsuccessHandler(logs),
      error => this.errorHandler(error)
    )
  }

  holdoutlistsuccessHandler(data) {
    if (data.status_code == "200") {
      this.holdoutList = data.response;
    }
    else {
      this.errorHandler(data);
    }
  }

  selectedcolumnswithoperation = [];
  selectedColumn = [];
  selectColumn(event) {
    $(".customInput").prop('disabled', true).val('').removeClass('errorstatus');
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
      setTimeout(() => {
        this.loaderbox = false;
      }, 10);
    }
    else {
      this.errorHandler(data);
    }
  }

  setInput(operationid, event) {
    var value = event.target.value;
    this.selectedColumn.forEach(element => {
      var input = $("#setInput_" + element + "_" + operationid).val();
      if (input != undefined) {
        $("#setInput_" + element + "_" + operationid).val(value).removeClass("error")

        if ($("#" + event.target.id).hasClass('errorstatus'))
          $("#setInput_" + element + "_" + operationid).addClass("error");
      }
    });
  }

  handling = [];
  selectHandling(event, id) {
    $(".customInput").prop('disabled', true).val('');
    var item = this.handling.find(s => s.column.toString() == this.selectedColumn.toString());
    $("#" + event.target.id).prop('checked', true);
    $("#customInput_" + event.target.id.split('_')[1] + '_' + event.target.id.split('_')[2]).prop('disabled', false);
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
          e["handlinginput_" + tabid] = [];
          if ($(".radiobutton:checked").length > 0) {
            $(".radiobutton:checked").each(function () {
              e["handling_" + tabid].push($(this).val().toString());
              e["handlingname_" + tabid].push($(this).attr('title'));
              e["handlingtarget_" + tabid].push($(this).prop('id'));
              var ids = $(this).prop('id').split('_')
              var val = $("#customInput_" + ids[1] + "_" + ids[2]).val();
              e["handlinginput_" + tabid].push(val);
            })
          }
        }
        return e;
      });
    });
  }

  removeHandlers(id, columnid, tabid) {
    // let tabid = this.activeId;
    var selectedelem = this.columnList.filter(function (e) {
      if (e.column_id == columnid) {
        let val = $("#" + id).val();
        e["handling_" + tabid].splice(e["handling_" + tabid].indexOf(val), 1);
        e["handlingname_" + tabid].splice(e["handlingname_" + tabid].indexOf($("#" + id).attr('title')), 1);
        e["handlingtarget_" + tabid].splice(e["handlingtarget_" + tabid].indexOf(id), 1);
      }
      return e;
    });
  }

  removeHandling(id, column, tabid) {
    if (this.selectedColumn.length == 1)
      $("#" + id).prop('checked', false);
    this.removeHandlers(id, column, tabid);
  }

  errorothertag = false;
  tabchange(event, tabid) {
    $(".checkbox:checked").prop("checked", false);
    this.selectedColumn = [];
    this.getColumnviseOperation();
  }

  reset() {
    $(".checkbox:checked").prop("checked", false);
    $(".customInput").prop('disabled', true).val('').removeClass('errorstatus');
    $(".radiobutton:checked").prop('checked', false);
    this.selectedColumn = [];
    this.getColumnList();
    this.getColumnviseOperation();
    if (this.isEnableCleanup) {
      if (!this.setCleanUpInterval) {
        this.setCleanUpInterval = setInterval(() => {
          this.getCldagStatus();
        }, 10000);
      }
    }

    // if (!this.isEnableModeling) {
    //   if (!this.setModelingInterval) {
    //     this.setModelingInterval = setInterval(() => {
    //       this.getCheckSplit();
    //     }, 10000);
    //   }
    // }
  }

  getScalingOperations() {
    this.apiService.getScalingOperations().subscribe(
      logs => this.scaleSuccessHandler(logs),
      error => this.errorHandler(error)
    )
  }

  scaleSuccessHandler(data) {
    if (data.status_code == "200") {
      this.scaleOperations = data.response;
    }
    else {
      this.errorHandler(data);
    }
  }

  groupBy(data, key) {
    return data.reduce(function (rv, x) {
      (rv[x[key]] = rv[x[key]] || []).push(x);
      return rv;
    }, []);
  };

  fianlarray = [];
  errorflag: boolean;
  saveHanlers(isSave, smallDataModal) {

    this.errorflag = false;
    this.fianlarray = [];
    let arrayhandlers = [];
    if ($(".errorstatus").length > 0) {
      this.toaster.error("Please enter valid input", 'Error')
    } else {
      if ($(".handlingitem").length > 0) {
        if ($(".error").length == 0) {
          $(".handlingitem").each(function () {
            var id = $(this).prop('id').split('_');
            var columnid = id[1];
            var operationid = id[2];
            var value = $("#setInput_" + columnid + "_" + operationid).val();
            arrayhandlers.push({ column_id: columnid, selected_handling: operationid, values: value });
          })
          var handlers = this.groupBy(arrayhandlers, 'column_id');
          for (var item in handlers) {
            let selectedhandling = [];
            let values = [];
            for (var childitem of handlers[item]) {
              selectedhandling.push(parseInt(childitem.selected_handling));
              if (childitem.values == "")
                this.errorflag = true;

              if (childitem.values == undefined) {
                childitem.values = '';
              }
              values.push(childitem.values);
            }
            this.fianlarray.push({ "column_id": [parseInt(item)], "selected_handling": selectedhandling, "values": values })
          }
          if (this.errorflag == true) {
            this.toaster.error("Please enter required input", 'Error')
          }
          else {
            if (isSave == 'False') {
              this.loaderdiv = true;
              this.apiService.saveOperations(this.schema_id, this.dataset_id, this.project_id, isSave, this.fianlarray).subscribe(
                logs => this.saveSuccessHandlers(logs),
                error => this.errorHandler(error)
              )
            }
            else {
              this.saveAs = new saveAsModal();
              this.saveAs.isPrivate = true;
              this.modalService.open(smallDataModal, { size: 'sm', windowClass: 'modal-holder', centered: true });
            }
          }
        }
        else
          this.toaster.error("Please enter valid input", 'Error')

      }
      else {
        if (isSave == 'False') {
          this.toaster.error("Please select any handlers", 'Error')
        }
        else {
          this.saveAs = new saveAsModal();
          this.saveAs.isPrivate = true;
          this.modalService.open(smallDataModal, { size: 'sm', windowClass: 'modal-holder', centered: true });
        }
      }

    }
  }

  saveSuccessHandlers(data) {
    if (data.status_code == "200") {
      $(".checkbox:checked").prop("checked", false);
      $(".customInput").prop('disabled', true).val('').removeClass('errorstatus');
      $(".radiobutton:checked").prop('checked', false);
      this.selectedColumn = [];
      this.getColumnList();
      this.getColumnviseOperation();
      this.toaster.success(data.error_msg, 'Success')
      this.getCldagStatus();
      this.loaderdiv = false;

    }
    else {
      this.errorHandler(data);
    }
  }

  response: any;
  saveScale() {
    this.loaderdiv = true;

    var user = JSON.parse(localStorage.getItem("currentUser"));
    if (this.scaldata.split_method == "cross_validation") {
      this.response = {
        schema_id: this.schema_id,
        dataset_id: this.dataset_id,
        project_id: this.project_id,
        user_name: user.username,
        scaling_op: this.scaldata.scaling_op,
        split_method: this.scaldata.split_method,
        cv: parseInt(this.scaldata.cv.toString()),
        valid_ratio: 0,
        test_ratio: this.scaldata.test_ratio / 100,
        random_state: this.scaldata.random_state
      }
    }
    else {
      this.response = {
        schema_id: this.schema_id,
        dataset_id: this.dataset_id,
        project_id: this.project_id,
        user_name: user.username,
        scaling_op: this.scaldata.scaling_op,
        split_method: this.scaldata.split_method,
        cv: 0,
        valid_ratio: parseInt(this.scaldata.split_ratio.toString().split('-')[1]) / 100,
        test_ratio: parseInt(this.scaldata.split_ratio.toString().split('-')[2]) / 100,
        random_state: this.scaldata.train_random_state
      }
    }
    
    this.apiService.savescalingOpertion(this.response).subscribe(
      logs => this.savescalSuccessHandlers(logs),
      error => this.errorHandler(error)
    )
  }

  savescalSuccessHandlers(data) {
    if (data.status_code == "200") {
      this.toaster.success(data.error_msg, 'Success')
      // this.getCheckSplit();
      this.loaderdiv = false;


    }
    else {
      this.errorHandler(data);
    }
  }

  checkuniquedatasetname(event) {
    var val = event.target.value;
    if (val != "") {
      this.apiService.checkUniqueDatasetName(val).subscribe(
        logs => this.successUniquedatasetynamevalidation(logs, event.target),
        error => this.errorHandler(error)
      );
    }
    else {
      this.datasetnameuniqueerror = false;
    }
  }

  datasetnameuniqueerror: any = false;
  successUniquedatasetynamevalidation(data, target) {
    if (data.response == 'false') {
      this.datasetnameuniqueerror = true;
      target.className = target.className.replace("ng-valid", " ");
      target.className = target.className + " ng-invalid";
    }
    else {
      this.datasetnameuniqueerror = false;
      target.className = target.className.replace("ng-invalid", " ");
      target.className = target.className + " ng-valid";
    }
  }

  saveAsDataset(flag) {
    let visibility = "";
    if (this.saveAs.isPrivate == true)
      visibility = 'private';
    else
      visibility = 'public';
      this.loaderdiv = true;

    this.apiService.saveasOperations(this.schema_id, this.dataset_id, this.project_id, this.saveAs.dataset_name, visibility, this.saveAs.description, flag, this.fianlarray)
      .subscribe(
        logs => this.saveAsSuccessHandlers(logs),
        error => this.errorHandler(error)
      )
  }

  saveAsSuccessHandlers(data) {
    if (data.status_code == "200") {
      $(".checkbox:checked").prop("checked", false);
      $(".customInput").prop('disabled', true).val('').removeClass('errorstatus');
      $(".radiobutton:checked").prop('checked', false);
      this.selectedColumn = [];
      this.getColumnList();
      this.getColumnviseOperation();
      this.toaster.success(data.error_msg, 'Success')
      this.modalService.dismissAll();
      this.getCldagStatus();
      this.loaderdiv = false;

    }
    else {
      this.errorHandler(data);
    }
  }

  smallModal(smallDataModal: any) {
    this.modalService.open(smallDataModal, { size: 'sm', windowClass: 'modal-holder', centered: true });
  }
}