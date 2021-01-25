import { Component, ErrorHandler, Input, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ToastrService } from 'ngx-toastr';
import { DataExplorationApiService } from '../data-exploration.service';

@Component({
  selector: 'app-data-visualization',
  templateUrl: './data-visualization.component.html',
  styleUrls: ['./data-visualization.component.scss']
})
export class DataVisualizationComponent implements OnInit {

  constructor(public apiService: DataExplorationApiService, public toaster: ToastrService,private modalService: NgbModal) { }
  @Input() public dataset_id: any;
  @Input() public title: any;
  @Input() public project_id: any
  loaderdiv=false;
  displaytitle = "false";




  columnlabelChartexpand:any;
  scalterChart:any;
  boxplotChart:any;
  countplotChart:any;
  heatmapchart:any;



  selectValue=[];
 animation = "progress-dark";
 theme = {
     'border-radius': '5px',
     'height': '40px',
     'background-color': ' rgb(34 39 54)',
     'border': '1px solid #32394e',
     'animation-duration': '20s'

 };

  ngOnInit(): void {
//this.loaderdiv=true;
this.selectValue = ['Alaska', 'Hawaii', 'California', 'Nevada', 'Oregon', 'Washington', 'Arizona'];
 this.columnlabelChartexpand = {
  chart: {
      height:'500px',
      width: '100%',
      type: 'bar',
      // offsetX: 0,
      // offsetY: 0,
      toolbar: {
          show: true
      },
      selection: {
        enabled: true
      }
  },
  dataLabels: {
      enabled:false,
  },
  colors: ['#34c38f'],
  
  series: [{
      name: 'Yearly Income',
      data: [7889081942.0, 3783083166.0, 5383083166.0, 2383083166.0, 1983083166.0, 6783083166.0, 4583083166.0, 5383083166.0, 2383083166.0, 5383083166.0]
  }],
  xaxis: {
      categories: ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
      position: 'bottom',
     
      

  },
  yaxis: {
      categories: [7889081942.0, 3783083166.0, 5383083166.0, 2383083166.0, 1983083166.0, 6783083166.0, 4583083166.0, 5383083166.0, 2383083166.0, 5383083166.0],
      position: 'left',
      labels: {
          show: true,
        align: 'right',
        minWidth: 0,
        maxWidth: 160,
      },
      offsetX: 0,
      offsetY: 0,

  },

  legend: {
      show: true,
      offsetX: 0,
      offsetY: 0,
  }
  
};

this.scalterChart  = {
  series: [
    {
      name: "TEAM 1",
      data: this.generateDayWiseTimeSeries(
        new Date("11 Feb 2017 GMT").getTime(),
        20,
        {
          min: 10,
          max: 60
        }
      )
    },
    {
      name: "TEAM 2",
      data: this.generateDayWiseTimeSeries(
        new Date("11 Feb 2017 GMT").getTime(),
        20,
        {
          min: 10,
          max: 60
        }
      )
    },
    // {
    //   name: "TEAM 3",
    //   data: this.generateDayWiseTimeSeries(
    //     new Date("11 Feb 2017 GMT").getTime(),
    //     30,
    //     {
    //       min: 10,
    //       max: 60
    //     }
    //   )
    // },
    // {
    //   name: "TEAM 4",
    //   data: this.generateDayWiseTimeSeries(
    //     new Date("11 Feb 2017 GMT").getTime(),
    //     10,
    //     {
    //       min: 10,
    //       max: 60
    //     }
    //   )
    // },
    // {
    //   name: "TEAM 5",
    //   data: this.generateDayWiseTimeSeries(
    //     new Date("11 Feb 2017 GMT").getTime(),
    //     30,
    //     {
    //       min: 10,
    //       max: 60
    //     }
    //   )
    // }
  ],
  chart: {
    height: 350,
    type: "scatter",
    zoom: {
      type: "xy"
    },
   
  },
  dataLabels: {
    enabled: false
  },
  grid: {
    xaxis: {
      lines: {
        show: true
      }
    },
    yaxis: {
      lines: {
        show: true
      }
    }
  },
  xaxis: {
    type: "datetime"
  },
  yaxis: {
    max: 70
  }
};

this.boxplotChart = {
  series: [
    {
      name: "candle",
      data: 
      [
        {
          x: new Date(1538778600000),
          y: [6629.81, 6650.5, 6623.04, 6633.33]
        },
        {
          x: new Date(1538780400000),
          y: [6632.01, 6643.59, 6620, 6630.11]
        },
        {
          x: new Date(1538780400000),
          y: [6630.71, 6648.95, 6623.34, 6635.65]
        },
        {
          x: new Date(1538784000000),
          y: [6635.65, 6651, 6629.67, 6638.24]
        },
        {
          x: new Date(1538787600000),
          y: [6638.24, 6640, 6620, 6624.47]
        },
        {
          x: new Date(1538787600000),
          y: [6624.53, 6636.03, 6621.68, 6624.31]
        },
        {
          x: new Date(1538789400000),
          y: [6624.61, 6632.2, 6617, 6626.02]
        },
        {
          x: new Date(1538791200000),
          y: [6627, 6627.62, 6584.22, 6603.02]
        },
        {
          x: new Date(1538793000000),
          y: [6605, 6608.03, 6598.95, 6604.01]
        },
        {
          x: new Date(1538794800000),
          y: [6604.5, 6614.4, 6602.26, 6608.02]
        },
        {
          x: new Date(1538796600000),
          y: [6608.02, 6610.68, 6601.99, 6608.91]
        },
        {
          x: new Date(1538798400000),
          y: [6608.91, 6618.99, 6608.01, 6612]
        },
        {
          x: new Date(1538800200000),
          y: [6612, 6615.13, 6605.09, 6612]
        },
        {
          x: new Date(1538802000000),
          y: [6612, 6624.12, 6608.43, 6622.95]
        },
        {
          x: new Date(1538803800000),
          y: [6623.91, 6623.91, 6615, 6615.67]
        },
        {
          x: new Date(1538805600000),
          y: [6618.69, 6618.74, 6610, 6610.4]
        },
        {
          x: new Date(1538807400000),
          y: [6611, 6622.78, 6610.4, 6614.9]
        },
        {
          x: new Date(1538809200000),
          y: [6614.9, 6626.2, 6613.33, 6623.45]
        },
        {
          x: new Date(1538811000000),
          y: [6623.48, 6627, 6618.38, 6620.35]
        },
        {
          x: new Date(1538812800000),
          y: [6619.43, 6620.35, 6610.05, 6615.53]
        },
        {
          x: new Date(1538814600000),
          y: [6615.53, 6617.93, 6610, 6615.19]
        },
        {
          x: new Date(1538816400000),
          y: [6615.19, 6621.6, 6608.2, 6620]
        },
        {
          x: new Date(1538818200000),
          y: [6619.54, 6625.17, 6614.15, 6620]
        },
        {
          x: new Date(1538820000000),
          y: [6620.33, 6634.15, 6617.24, 6624.61]
        },
        {
          x: new Date(1538821800000),
          y: [6625.95, 6626, 6611.66, 6617.58]
        },
        {
          x: new Date(1538823600000),
          y: [6619, 6625.97, 6595.27, 6598.86]
        },
        {
          x: new Date(1538825400000),
          y: [6598.86, 6598.88, 6570, 6587.16]
        },
        {
          x: new Date(1538827200000),
          y: [6588.86, 6600, 6580, 6593.4]
        },
        {
          x: new Date(1538829000000),
          y: [6593.99, 6598.89, 6585, 6587.81]
        },
        {
          x: new Date(1538830800000),
          y: [6587.81, 6592.73, 6567.14, 6578]
        },
        {
          x: new Date(1538832600000),
          y: [6578.35, 6581.72, 6567.39, 6579]
        },
        {
          x: new Date(1538834400000),
          y: [6579.38, 6580.92, 6566.77, 6575.96]
        },
        {
          x: new Date(1538836200000),
          y: [6575.96, 6589, 6571.77, 6588.92]
        },
        {
          x: new Date(1538838000000),
          y: [6588.92, 6594, 6577.55, 6589.22]
        },
        {
          x: new Date(1538839800000),
          y: [6589.3, 6598.89, 6589.1, 6596.08]
        },
        {
          x: new Date(1538841600000),
          y: [6597.5, 6600, 6588.39, 6596.25]
        },
        {
          x: new Date(1538843400000),
          y: [6598.03, 6600, 6588.73, 6595.97]
        },
        {
          x: new Date(1538845200000),
          y: [6595.97, 6602.01, 6588.17, 6602]
        },
        {
          x: new Date(1538847000000),
          y: [6602, 6607, 6596.51, 6599.95]
        },
        {
          x: new Date(1538848800000),
          y: [6600.63, 6601.21, 6590.39, 6591.02]
        }
      ]
    }
  ],
  chart: {
    type: "candlestick",
    height: 350
  },
  title: {
    text: "CandleStick Chart",
    align: "left"
  },
  xaxis: {
    type: "datetime"
  },
  yaxis: {
    tooltip: {
      enabled: true
    }
  }
};

this.countplotChart={
  series: [{
  name: 'Net Profit',
  data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
}, {
  name: 'Revenue',
  data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
}, {
  name: 'Free Cash Flow',
  data: [35, 41, 36, 26, 45, 48, 52, 53, 41]
}],
  chart: {
  type: 'bar',
  height: 350
},
plotOptions: {
  bar: {
    horizontal: false,
    columnWidth: '55%',
    endingShape: 'rounded'
  },
},
dataLabels: {
  enabled: false
},
stroke: {
  show: true,
  width: 2,
  colors: ['transparent']
},
xaxis: {
  categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
},
yaxis: {
  title: {
    text: '$ (thousands)'
  }
},
fill: {
  opacity: 1
},
tooltip: {
  y: {
    formatter: function (val) {
      return "$ " + val + " thousands"
    }
  }
}
};

this.heatmapchart=  {
  series: [
    {
      name: "Jan",
      data: this.generateData(20, {
        min: -30,
        max: 55
      })
    },
    {
      name: "Feb",
      data: this.generateData(20, {
        min: -30,
        max: 55
      })
    },
    {
      name: "Mar",
      data: this.generateData(20, {
        min: -30,
        max: 55
      })
    },
    {
      name: "Apr",
      data: this.generateData(20, {
        min: -30,
        max: 55
      })
    },
    {
      name: "May",
      data: this.generateData(20, {
        min: -30,
        max: 55
      })
    },
    {
      name: "Jun",
      data: this.generateData(20, {
        min: -30,
        max: 55
      })
    },
    {
      name: "Jul",
      data: this.generateData(20, {
        min: -30,
        max: 55
      })
    },
    {
      name: "Aug",
      data: this.generateData(20, {
        min: -30,
        max: 55
      })
    },
    {
      name: "Sep",
      data: this.generateData(20, {
        min: -30,
        max: 55
      })
    }
  ],
  chart: {
    height: 350,
    type: "heatmap"
  },
  plotOptions: {
    heatmap: {
      shadeIntensity: 0.5,
      colorScale: {
        ranges: [
          {
            from: -30,
            to: 5,
            name: "low",
            color: "#00A100"
          },
          {
            from: 6,
            to: 20,
            name: "medium",
            color: "#128FD9"
          },
          {
            from: 21,
            to: 45,
            name: "high",
            color: "#FFB200"
          },
          {
            from: 46,
            to: 55,
            name: "extreme",
            color: "#FF0000"
          }
        ]
      }
    }
  },
  dataLabels: {
    enabled: false
  },
  title: {
    text: "HeatMap Chart with Color Range"
  }
};

}


public generateData(count, yrange) {
  var i = 0;
  var series = [];
  while (i < count) {
    var x = "w" + (i + 1).toString();
    var y =
      Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

    series.push({
      x: x,
      y: y
    });
    i++;
  }
  return series;
}
//bubble chart need x-y-z three values


// this.scalterChart = {
//   series: [
//     {
//       name: "Bubble1",
//       data: this.generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
//         min: 10,
//         max: 60
//       })
//     },
//     {
//       name: "Bubble2",
//       data: this.generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
//         min: 10,
//         max: 60
//       })
//     },
//     {
//       name: "Bubble3",
//       data: this.generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
//         min: 10,
//         max: 60
//       })
//     },
//     {
//       name: "Bubble4",
//       data: this.generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
//         min: 10,
//         max: 60
//       })
//     }
//   ],
//   chart: {
//     height: 350,
//     type: "bubble"
//   },
//   dataLabels: {
//     enabled: false
//   },
//   fill: {
//     opacity: 0.8
//   },
//   title: {
//     text: "Simple Bubble Chart"
//   },
//   xaxis: {
//     tickAmount: 12,
//     type: "category"
//   },
//   yaxis: {
//     max: 70
//   }
// };

  public generateDayWiseTimeSeries(baseval, count, yrange) {
    var i = 0;
    var series = [];
    while (i < count) {
      var y =
        Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
    
      series.push([baseval, y]);
      baseval += 86400000;
      i++;
    }
    console.log(series);
    
    return series;
    }

    
  // public generateData(baseval, count, yrange) {
  //   var i = 0;
  //   var series = [];
  //   while (i < count) {
  //     var x = Math.floor(Math.random() * (750 - 1 + 1)) + 1;
  //     var y =
  //       Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
  //     var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15;
    
  //     series.push([x, y, z]);
  //     baseval += 86400000;
  //     i++;
  //   }
  //   console.log(series);
    
  //   return series;
  //   }


  successHandler(logs) {
    console.log(logs.response);
   
    this.loaderdiv=false;
  }

  

  errorHandler(error) {
    this.loaderdiv=false;
    if (error.error_msg)
      this.toaster.error(error.error_msg, 'Error');
    else {
      console.log(error);
      this.toaster.error('Something went wrong', 'Error');
    }
  }

  chart_type="histogram"
  chartchange(id){
    this.chart_type=id;
  }
  
}


