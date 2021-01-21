import { Component, ErrorHandler, Input, OnInit } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { SchemaMappingApiService } from '../schema-mapping-api.service';

@Component({
  selector: 'app-create-schema-mapping',
  templateUrl: './create-schema-mapping.component.html',
  styleUrls: ['./create-schema-mapping.component.scss']
})
export class CreateSchemaMappingComponent implements OnInit {

  constructor(public apiService: SchemaMappingApiService, public toaster: ToastrService) { }
  @Input() public dataset_id: any;
  @Input() public title: any;
  @Input() public project_id: any;

  displaytitle = "false";
  columnattrList: any = [];
  datatypeList: any = [];
  datasetSchema: any = [];
  ngOnInit(): void {
    this.getColumnAttributeList();
    //this.getDataTypeList()
    this.getSchema(this.dataset_id);
  }

  getSchema(datasetid) {
    this.apiService.getDatasetSchema(datasetid).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error)
    )
  }

  successHandler(logs) {
    console.log(logs.response);
    this.datasetSchema = logs.response;
  }

  getColumnAttributeList() {
    this.apiService.getColumnAttributes().subscribe(
      logs => this.columnattributesSuccessHandler(logs),
      error => this.errorHandler(error)
    )
  }

  getDataTypeList() {
    this.apiService.getDatatypeList().subscribe(
      logs => this.DatatypeSuccessHandler(logs),
      error => this.errorHandler(error)
    )
  }
  DatatypeSuccessHandler(data) {
    this.datatypeList = data.response.attribute_name;
    console.log(this.datatypeList);

  }

  columnattributesSuccessHandler(data) {
    this.columnattrList = data.response.column_attribute;
  }

  errorHandler(error) {
    console.log(error);
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      console.log(error);
      this.toaster.error('Something went wrong', 'Error');
    }
  }

  save(){
    if($(".schema-mapping").find(".errorstatus").length>0){
      this.toaster.error('Please enter valid input', 'Error');

    }
    else{
     let savedata=[];
      this.datasetSchema.forEach((element,index) => {
        // let schema=new schemamapping();
       var schema= {change_column_name:$("#columnname_"+index).val().toString(),
        column_name:element.column_name,
        data_type:element.column_attribute,
        column_attribute:$("#selectattr_"+index+" :selected").val().toString()}
        savedata.push(schema);
      });
      console.log(savedata);
      this.apiService.saveDatasetSchema(this.dataset_id,this.project_id,{data:savedata});
    }
  }

  reset(){

  }


  changeattrinute(value,i){
    $("#tr_"+i).removeClass("target-selected");
    if(value=="target"){
      $("#tr_"+i).addClass("target-selected");
    }
  }

  checksame(columnname,newname,index){
    $("#td_"+index).removeClass("errorstatus");
    if(columnname==newname)
    $("#td_"+index).addClass("errorstatus");
  }
}

export class schemamapping{
  column_name:string;
  column_attribute?:string;
  change_column_name?:string;
  data_type:string;

}