import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ActivatedRouteSnapshot, Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ToastrService } from 'ngx-toastr';
import { SchemaMappingApiService } from '../schema-mapping-api.service';
@Component({
  selector: 'app-manage-schema-mapping',
  templateUrl: './manage-schema-mapping.component.html',
  styleUrls: ['./manage-schema-mapping.component.scss']
})
export class ManageSchemaMappingComponent implements OnInit {
  displaytitle = false;
  schemamapping = false;
  navigate_to = "";
  activeId = 0;
  constructor(public apiService: SchemaMappingApiService, public activatedroute: ActivatedRoute, private modalService: NgbModal, public router: Router, private toaster: ToastrService, private http: HttpClient) { }
  title = "Data Detail List";
  dataset_id: any;
  columnlist: any = [];
  project_id: any;
  schema_id: any;
  params: any;
  currentuser: any;
  project_name: any;
  activatedroutedata: any;
  async ngOnInit() {
    this.params = history.state;
    if (this.params.isFromMenu == true) {
      this.getproject();
      $(".openmodal").trigger('click');
    }
    else {
      if (this.params.dataset_id != undefined)
        localStorage.setItem("preprocessing", JSON.stringify(this.params));
      else {
        this.params = localStorage.getItem("preprocessing");
        this.params = JSON.parse(this.params);
      }

      if (this.params.dataset_name != undefined) {
        this.title = this.params.dataset_name;
      }

      if (this.params.project_name != undefined) {
        this.project_name = this.params.project_name;
      }

      this.navigate_to = this.params.navigate_to;
      this.project_id = this.params.project_id;
      if (this.navigate_to == "/dataset") {
        this.displaytitle = true;
      }
      this.dataset_id = this.params.dataset_id;
      this.schema_id = this.params.schema_id;

      this.activatedroute.data.subscribe(data => {
        this.activatedroutedata = data;
        if (this.activatedroutedata.Activeid != undefined)
          this.activeId = this.activatedroutedata.Activeid;
      })
      console.log(this.params);
    }
  }

  projectdata: any;
  setproject(value) {
    console.log(value);
    if (value != "") {
      var projects = this.projectList.filter(function (elem) {
        if (elem.project_id == value)
          return elem
      })
      this.projectdata = projects[0];
    }
    else {
      this.projectdata = undefined
    }
    console.log(this.projectdata);
  }

  setParams() {
    if (this.projectdata != undefined) {
      this.params = {
        dataset_id: this.projectdata.dataset_id,
        dataset_name: this.projectdata.dataset_name,
        project_name: this.projectdata.project_name,
        project_id: this.projectdata.project_id, navigate_to: "/project",
        schema_id: this.projectdata.schema_id
      }
      this.dataset_id = this.params.dataset_id;
      this.schema_id = this.params.schema_id;
      this.title = this.params.dataset_name;
      this.project_name = this.params.project_name;
      this.navigate_to = this.params.navigate_to;
      this.project_id = this.params.project_id;

      localStorage.setItem("preprocessing", JSON.stringify(this.params));

      this.activatedroute.data.subscribe(data => {
        this.activatedroutedata = data;
        if (this.activatedroutedata.Activeid != undefined)
          this.activeId = this.activatedroutedata.Activeid;
      })
      this.modalService.dismissAll();
    }
    else {
      this.toaster.error("Please select any project", "Error");
    }
  }
  projectList: any;
  getproject() {
    this.apiService.getproject().subscribe(
      logs => this.successProjectListHandler(logs),
      error => this.errorHandler(error)
    );
  }

  successProjectListHandler(data) {
    if (data.status_code == "200") {
      this.projectList = data.response;
    }
    else {
      this.projectList = []
    }
  }

  errorHandler(error) {
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      this.toaster.error('Something went wrong', 'Error');
    }
  }

  navigatePage(id) {
    switch (id) {
      case 1:
        this.router.navigate(['/datadetail']);
        break;
      case 2:
        this.router.navigate(['/schema']);
        break;
      case 3:
        this.router.navigate(['/exploration']);
        break;
      case 5:
        this.router.navigate(['/cleanup']);
        break;
      default:
        break;
    }
  }

  ProjectData(projectModal: any) {
    this.modalService.open(projectModal, { size: 'lg', windowClass: 'modal-holder', centered: true });
  }
}