import { Component, HostListener, Input, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { DataTableDirective } from 'angular-datatables';
import { ToastrService } from 'ngx-toastr';
import { Subject } from 'rxjs';
import { SchemaMappingApiService } from '../schema-mapping-api.service';
@Component({
  selector: 'app-create-schema-mapping',
  templateUrl: './create-schema-mapping.component.html',
  styleUrls: ['./create-schema-mapping.component.scss']
})
export class CreateSchemaMappingComponent implements OnInit {
  @ViewChild(DataTableDirective, { static: false })
  datatableElement: DataTableDirective;
  dtOptions: DataTables.Settings = {};
  dtTrigger: Subject<any> = new Subject<any>();

  constructor(public apiService: SchemaMappingApiService, public router: Router, public toaster: ToastrService, private modalService: NgbModal) { }
  @Input() public dataset_id: any;
  @Input() public title: any;
  @Input() public project_id: any;
  @Input() public schema_id: any;
  @Input() public project_name: any;
  loaderdiv = false;
  saveAs: any = {
    isPrivate: false,
    dataset_name: "",
    description: ""
  }
  selectdatetimeoption = "";
  filter: boolean = true;
  displaytitle = "false";
  columnattrList: any = [];
  datatypeList: any = [];
  datetimeoptionList: any = [];
  datasetSchema: any = [];
  Originaldata: any = [];
  displaydiv = false;
  animation = "progress-dark";
  theme = {
    'border-radius': '5px',
    'height': '40px',
    'background-color': ' rgb(34 39 54)',
    'border': '1px solid #32394e',
    'animation-duration': '20s'
  };

  @HostListener('window:resize', ['$event'])
  onResize(event) {
    if (this.datatableElement.dtInstance) {
      this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
        dtInstance.columns.adjust().draw();
      })
    }
  }

  checkuniquecolumnname(event, id) {
    // console.log(event.target.value, id);
    if (event.target.value != "") {
      this.apiService.checkuniqueColumnName(event.target.value, this.schema_id).subscribe(
        logs => this.checkuniquesuccessHandler(logs, id),
        error => this.errorHandler(error)
      )
    }
    else {
      $("#td_" + id).removeClass("errorstatus");
      $(".changeerror_" + id).text('');
    }
  }

  checkuniquesuccessHandler(data, id) {
    // console.log(data);
    if (data.status_code == '500') {
      $("#td_" + id).addClass("errorstatus");
      $(".changeerror_" + id).text(data.error_msg);
    }
    else {
      $("#td_" + id).removeClass("errorstatus");
      $(".changeerror_" + id).text('');
    }
  }



  ngOnInit(): void {
    this.dtOptions = {
      paging: false,
      // ordering: true,
      scrollCollapse: true,
      info: false,
      // searching: false,
      scrollX: true,
      scrollY: "calc(100vh - 450px)",
    }
    this.displaydiv = true;
    this.getColumnAttributeList();
    this.getFeatureSelection();
    // console.log(this.project_id, this.dataset_id);
    this.getSchema(this.project_id, this.dataset_id, this.schema_id);
  }

  getSchema(projectid, datasetid, schemaid) {
    this.apiService.getDatasetSchema(projectid, datasetid, schemaid).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error)
    )
  }

  successHandler(logs) {
    this.displaydiv = false;
    this.datasetSchema = logs.response;
    this.Originaldata = logs.response;
    setTimeout(() => {
      if (!this.datatableElement.dtInstance) {
        this.dtTrigger.next();
        this.datatableElement.dtInstance.then((dtInstance: DataTables.Api) => {
          dtInstance.columns().every(function () {
            const that = this;
            $('#input_' + this.index("visible")).on('keyup change', function () {
              console.log(this['value']);
              if (that.search() !== this['value']) {
                that
                  .search(this['value'])
                  .draw();
              }
            });
          });
        });
      }

    }, 0);
  }



  getColumnAttributeList() {
    this.apiService.getColumnAttributes().subscribe(
      logs => this.columnattributesSuccessHandler(logs),
      error => this.errorHandler(error)
    )
  }

  // getDataTypeList() {
  //   this.apiService.getDatatypeList().subscribe(
  //     logs => this.DatatypeSuccessHandler(logs),
  //     error => this.errorHandler(error)
  //   )
  // }

  // DatatypeSuccessHandler(data) {
  //   this.datatypeList = data.response.attribute_name;
  // }

  currentmodelId: any;
  DatatypeModal(dateModal: any, item, i) {
    console.log(item);
    this.currentmodelId = i;
    $("#datetimeformattooltip_"+i).prop("hidden",true);

    if (item == "timestamp")
      this.modalService.open(dateModal, { size: 'sm', windowClass: 'modal-holder', centered: true });
  }

  savetimestamp() {
    console.log(this.currentmodelId);
    console.log(this.selectdatetimeoption);
    if (this.selectdatetimeoption != "") {
      if (this.selectdatetimeoption != 'Custom') {
        $("#datetimeformat_" + this.currentmodelId).val(this.selectdatetimeoption);
        $("#datetimeformattooltip_"+this.currentmodelId).prop("hidden",false);
        this.currentmodelId = '';
        this.selectdatetimeoption = '';
        this.modalService.dismissAll();
      }
      else {
        var format = $("#custome-dateformate").val();
        if (format != "") {
          $("#datetimeformat_" + this.currentmodelId).val(format);
          $("#datetimeformattooltip_"+this.currentmodelId).prop("hidden",false);
          this.currentmodelId = '';
          this.selectdatetimeoption = '';
          this.modalService.dismissAll();
        }
        else {
          this.toaster.error("Please enter custom datetime format", "Error");
        }
      }
    }
    else {
      this.toaster.error("Please select any datetime format", "Error");
    }


  }

  featuresList:any;
  getFeatureSelection(){
    this.apiService.getfeatureSelection().subscribe(
      logs=>this.SuccessFeatureSelection(logs),
      error=>this.errorHandler(error)
    )
  }

  SuccessFeatureSelection(data){
if(data.status_code=="200")
{
  this.featuresList=data.response;
  console.log(this.featuresList);
  
} 
else{
  this.errorHandler(data);
} }

  currentcontet="";
  displaytooltip(tooltip,id){
      this.currentcontet=$("#datetimeformat_"+id).val().toString();
      tooltip.open();
  }

  hidetooltip(tooltip){
     tooltip.close();
  }

  columnattributesSuccessHandler(data) {
    this.columnattrList = data.response.column_attribute;
    this.datatypeList = data.response.datatype;
    this.datetimeoptionList = data.response.datetime_options;

  }

  errorHandler(error) {
    this.loaderdiv = false;
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }

  save() {
    if ($(".schema-mapping").find(".errorstatus").length > 0) {
      this.toaster.error('Please enter valid input', 'Error');
    }
    else {
      let savedata = [];
      this.loaderdiv = true;
      this.datasetSchema.forEach((element, index) => {
        var txt_column_name = $("#columnname_" + index).val();
        txt_column_name = txt_column_name == undefined ? '' : txt_column_name.toString();
        var txt_column_attribute = $("#selectattr_" + index + " :selected").val();
        txt_column_attribute = txt_column_attribute == undefined ? '' : txt_column_attribute.toString();
        var txt_datatype = $("#selectdatatype_" + index + " :selected").val();
        txt_datatype = txt_datatype == undefined ? '' : txt_datatype.toString();
 var date_format=$("#datetimeformat_" + index).val();
 date_format = date_format == undefined ? '' : date_format.toString();
        if (txt_column_name == this.Originaldata[index].change_column_name && txt_column_attribute == this.Originaldata[index].column_attribute && txt_datatype == this.Originaldata[index].data_type) {
        }
        else {
          if (txt_column_name != element.column_name) {
            if(txt_datatype=='timestamp' && date_format==''){
              this.toaster.error('Please select any datetime format', 'Error');
            }
            else{
              var schema = {
                change_column_name: txt_column_name,
                index: element.index,
                column_name: element.column_name,
                data_type: txt_datatype,
                date_format:date_format,
                column_attribute: txt_column_attribute
              }
              savedata.push(schema);
            }
          }
        }
      });
      if (savedata.length > 0) {
        savedata.push(this.datasetSchema[0]);

         console.log(savedata);
         this.loaderdiv = false;

        this.apiService.saveDatasetSchema(this.dataset_id, this.project_id, this.schema_id, { data: savedata }).subscribe(logs => this.savesuccessHandler(logs), error => this.errorHandler(error));

      } else {
        this.loaderdiv = false;
        this.toaster.error('Please enter valid input', 'Error');

      }
    }
  }

  // savaAs() {
  //   if ($(".schema-mapping").find(".errorstatus").length > 0) {
  //     this.toaster.error('Please enter valid input', 'Error');
  //   }
  //   else {
  //     this.loaderdiv = true;
  //     let savedata = [];
  //     this.datasetSchema.forEach((element, index) => {
  //       var txt_column_name = $("#columnname_" + index).val().toString();
  //       var txt_column_attribute = $("#selectattr_" + index + " :selected").val().toString();
  //       // if(txt_column_name=="" && txt_column_attribute==""){
  //       // }
  //       // else{
  //       //   if(txt_column_name!=element.column_name){
  //       var schema = {
  //         change_column_name: txt_column_name,
  //         column_name: element.column_name,
  //         data_type: element.data_type,
  //         column_attribute: txt_column_attribute
  //       }
  //       savedata.push(schema);
  //       //   }
  //       // }
  //     });
  //     // console.log(this.saveAs);
  //     this.apiService.saveasDatasetSchema(this.project_id, this.saveAs.dataset_name, this.saveAs.description, this.saveAs.isPrivate, "Save as", { data: savedata }).subscribe(logs => this.savesuccessHandler(logs), error => this.errorHandler(error));

  //   }

  // }

  savesuccessHandler(data) {
    this.loaderdiv = false;
    if (data.status_code == "200") {
      this.toaster.success(data.error_msg, "Success");
      this.reset();

    }
    else
      this.errorHandler(data);
  }

  reset() {
    let currentUrl = this.router.url;
    this.router.routeReuseStrategy.shouldReuseRoute = () => false;
    this.router.onSameUrlNavigation = 'reload';
    this.router.navigate([currentUrl]);

  }

  changeattrinute(value, i) {
    $("#tr_" + i).removeClass("target-selected");
    if (value == "target") {
      $("#tr_" + i).addClass("target-selected");
    }
  }

  checksame(columnname, newname, index) {
    $("#td_" + index).removeClass("errorstatus");
    if (columnname == newname)
      $("#td_" + index).addClass("errorstatus");
  }

  smallModal(smallDataModal: any) {
    this.modalService.open(smallDataModal, { size: 'sm', windowClass: 'modal-holder', centered: true });
  }

  displayfilter() {
    this.filter = !this.filter;
    $('.filter').val('').trigger('change');
  }

  largeModal(schemarecommodate: any) {
    this.modalService.open(schemarecommodate, { size: 'lg', windowClass: 'modal-holder', centered: true });
  }
}