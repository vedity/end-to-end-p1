import { Component, Input, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ToastrService } from 'ngx-toastr';
import { SchemaMappingApiService } from '../schema-mapping-api.service';
@Component({
  selector: 'app-create-schema-mapping',
  templateUrl: './create-schema-mapping.component.html',
  styleUrls: ['./create-schema-mapping.component.scss']
})
export class CreateSchemaMappingComponent implements OnInit {

  constructor(public apiService: SchemaMappingApiService, public toaster: ToastrService,private modalService: NgbModal) { }
  @Input() public dataset_id: any;
  @Input() public title: any;
  @Input() public project_id: any
  loaderdiv=false;
  saveAs:any={
    isPrivate:false,
    dataset_name:"",
    description:""

  }
  displaytitle = "false";
  columnattrList: any = [];
  datatypeList: any = [];
  datasetSchema: any = [];
  finaldata:any=[];
  displaydiv=false;
  animation = "progress-dark";
 theme = {
     'border-radius': '5px',
     'height': '40px',
     'background-color': ' rgb(34 39 54)',
     'border': '1px solid #32394e',
     'animation-duration': '20s'
 };

  ngOnInit(): void {
    this.displaydiv=true;
    this.getColumnAttributeList();
    console.log(this.project_id,this.dataset_id);
    
    this.getSchema(this.project_id,this.dataset_id);
  }

  getSchema(projectid,datasetid) {
    this.apiService.getDatasetSchema(projectid,datasetid).subscribe(
      logs => this.successHandler(logs),
      error => this.errorHandler(error)
    )
  }

  successHandler(logs) {
    this.displaydiv=false;
    this.datasetSchema = logs.response;
    this.finaldata=logs.response;
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
  }

  columnattributesSuccessHandler(data) {
    this.columnattrList = data.response.column_attribute;
  }

  errorHandler(error) {
    this.loaderdiv=false;
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }

  save(){
    if($(".schema-mapping").find(".errorstatus").length>0){
      this.toaster.error('Please enter valid input', 'Error');
    }
    else{
     let savedata=[];
     this.loaderdiv=true;
      this.datasetSchema.forEach((element,index) => {
        var txt_column_name=$("#columnname_"+index).val().toString();
        var txt_column_attribute=$("#selectattr_"+index+" :selected").val().toString();
        if(txt_column_name=="" && txt_column_attribute==""){

        }
        else{
          if(txt_column_name!=element.column_name){
            var schema= {change_column_name:txt_column_name,
            column_name:element.column_name,
            data_type:element.data_type,
            column_attribute:txt_column_attribute}
            savedata.push(schema);
          }
        }
     
      });
      if(savedata.length>0)
      this.apiService.saveDatasetSchema(this.dataset_id,this.project_id,{data:savedata}).subscribe(logs=>this.savesuccessHandler(logs),error=>this.errorHandler(error));
      else{
     this.loaderdiv=false;
        this.toaster.error('Please enter valid input', 'Error');

      }
    }
  }

  savaAs(){
    if($(".schema-mapping").find(".errorstatus").length>0){
      this.toaster.error('Please enter valid input', 'Error');
    }
    else{
      this.loaderdiv=true;
     let savedata=[];
      this.datasetSchema.forEach((element,index) => {
        var txt_column_name=$("#columnname_"+index).val().toString();
        var txt_column_attribute=$("#selectattr_"+index+" :selected").val().toString();
        // if(txt_column_name=="" && txt_column_attribute==""){
        // }
        // else{
        //   if(txt_column_name!=element.column_name){
            var schema= {change_column_name:txt_column_name,
            column_name:element.column_name,
            data_type:element.data_type,
            column_attribute:txt_column_attribute}
            savedata.push(schema);
        //   }
        // }
      });
      console.log(this.saveAs);
      this.apiService.saveasDatasetSchema(this.project_id,this.saveAs.dataset_name,this.saveAs.description,this.saveAs.isPrivate,"Save as",{data:savedata}).subscribe(logs=>this.savesuccessHandler(logs),error=>this.errorHandler(error));
      
    }
  
  }

  savesuccessHandler(data){
    this.loaderdiv=false;
    if (data.status_code == "200"){
      this.toaster.success(data.error_msg,"Success");
      this.getSchema(this.project_id,this.dataset_id);

    }
    else
      this.errorHandler(data);
  }

  reset(){
    this.getSchema(this.project_id,this.dataset_id);

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

  smallModal(smallDataModal: any) {
    this.modalService.open(smallDataModal, { size: 'sm',windowClass:'modal-holder', centered: true });
  }
}