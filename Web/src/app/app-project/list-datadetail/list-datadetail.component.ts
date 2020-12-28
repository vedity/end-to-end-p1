import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-list-datadetail',
    templateUrl: './list-datadetail.component.html',
    styleUrls: ['./list-datadetail.component.scss']
})
export class ListDatadetailComponent implements OnInit {


    constructor() { }
    transactions: any;
    ngOnInit() {
        this.transactions = [
            {
                "index": {
                    "values": 0,
                    "display": "false"
                },
                "car_ID": {
                    "values": 1,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "alfa-romero giulia",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "convertible",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 88.6,
                    "display": "true"
                },
                "carlength": {
                    "values": 168.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.1,
                    "display": "true"
                },
                "carheight": {
                    "values": 48.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2548,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 130,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.47,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.68,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 111,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 21,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 27,
                    "display": "true"
                },
                "price": {
                    "values": 13495.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 1,
                    "display": "false"
                },
                "car_ID": {
                    "values": 2,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "alfa-romero stelvio",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "convertible",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 88.6,
                    "display": "true"
                },
                "carlength": {
                    "values": 168.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.1,
                    "display": "true"
                },
                "carheight": {
                    "values": 48.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2548,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 130,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.47,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.68,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 111,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 21,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 27,
                    "display": "true"
                },
                "price": {
                    "values": 16500.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 2,
                    "display": "false"
                },
                "car_ID": {
                    "values": 3,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "alfa-romero Quadrifoglio",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 171.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.4,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2823,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 152,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.68,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.47,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 154,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 26,
                    "display": "true"
                },
                "price": {
                    "values": 16500.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 3,
                    "display": "false"
                },
                "car_ID": {
                    "values": 4,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "audi 100 ls",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 99.8,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2337,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 109,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 10.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 102,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 13950.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 4,
                    "display": "false"
                },
                "car_ID": {
                    "values": 5,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "audi 100ls",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "4wd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 99.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2824,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "five",
                    "display": "true"
                },
                "enginesize": {
                    "values": 136,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 115,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 18,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 22,
                    "display": "true"
                },
                "price": {
                    "values": 17450.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 5,
                    "display": "false"
                },
                "car_ID": {
                    "values": 6,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "audi fox",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 99.8,
                    "display": "true"
                },
                "carlength": {
                    "values": 177.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2507,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "five",
                    "display": "true"
                },
                "enginesize": {
                    "values": 136,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 110,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 15250.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 6,
                    "display": "false"
                },
                "car_ID": {
                    "values": 7,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "audi 100ls",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 105.8,
                    "display": "true"
                },
                "carlength": {
                    "values": 192.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 71.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2844,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "five",
                    "display": "true"
                },
                "enginesize": {
                    "values": 136,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 110,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 17710.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 7,
                    "display": "false"
                },
                "car_ID": {
                    "values": 8,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "audi 5000",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 105.8,
                    "display": "true"
                },
                "carlength": {
                    "values": 192.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 71.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2954,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "five",
                    "display": "true"
                },
                "enginesize": {
                    "values": 136,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 110,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 18920.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 8,
                    "display": "false"
                },
                "car_ID": {
                    "values": 9,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "audi 4000",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 105.8,
                    "display": "true"
                },
                "carlength": {
                    "values": 192.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 71.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.9,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3086,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "five",
                    "display": "true"
                },
                "enginesize": {
                    "values": 131,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.13,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 140,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 20,
                    "display": "true"
                },
                "price": {
                    "values": 23875.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 9,
                    "display": "false"
                },
                "car_ID": {
                    "values": 10,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "audi 5000s (diesel)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "4wd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 99.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 178.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3053,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "five",
                    "display": "true"
                },
                "enginesize": {
                    "values": 131,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.13,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 160,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 16,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 22,
                    "display": "true"
                },
                "price": {
                    "values": 17859.167,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 10,
                    "display": "false"
                },
                "car_ID": {
                    "values": 11,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "bmw 320i",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 101.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2395,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.5,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.8,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.8,
                    "display": "true"
                },
                "horsepower": {
                    "values": 101,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5800,
                    "display": "true"
                },
                "citympg": {
                    "values": 23,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 29,
                    "display": "true"
                },
                "price": {
                    "values": 16430.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 11,
                    "display": "false"
                },
                "car_ID": {
                    "values": 12,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "bmw 320i",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 101.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2395,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.5,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.8,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.8,
                    "display": "true"
                },
                "horsepower": {
                    "values": 101,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5800,
                    "display": "true"
                },
                "citympg": {
                    "values": 23,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 29,
                    "display": "true"
                },
                "price": {
                    "values": 16925.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 12,
                    "display": "false"
                },
                "car_ID": {
                    "values": 13,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "bmw x1",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 101.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2710,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 164,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.31,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.19,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 121,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4250,
                    "display": "true"
                },
                "citympg": {
                    "values": 21,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 20970.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 13,
                    "display": "false"
                },
                "car_ID": {
                    "values": 14,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "bmw x3",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 101.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2765,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 164,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.31,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.19,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 121,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4250,
                    "display": "true"
                },
                "citympg": {
                    "values": 21,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 21105.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 14,
                    "display": "false"
                },
                "car_ID": {
                    "values": 15,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "bmw z4",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 103.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 189.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3055,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 164,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.31,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.19,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 121,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4250,
                    "display": "true"
                },
                "citympg": {
                    "values": 20,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 24565.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 15,
                    "display": "false"
                },
                "car_ID": {
                    "values": 16,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "bmw x4",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 103.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 189.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3230,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 209,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 182,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 16,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 22,
                    "display": "true"
                },
                "price": {
                    "values": 30760.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 16,
                    "display": "false"
                },
                "car_ID": {
                    "values": 17,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "bmw x5",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 103.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 193.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3380,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 209,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 182,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 16,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 22,
                    "display": "true"
                },
                "price": {
                    "values": 41315.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 17,
                    "display": "false"
                },
                "car_ID": {
                    "values": 18,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "bmw x3",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 110.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 197.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 70.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3505,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 209,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 182,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 15,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 20,
                    "display": "true"
                },
                "price": {
                    "values": 36880.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 18,
                    "display": "false"
                },
                "car_ID": {
                    "values": 19,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "chevrolet impala",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 88.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 141.1,
                    "display": "true"
                },
                "carwidth": {
                    "values": 60.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.2,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1488,
                    "display": "true"
                },
                "enginetype": {
                    "values": "l",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "three",
                    "display": "true"
                },
                "enginesize": {
                    "values": 61,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.91,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 48,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5100,
                    "display": "true"
                },
                "citympg": {
                    "values": 47,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 53,
                    "display": "true"
                },
                "price": {
                    "values": 5151.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 19,
                    "display": "false"
                },
                "car_ID": {
                    "values": 20,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "chevrolet monte carlo",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 155.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1874,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 90,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.03,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.11,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 70,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 38,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 43,
                    "display": "true"
                },
                "price": {
                    "values": 6295.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 20,
                    "display": "false"
                },
                "car_ID": {
                    "values": 21,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "chevrolet vega 2300",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 158.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1909,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 90,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.03,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.11,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 70,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 38,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 43,
                    "display": "true"
                },
                "price": {
                    "values": 6575.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 21,
                    "display": "false"
                },
                "car_ID": {
                    "values": 22,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "dodge rampage",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1876,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 90,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.97,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.41,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 37,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 41,
                    "display": "true"
                },
                "price": {
                    "values": 5572.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 22,
                    "display": "false"
                },
                "car_ID": {
                    "values": 23,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "dodge challenger se",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1876,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 90,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.97,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6377.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 23,
                    "display": "false"
                },
                "car_ID": {
                    "values": 24,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "dodge d200",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2128,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.03,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 102,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 7957.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 24,
                    "display": "false"
                },
                "car_ID": {
                    "values": 25,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "dodge monaco (sw)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1967,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 90,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.97,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6229.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 25,
                    "display": "false"
                },
                "car_ID": {
                    "values": 26,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "dodge colt hardtop",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1989,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 90,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.97,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6692.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 26,
                    "display": "false"
                },
                "car_ID": {
                    "values": 27,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "dodge colt (sw)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1989,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 90,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.97,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 7609.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 27,
                    "display": "false"
                },
                "car_ID": {
                    "values": 28,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "dodge coronet custom",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2191,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.03,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 102,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 8558.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 28,
                    "display": "false"
                },
                "car_ID": {
                    "values": 29,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "dodge dart custom",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 103.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 174.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 59.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2535,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.34,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.46,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 88,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 8921.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 29,
                    "display": "false"
                },
                "car_ID": {
                    "values": 30,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "dodge coronet custom (sw)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.2,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2811,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 156,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.6,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.9,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 145,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 12964.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 30,
                    "display": "false"
                },
                "car_ID": {
                    "values": 31,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda civic",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 86.6,
                    "display": "true"
                },
                "carlength": {
                    "values": 144.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1713,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "1bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.91,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.41,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 58,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 49,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 54,
                    "display": "true"
                },
                "price": {
                    "values": 6479.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 31,
                    "display": "false"
                },
                "car_ID": {
                    "values": 32,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda civic cvcc",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 86.6,
                    "display": "true"
                },
                "carlength": {
                    "values": 144.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1819,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "1bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.91,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.41,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.2,
                    "display": "true"
                },
                "horsepower": {
                    "values": 76,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 6000,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6855.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 32,
                    "display": "false"
                },
                "car_ID": {
                    "values": 33,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda civic",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 150.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1837,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 79,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "1bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.91,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.07,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 10.1,
                    "display": "true"
                },
                "horsepower": {
                    "values": 60,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 38,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 42,
                    "display": "true"
                },
                "price": {
                    "values": 5399.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 33,
                    "display": "false"
                },
                "car_ID": {
                    "values": 34,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda accord cvcc",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 150.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1940,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "1bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.91,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.41,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.2,
                    "display": "true"
                },
                "horsepower": {
                    "values": 76,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 6000,
                    "display": "true"
                },
                "citympg": {
                    "values": 30,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 6529.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 34,
                    "display": "false"
                },
                "car_ID": {
                    "values": 35,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda civic cvcc",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 150.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1956,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "1bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.91,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.41,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.2,
                    "display": "true"
                },
                "horsepower": {
                    "values": 76,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 6000,
                    "display": "true"
                },
                "citympg": {
                    "values": 30,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 7129.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 35,
                    "display": "false"
                },
                "car_ID": {
                    "values": 36,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda accord lx",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 163.4,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2010,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "1bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.91,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.41,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.2,
                    "display": "true"
                },
                "horsepower": {
                    "values": 76,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 6000,
                    "display": "true"
                },
                "citympg": {
                    "values": 30,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 7295.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 36,
                    "display": "false"
                },
                "car_ID": {
                    "values": 37,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda civic 1500 gl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.1,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 58.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2024,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "1bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.92,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.41,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.2,
                    "display": "true"
                },
                "horsepower": {
                    "values": 76,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 6000,
                    "display": "true"
                },
                "citympg": {
                    "values": 30,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 7295.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 37,
                    "display": "false"
                },
                "car_ID": {
                    "values": 38,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda accord",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 167.5,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2236,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 110,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "1bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.58,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 86,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5800,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 33,
                    "display": "true"
                },
                "price": {
                    "values": 7895.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 38,
                    "display": "false"
                },
                "car_ID": {
                    "values": 39,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda civic 1300",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 167.5,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2289,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 110,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "1bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.58,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 86,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5800,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 33,
                    "display": "true"
                },
                "price": {
                    "values": 9095.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 39,
                    "display": "false"
                },
                "car_ID": {
                    "values": 40,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda prelude",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 175.4,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2304,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 110,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "1bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.58,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 86,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5800,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 33,
                    "display": "true"
                },
                "price": {
                    "values": 8845.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 40,
                    "display": "false"
                },
                "car_ID": {
                    "values": 41,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda accord",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 175.4,
                    "display": "true"
                },
                "carwidth": {
                    "values": 62.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2372,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 110,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "1bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.58,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 86,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5800,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 33,
                    "display": "true"
                },
                "price": {
                    "values": 10295.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 41,
                    "display": "false"
                },
                "car_ID": {
                    "values": 42,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda civic",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 175.4,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2465,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 110,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.58,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 101,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5800,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 12945.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 42,
                    "display": "false"
                },
                "car_ID": {
                    "values": 43,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "honda civic (auto)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 169.1,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 51.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2293,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 110,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.58,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.1,
                    "display": "true"
                },
                "horsepower": {
                    "values": 100,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 25,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 31,
                    "display": "true"
                },
                "price": {
                    "values": 10345.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 43,
                    "display": "false"
                },
                "car_ID": {
                    "values": 44,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "isuzu MU-X",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 170.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 61.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2337,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 111,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.31,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 78,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 29,
                    "display": "true"
                },
                "price": {
                    "values": 6785.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 44,
                    "display": "false"
                },
                "car_ID": {
                    "values": 45,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "isuzu D-Max ",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 155.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1874,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 90,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.03,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.11,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 70,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 38,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 43,
                    "display": "true"
                },
                "price": {
                    "values": 8916.5,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 45,
                    "display": "false"
                },
                "car_ID": {
                    "values": 46,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "isuzu D-Max V-Cross",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 155.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1909,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 90,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.03,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.11,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 70,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 38,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 43,
                    "display": "true"
                },
                "price": {
                    "values": 8916.5,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 46,
                    "display": "false"
                },
                "car_ID": {
                    "values": 47,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "isuzu D-Max ",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 172.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 51.4,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2734,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 119,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "spfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.43,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.2,
                    "display": "true"
                },
                "horsepower": {
                    "values": 90,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 29,
                    "display": "true"
                },
                "price": {
                    "values": 11048.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 47,
                    "display": "false"
                },
                "car_ID": {
                    "values": 48,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "jaguar xj",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 113.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 199.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 69.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 4066,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 258,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.63,
                    "display": "true"
                },
                "stroke": {
                    "values": 4.17,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.1,
                    "display": "true"
                },
                "horsepower": {
                    "values": 176,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4750,
                    "display": "true"
                },
                "citympg": {
                    "values": 15,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 19,
                    "display": "true"
                },
                "price": {
                    "values": 32250.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 48,
                    "display": "false"
                },
                "car_ID": {
                    "values": 49,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "jaguar xf",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 113.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 199.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 69.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 4066,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 258,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.63,
                    "display": "true"
                },
                "stroke": {
                    "values": 4.17,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.1,
                    "display": "true"
                },
                "horsepower": {
                    "values": 176,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4750,
                    "display": "true"
                },
                "citympg": {
                    "values": 15,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 19,
                    "display": "true"
                },
                "price": {
                    "values": 35550.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 49,
                    "display": "false"
                },
                "car_ID": {
                    "values": 50,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "jaguar xk",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 102.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 191.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 70.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 47.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3950,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "twelve",
                    "display": "true"
                },
                "enginesize": {
                    "values": 326,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.54,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.76,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 11.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 262,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 13,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 17,
                    "display": "true"
                },
                "price": {
                    "values": 36000.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 50,
                    "display": "false"
                },
                "car_ID": {
                    "values": 51,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "maxda rx3",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 159.1,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1890,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 91,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.03,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 30,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 31,
                    "display": "true"
                },
                "price": {
                    "values": 5195.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 51,
                    "display": "false"
                },
                "car_ID": {
                    "values": 52,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "maxda glc deluxe",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 159.1,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1900,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 91,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.03,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6095.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 52,
                    "display": "false"
                },
                "car_ID": {
                    "values": 53,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda rx2 coupe",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 159.1,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1905,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 91,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.03,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6795.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 53,
                    "display": "false"
                },
                "car_ID": {
                    "values": 54,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda rx-4",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 166.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1945,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 91,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.03,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6695.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 54,
                    "display": "false"
                },
                "car_ID": {
                    "values": 55,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda glc deluxe",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 166.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1950,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 91,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.08,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 7395.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 55,
                    "display": "false"
                },
                "car_ID": {
                    "values": 56,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda 626",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 169.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.7,
                    "display": "true"
                },
                "carheight": {
                    "values": 49.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2380,
                    "display": "true"
                },
                "enginetype": {
                    "values": "rotor",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "two",
                    "display": "true"
                },
                "enginesize": {
                    "values": 70,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "4bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.33,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.255,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 101,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 6000,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 23,
                    "display": "true"
                },
                "price": {
                    "values": 10945.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 56,
                    "display": "false"
                },
                "car_ID": {
                    "values": 57,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda glc",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 169.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.7,
                    "display": "true"
                },
                "carheight": {
                    "values": 49.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2380,
                    "display": "true"
                },
                "enginetype": {
                    "values": "rotor",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "two",
                    "display": "true"
                },
                "enginesize": {
                    "values": 70,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "4bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.33,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.255,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 101,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 6000,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 23,
                    "display": "true"
                },
                "price": {
                    "values": 11845.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 57,
                    "display": "false"
                },
                "car_ID": {
                    "values": 58,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda rx-7 gs",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 169.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.7,
                    "display": "true"
                },
                "carheight": {
                    "values": 49.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2385,
                    "display": "true"
                },
                "enginetype": {
                    "values": "rotor",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "two",
                    "display": "true"
                },
                "enginesize": {
                    "values": 70,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "4bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.33,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.255,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 101,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 6000,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 23,
                    "display": "true"
                },
                "price": {
                    "values": 13645.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 58,
                    "display": "false"
                },
                "car_ID": {
                    "values": 59,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda glc 4",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 169.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.7,
                    "display": "true"
                },
                "carheight": {
                    "values": 49.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2500,
                    "display": "true"
                },
                "enginetype": {
                    "values": "rotor",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "two",
                    "display": "true"
                },
                "enginesize": {
                    "values": 80,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.33,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.255,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 135,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 6000,
                    "display": "true"
                },
                "citympg": {
                    "values": 16,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 23,
                    "display": "true"
                },
                "price": {
                    "values": 15645.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 59,
                    "display": "false"
                },
                "car_ID": {
                    "values": 60,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda 626",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.8,
                    "display": "true"
                },
                "carlength": {
                    "values": 177.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2385,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.39,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 84,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 26,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 8845.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 60,
                    "display": "false"
                },
                "car_ID": {
                    "values": 61,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda glc custom l",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.8,
                    "display": "true"
                },
                "carlength": {
                    "values": 177.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2410,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.39,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 84,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 26,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 8495.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 61,
                    "display": "false"
                },
                "car_ID": {
                    "values": 62,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda glc custom",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.8,
                    "display": "true"
                },
                "carlength": {
                    "values": 177.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2385,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.39,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 84,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 26,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 10595.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 62,
                    "display": "false"
                },
                "car_ID": {
                    "values": 63,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda rx-4",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.8,
                    "display": "true"
                },
                "carlength": {
                    "values": 177.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2410,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.39,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 84,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 26,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 10245.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 63,
                    "display": "false"
                },
                "car_ID": {
                    "values": 64,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda glc deluxe",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.8,
                    "display": "true"
                },
                "carlength": {
                    "values": 177.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2443,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.39,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 22.7,
                    "display": "true"
                },
                "horsepower": {
                    "values": 64,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4650,
                    "display": "true"
                },
                "citympg": {
                    "values": 36,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 42,
                    "display": "true"
                },
                "price": {
                    "values": 10795.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 64,
                    "display": "false"
                },
                "car_ID": {
                    "values": 65,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda 626",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.8,
                    "display": "true"
                },
                "carlength": {
                    "values": 177.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2425,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.39,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 84,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 26,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 11245.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 65,
                    "display": "false"
                },
                "car_ID": {
                    "values": 66,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda glc",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 104.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 175.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.1,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.4,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2670,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 140,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.76,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.16,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 120,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 27,
                    "display": "true"
                },
                "price": {
                    "values": 18280.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 66,
                    "display": "false"
                },
                "car_ID": {
                    "values": 67,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "mazda rx-7 gs",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 104.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 175.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.1,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.4,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2700,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 134,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.43,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 22.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 72,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4200,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 39,
                    "display": "true"
                },
                "price": {
                    "values": 18344.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 67,
                    "display": "false"
                },
                "car_ID": {
                    "values": 68,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "buick electra 225 custom",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 110.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 190.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 70.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3515,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "five",
                    "display": "true"
                },
                "enginesize": {
                    "values": 183,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.58,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 21.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 123,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4350,
                    "display": "true"
                },
                "citympg": {
                    "values": 22,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 25552.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 68,
                    "display": "false"
                },
                "car_ID": {
                    "values": 69,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "buick century luxus (sw)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 110.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 190.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 70.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 58.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3750,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "five",
                    "display": "true"
                },
                "enginesize": {
                    "values": 183,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.58,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 21.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 123,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4350,
                    "display": "true"
                },
                "citympg": {
                    "values": 22,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 28248.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 69,
                    "display": "false"
                },
                "car_ID": {
                    "values": 70,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "buick century",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hardtop",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 106.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 187.5,
                    "display": "true"
                },
                "carwidth": {
                    "values": 70.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.9,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3495,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "five",
                    "display": "true"
                },
                "enginesize": {
                    "values": 183,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.58,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 21.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 123,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4350,
                    "display": "true"
                },
                "citympg": {
                    "values": 22,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 28176.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 70,
                    "display": "false"
                },
                "car_ID": {
                    "values": 71,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "buick skyhawk",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 115.6,
                    "display": "true"
                },
                "carlength": {
                    "values": 202.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 71.7,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3770,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "five",
                    "display": "true"
                },
                "enginesize": {
                    "values": 183,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.58,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 21.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 123,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4350,
                    "display": "true"
                },
                "citympg": {
                    "values": 22,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 31600.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 71,
                    "display": "false"
                },
                "car_ID": {
                    "values": 72,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "buick opel isuzu deluxe",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 115.6,
                    "display": "true"
                },
                "carlength": {
                    "values": 202.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 71.7,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3740,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "eight",
                    "display": "true"
                },
                "enginesize": {
                    "values": 234,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.46,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.1,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 155,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4750,
                    "display": "true"
                },
                "citympg": {
                    "values": 16,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 18,
                    "display": "true"
                },
                "price": {
                    "values": 34184.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 72,
                    "display": "false"
                },
                "car_ID": {
                    "values": 73,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "buick skylark",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "convertible",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.6,
                    "display": "true"
                },
                "carlength": {
                    "values": 180.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 70.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3685,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "eight",
                    "display": "true"
                },
                "enginesize": {
                    "values": 234,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.46,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.1,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 155,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4750,
                    "display": "true"
                },
                "citympg": {
                    "values": 16,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 18,
                    "display": "true"
                },
                "price": {
                    "values": 35056.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 73,
                    "display": "false"
                },
                "car_ID": {
                    "values": 74,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "buick century special",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 120.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 208.1,
                    "display": "true"
                },
                "carwidth": {
                    "values": 71.7,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3900,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "eight",
                    "display": "true"
                },
                "enginesize": {
                    "values": 308,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.8,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.35,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 184,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4500,
                    "display": "true"
                },
                "citympg": {
                    "values": 14,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 16,
                    "display": "true"
                },
                "price": {
                    "values": 40960.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 74,
                    "display": "false"
                },
                "car_ID": {
                    "values": 75,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "buick regal sport coupe (turbo)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hardtop",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 112.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 199.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 72.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.4,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3715,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "eight",
                    "display": "true"
                },
                "enginesize": {
                    "values": 304,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.8,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.35,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 184,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4500,
                    "display": "true"
                },
                "citympg": {
                    "values": 14,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 16,
                    "display": "true"
                },
                "price": {
                    "values": 45400.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 75,
                    "display": "false"
                },
                "car_ID": {
                    "values": 76,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "mercury cougar",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 102.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 178.4,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2910,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 140,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.78,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.12,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 175,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 16503.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 76,
                    "display": "false"
                },
                "car_ID": {
                    "values": 77,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi mirage",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1918,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.97,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 37,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 41,
                    "display": "true"
                },
                "price": {
                    "values": 5389.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 77,
                    "display": "false"
                },
                "car_ID": {
                    "values": 78,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi lancer",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1944,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.97,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6189.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 78,
                    "display": "false"
                },
                "car_ID": {
                    "values": 79,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi outlander",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2004,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.97,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6669.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 79,
                    "display": "false"
                },
                "car_ID": {
                    "values": 80,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi g4",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2145,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "spdi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.03,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 102,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 7689.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 80,
                    "display": "false"
                },
                "car_ID": {
                    "values": 81,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi mirage g4",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 49.4,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2370,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 110,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "spdi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.17,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.46,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 116,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 23,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 9959.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 81,
                    "display": "false"
                },
                "car_ID": {
                    "values": 82,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi g4",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 49.4,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2328,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.35,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.46,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 88,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 25,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 8499.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 82,
                    "display": "false"
                },
                "car_ID": {
                    "values": 83,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi outlander",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.2,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2833,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 156,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "spdi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.58,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.86,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 145,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 12629.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 83,
                    "display": "false"
                },
                "car_ID": {
                    "values": 84,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi g4",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.2,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2921,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 156,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "spdi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.59,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.86,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 145,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 14869.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 84,
                    "display": "false"
                },
                "car_ID": {
                    "values": 85,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi mirage g4",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.2,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2926,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 156,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "spdi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.59,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.86,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 145,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 14489.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 85,
                    "display": "false"
                },
                "car_ID": {
                    "values": 86,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi montero",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 172.4,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 51.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2365,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.35,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.46,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 88,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 25,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 6989.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 86,
                    "display": "false"
                },
                "car_ID": {
                    "values": 87,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi pajero",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 172.4,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 51.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2405,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.35,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.46,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 88,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 25,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 8189.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 87,
                    "display": "false"
                },
                "car_ID": {
                    "values": 88,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi outlander",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 172.4,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 51.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2403,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 110,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "spdi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.17,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.46,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 116,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 23,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 9279.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 88,
                    "display": "false"
                },
                "car_ID": {
                    "values": 89,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "mitsubishi mirage g4",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 172.4,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 51.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2403,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 110,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "spdi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.17,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.46,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 116,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 23,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 9279.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 89,
                    "display": "false"
                },
                "car_ID": {
                    "values": 90,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "Nissan versa",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 165.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1889,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.29,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 69,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 5499.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 90,
                    "display": "false"
                },
                "car_ID": {
                    "values": 91,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan gt-r",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 165.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2017,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 103,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.99,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.47,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 21.9,
                    "display": "true"
                },
                "horsepower": {
                    "values": 55,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 45,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 50,
                    "display": "true"
                },
                "price": {
                    "values": 7099.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 91,
                    "display": "false"
                },
                "car_ID": {
                    "values": 92,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan rogue",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 165.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1918,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.29,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 69,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 6649.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 92,
                    "display": "false"
                },
                "car_ID": {
                    "values": 93,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan latio",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 165.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1938,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.29,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 69,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 6849.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 93,
                    "display": "false"
                },
                "car_ID": {
                    "values": 94,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan titan",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 170.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2024,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.29,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 69,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 7349.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 94,
                    "display": "false"
                },
                "car_ID": {
                    "values": 95,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan leaf",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 165.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1951,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.29,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 69,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 7299.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 95,
                    "display": "false"
                },
                "car_ID": {
                    "values": 96,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan juke",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 165.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2028,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.29,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 69,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 7799.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 96,
                    "display": "false"
                },
                "car_ID": {
                    "values": 97,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan latio",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 165.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1971,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.29,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 69,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 7499.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 97,
                    "display": "false"
                },
                "car_ID": {
                    "values": 98,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan note",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 170.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2037,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.29,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 69,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 7999.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 98,
                    "display": "false"
                },
                "car_ID": {
                    "values": 99,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan clipper",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hardtop",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 162.4,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2008,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.15,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.29,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 69,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 8249.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 99,
                    "display": "false"
                },
                "car_ID": {
                    "values": 100,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan rogue",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.4,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2324,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 120,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.33,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.47,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 97,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 8949.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 100,
                    "display": "false"
                },
                "car_ID": {
                    "values": 101,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan nv200",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.4,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2302,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 120,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.33,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.47,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 97,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 9549.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 101,
                    "display": "false"
                },
                "car_ID": {
                    "values": 102,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan dayz",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 100.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 181.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3095,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 181,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.43,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.27,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 152,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 22,
                    "display": "true"
                },
                "price": {
                    "values": 13499.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 102,
                    "display": "false"
                },
                "car_ID": {
                    "values": 103,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan fuga",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 100.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 184.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3296,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 181,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.43,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.27,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 152,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 22,
                    "display": "true"
                },
                "price": {
                    "values": 14399.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 103,
                    "display": "false"
                },
                "car_ID": {
                    "values": 104,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan otti",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 100.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 184.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3060,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 181,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.43,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.27,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 152,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 13499.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 104,
                    "display": "false"
                },
                "car_ID": {
                    "values": 105,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan teana",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 91.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 170.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 49.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3071,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 181,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.43,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.27,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 160,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 17199.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 105,
                    "display": "false"
                },
                "car_ID": {
                    "values": 106,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan kicks",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 91.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 170.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 49.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3139,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 181,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.43,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.27,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.8,
                    "display": "true"
                },
                "horsepower": {
                    "values": 200,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 23,
                    "display": "true"
                },
                "price": {
                    "values": 19699.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 106,
                    "display": "false"
                },
                "car_ID": {
                    "values": 107,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "nissan clipper",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 99.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 178.5,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 49.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3139,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 181,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.43,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.27,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 160,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 18399.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 107,
                    "display": "false"
                },
                "car_ID": {
                    "values": 108,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "peugeot 504",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 107.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3020,
                    "display": "true"
                },
                "enginetype": {
                    "values": "l",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 120,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.46,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.19,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 97,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 11900.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 108,
                    "display": "false"
                },
                "car_ID": {
                    "values": 109,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "peugeot 304",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 107.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3197,
                    "display": "true"
                },
                "enginetype": {
                    "values": "l",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 152,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.7,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.52,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 21.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 95,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4150,
                    "display": "true"
                },
                "citympg": {
                    "values": 28,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 33,
                    "display": "true"
                },
                "price": {
                    "values": 13200.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 109,
                    "display": "false"
                },
                "car_ID": {
                    "values": 110,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "peugeot 504 (sw)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 114.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 198.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 58.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3230,
                    "display": "true"
                },
                "enginetype": {
                    "values": "l",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 120,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.46,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.19,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 97,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 12440.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 110,
                    "display": "false"
                },
                "car_ID": {
                    "values": 111,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "peugeot 504",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 114.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 198.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 58.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3430,
                    "display": "true"
                },
                "enginetype": {
                    "values": "l",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 152,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.7,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.52,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 21.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 95,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4150,
                    "display": "true"
                },
                "citympg": {
                    "values": 25,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 13860.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 111,
                    "display": "false"
                },
                "car_ID": {
                    "values": 112,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "peugeot 504",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 107.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3075,
                    "display": "true"
                },
                "enginetype": {
                    "values": "l",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 120,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.46,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.19,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 95,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 15580.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 112,
                    "display": "false"
                },
                "car_ID": {
                    "values": 113,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "peugeot 604sl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 107.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3252,
                    "display": "true"
                },
                "enginetype": {
                    "values": "l",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 152,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.7,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.52,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 21.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 95,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4150,
                    "display": "true"
                },
                "citympg": {
                    "values": 28,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 33,
                    "display": "true"
                },
                "price": {
                    "values": 16900.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 113,
                    "display": "false"
                },
                "car_ID": {
                    "values": 114,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "peugeot 504",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 114.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 198.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3285,
                    "display": "true"
                },
                "enginetype": {
                    "values": "l",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 120,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.46,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.19,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 95,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 16695.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 114,
                    "display": "false"
                },
                "car_ID": {
                    "values": 115,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "peugeot 505s turbo diesel",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 114.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 198.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 58.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3485,
                    "display": "true"
                },
                "enginetype": {
                    "values": "l",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 152,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.7,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.52,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 21.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 95,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4150,
                    "display": "true"
                },
                "citympg": {
                    "values": 25,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 17075.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 115,
                    "display": "false"
                },
                "car_ID": {
                    "values": 116,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "peugeot 504",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 107.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3075,
                    "display": "true"
                },
                "enginetype": {
                    "values": "l",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 120,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.46,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.19,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 97,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 16630.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 116,
                    "display": "false"
                },
                "car_ID": {
                    "values": 117,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "peugeot 504",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 107.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3252,
                    "display": "true"
                },
                "enginetype": {
                    "values": "l",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 152,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.7,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.52,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 21.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 95,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4150,
                    "display": "true"
                },
                "citympg": {
                    "values": 28,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 33,
                    "display": "true"
                },
                "price": {
                    "values": 17950.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 117,
                    "display": "false"
                },
                "car_ID": {
                    "values": 118,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "peugeot 604sl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 108.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3130,
                    "display": "true"
                },
                "enginetype": {
                    "values": "l",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 134,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.61,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.21,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 142,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5600,
                    "display": "true"
                },
                "citympg": {
                    "values": 18,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 18150.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 118,
                    "display": "false"
                },
                "car_ID": {
                    "values": 119,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "plymouth fury iii",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1918,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 90,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.97,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 37,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 41,
                    "display": "true"
                },
                "price": {
                    "values": 5572.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 119,
                    "display": "false"
                },
                "car_ID": {
                    "values": 120,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "plymouth cricket",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2128,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "spdi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.03,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.39,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.6,
                    "display": "true"
                },
                "horsepower": {
                    "values": 102,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 7957.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 120,
                    "display": "false"
                },
                "car_ID": {
                    "values": 121,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "plymouth fury iii",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1967,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 90,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.97,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6229.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 121,
                    "display": "false"
                },
                "car_ID": {
                    "values": 122,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "plymouth satellite custom (sw)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 167.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1989,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 90,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.97,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6692.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 122,
                    "display": "false"
                },
                "car_ID": {
                    "values": 123,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "plymouth fury gran sedan",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 167.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2191,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.97,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.23,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 7609.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 123,
                    "display": "false"
                },
                "car_ID": {
                    "values": 124,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "plymouth valiant",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 103.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 174.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 59.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2535,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.35,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.46,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 88,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 8921.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 124,
                    "display": "false"
                },
                "car_ID": {
                    "values": 125,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "plymouth duster",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.2,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2818,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 156,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "spdi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.59,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.86,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 145,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5000,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 12764.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 125,
                    "display": "false"
                },
                "car_ID": {
                    "values": 126,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "porsche macan",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 168.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.2,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2778,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 151,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.94,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.11,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 143,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 27,
                    "display": "true"
                },
                "price": {
                    "values": 22018.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 126,
                    "display": "false"
                },
                "car_ID": {
                    "values": 127,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "porcshce panamera",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hardtop",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "rear",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 89.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 168.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 51.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2756,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 194,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.74,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.9,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 207,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5900,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 32528.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 127,
                    "display": "false"
                },
                "car_ID": {
                    "values": 128,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "porsche cayenne",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hardtop",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "rear",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 89.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 168.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 51.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2756,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 194,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.74,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.9,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 207,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5900,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 34028.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 128,
                    "display": "false"
                },
                "car_ID": {
                    "values": 129,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "porsche boxter",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "convertible",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "rear",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 89.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 168.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 51.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2800,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 194,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.74,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.9,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 207,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5900,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 37028.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 129,
                    "display": "false"
                },
                "car_ID": {
                    "values": 130,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "porsche cayenne",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 175.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 72.3,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3366,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "eight",
                    "display": "true"
                },
                "enginesize": {
                    "values": 203,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.94,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.11,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 10.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 288,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5750,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 31400.5,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 130,
                    "display": "false"
                },
                "car_ID": {
                    "values": 131,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "renault 12tl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 181.5,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.2,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2579,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 132,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.46,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.9,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.7,
                    "display": "true"
                },
                "horsepower": {
                    "values": 90,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5100,
                    "display": "true"
                },
                "citympg": {
                    "values": 23,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 31,
                    "display": "true"
                },
                "price": {
                    "values": 9295.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 131,
                    "display": "false"
                },
                "car_ID": {
                    "values": 132,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "renault 5 gtl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 50.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2460,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 132,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.46,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.9,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.7,
                    "display": "true"
                },
                "horsepower": {
                    "values": 90,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5100,
                    "display": "true"
                },
                "citympg": {
                    "values": 23,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 31,
                    "display": "true"
                },
                "price": {
                    "values": 9895.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 132,
                    "display": "false"
                },
                "car_ID": {
                    "values": 133,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "saab 99e",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 99.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2658,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 121,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.54,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.07,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.31,
                    "display": "true"
                },
                "horsepower": {
                    "values": 110,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5250,
                    "display": "true"
                },
                "citympg": {
                    "values": 21,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 11850.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 133,
                    "display": "false"
                },
                "car_ID": {
                    "values": 134,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "saab 99le",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 99.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2695,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 121,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.54,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.07,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 110,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5250,
                    "display": "true"
                },
                "citympg": {
                    "values": 21,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 12170.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 134,
                    "display": "false"
                },
                "car_ID": {
                    "values": 135,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "saab 99le",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 99.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2707,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 121,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 2.54,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.07,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 110,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5250,
                    "display": "true"
                },
                "citympg": {
                    "values": 21,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 15040.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 135,
                    "display": "false"
                },
                "car_ID": {
                    "values": 136,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "saab 99gle",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 99.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2758,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 121,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.54,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.07,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 110,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5250,
                    "display": "true"
                },
                "citympg": {
                    "values": 21,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 15510.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 136,
                    "display": "false"
                },
                "car_ID": {
                    "values": 137,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "saab 99gle",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 99.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2808,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 121,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.54,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.07,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 160,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 26,
                    "display": "true"
                },
                "price": {
                    "values": 18150.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 137,
                    "display": "false"
                },
                "car_ID": {
                    "values": 138,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "saab 99e",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 99.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 186.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2847,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 121,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.54,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.07,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 160,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 26,
                    "display": "true"
                },
                "price": {
                    "values": 18620.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 138,
                    "display": "false"
                },
                "car_ID": {
                    "values": 139,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "subaru",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 156.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2050,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.36,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 69,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4900,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 36,
                    "display": "true"
                },
                "price": {
                    "values": 5118.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 139,
                    "display": "false"
                },
                "car_ID": {
                    "values": 140,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "subaru dl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.9,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2120,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.7,
                    "display": "true"
                },
                "horsepower": {
                    "values": 73,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4400,
                    "display": "true"
                },
                "citympg": {
                    "values": 26,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 31,
                    "display": "true"
                },
                "price": {
                    "values": 7053.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 140,
                    "display": "false"
                },
                "car_ID": {
                    "values": 141,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "subaru dl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "4wd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 93.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 157.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2240,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.7,
                    "display": "true"
                },
                "horsepower": {
                    "values": 73,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4400,
                    "display": "true"
                },
                "citympg": {
                    "values": 26,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 31,
                    "display": "true"
                },
                "price": {
                    "values": 7603.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 141,
                    "display": "false"
                },
                "car_ID": {
                    "values": 142,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "subaru",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 172.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2145,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 82,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 32,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 7126.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 142,
                    "display": "false"
                },
                "car_ID": {
                    "values": 143,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "subaru brz",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 172.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2190,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 82,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4400,
                    "display": "true"
                },
                "citympg": {
                    "values": 28,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 33,
                    "display": "true"
                },
                "price": {
                    "values": 7775.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 143,
                    "display": "false"
                },
                "car_ID": {
                    "values": 144,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "subaru baja",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.2,
                    "display": "true"
                },
                "carlength": {
                    "values": 172.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2340,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 94,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 26,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 9960.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 144,
                    "display": "false"
                },
                "car_ID": {
                    "values": 145,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "subaru r1",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "4wd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 172.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2385,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 82,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 9233.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 145,
                    "display": "false"
                },
                "car_ID": {
                    "values": 146,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "subaru r2",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "4wd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 172.0,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.3,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2510,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.7,
                    "display": "true"
                },
                "horsepower": {
                    "values": 111,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 29,
                    "display": "true"
                },
                "price": {
                    "values": 11259.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 146,
                    "display": "false"
                },
                "car_ID": {
                    "values": 147,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "subaru trezia",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.5,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2290,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 82,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 28,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 7463.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 147,
                    "display": "false"
                },
                "car_ID": {
                    "values": 148,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "subaru tribeca",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.0,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.5,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2455,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 94,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 25,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 31,
                    "display": "true"
                },
                "price": {
                    "values": 10198.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 148,
                    "display": "false"
                },
                "car_ID": {
                    "values": 149,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "subaru dl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "4wd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.9,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2420,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 82,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 23,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 29,
                    "display": "true"
                },
                "price": {
                    "values": 8013.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 149,
                    "display": "false"
                },
                "car_ID": {
                    "values": 150,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "subaru dl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "4wd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 96.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 173.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.9,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2650,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcf",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 108,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.64,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.7,
                    "display": "true"
                },
                "horsepower": {
                    "values": 111,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 23,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 23,
                    "display": "true"
                },
                "price": {
                    "values": 11694.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 150,
                    "display": "false"
                },
                "car_ID": {
                    "values": 151,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corona mark ii",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 158.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 1985,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.05,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 62,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 35,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 39,
                    "display": "true"
                },
                "price": {
                    "values": 5348.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 151,
                    "display": "false"
                },
                "car_ID": {
                    "values": 152,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corona",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 158.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2040,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.05,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 62,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6338.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 152,
                    "display": "false"
                },
                "car_ID": {
                    "values": 153,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corolla 1200",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 158.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2015,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.05,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 62,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 6488.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 153,
                    "display": "false"
                },
                "car_ID": {
                    "values": 154,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corona hardtop",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 169.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 59.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2280,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.05,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 62,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 31,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 6918.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 154,
                    "display": "false"
                },
                "car_ID": {
                    "values": 155,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corolla 1600 (sw)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "4wd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 169.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 59.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2290,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.05,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 62,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 7898.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 155,
                    "display": "false"
                },
                "car_ID": {
                    "values": 156,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota carina",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "4wd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 169.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 63.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 59.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3110,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 92,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.05,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 62,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 8778.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 156,
                    "display": "false"
                },
                "car_ID": {
                    "values": 157,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota mark ii",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 166.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2081,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 70,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 30,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 6938.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 157,
                    "display": "false"
                },
                "car_ID": {
                    "values": 158,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corolla 1200",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 166.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2109,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 70,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 30,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 37,
                    "display": "true"
                },
                "price": {
                    "values": 7198.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 158,
                    "display": "false"
                },
                "car_ID": {
                    "values": 159,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corona",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 166.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2275,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 110,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.27,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.35,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 22.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 56,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4500,
                    "display": "true"
                },
                "citympg": {
                    "values": 34,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 36,
                    "display": "true"
                },
                "price": {
                    "values": 7898.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 159,
                    "display": "false"
                },
                "car_ID": {
                    "values": 160,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corolla",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 166.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2275,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 110,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.27,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.35,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 22.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 56,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4500,
                    "display": "true"
                },
                "citympg": {
                    "values": 38,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 47,
                    "display": "true"
                },
                "price": {
                    "values": 7788.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 160,
                    "display": "false"
                },
                "car_ID": {
                    "values": 161,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corona",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 166.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2094,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 70,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 38,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 47,
                    "display": "true"
                },
                "price": {
                    "values": 7738.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 161,
                    "display": "false"
                },
                "car_ID": {
                    "values": 162,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corolla",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 166.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2122,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 70,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 28,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 8358.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 162,
                    "display": "false"
                },
                "car_ID": {
                    "values": 163,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota mark ii",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 95.7,
                    "display": "true"
                },
                "carlength": {
                    "values": 166.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.4,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.8,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2140,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 70,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 28,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 9258.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 163,
                    "display": "false"
                },
                "car_ID": {
                    "values": 164,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corolla liftback",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 168.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2169,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 70,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 29,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 8058.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 164,
                    "display": "false"
                },
                "car_ID": {
                    "values": 165,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corona",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 168.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2204,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "2bbl",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.03,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 70,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 29,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 8238.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 165,
                    "display": "false"
                },
                "car_ID": {
                    "values": 166,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota celica gt liftback",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 168.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2265,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.24,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.08,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 112,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 6600,
                    "display": "true"
                },
                "citympg": {
                    "values": 26,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 29,
                    "display": "true"
                },
                "price": {
                    "values": 9298.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 166,
                    "display": "false"
                },
                "car_ID": {
                    "values": 167,
                    "display": "true"
                },
                "symboling": {
                    "values": 1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corolla tercel",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 168.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2300,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 98,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.24,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.08,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.4,
                    "display": "true"
                },
                "horsepower": {
                    "values": 112,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 6600,
                    "display": "true"
                },
                "citympg": {
                    "values": 26,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 29,
                    "display": "true"
                },
                "price": {
                    "values": 9538.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 167,
                    "display": "false"
                },
                "car_ID": {
                    "values": 168,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corona liftback",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hardtop",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2540,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 146,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.5,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 116,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 8449.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 168,
                    "display": "false"
                },
                "car_ID": {
                    "values": 169,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corolla",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hardtop",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2536,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 146,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.5,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 116,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 9639.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 169,
                    "display": "false"
                },
                "car_ID": {
                    "values": 170,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota starlet",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2551,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 146,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.5,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 116,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 9989.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 170,
                    "display": "false"
                },
                "car_ID": {
                    "values": 171,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota tercel",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hardtop",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2679,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 146,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.5,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 116,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 11199.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 171,
                    "display": "false"
                },
                "car_ID": {
                    "values": 172,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corolla",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2714,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 146,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.5,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 116,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 11549.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 172,
                    "display": "false"
                },
                "car_ID": {
                    "values": 173,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota cressida",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "convertible",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 98.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 176.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.6,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2975,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 146,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.5,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 116,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 30,
                    "display": "true"
                },
                "price": {
                    "values": 17669.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 173,
                    "display": "false"
                },
                "car_ID": {
                    "values": 174,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corolla",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 102.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 175.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.9,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2326,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.31,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.54,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.7,
                    "display": "true"
                },
                "horsepower": {
                    "values": 92,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4200,
                    "display": "true"
                },
                "citympg": {
                    "values": 29,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 8948.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 174,
                    "display": "false"
                },
                "car_ID": {
                    "values": 175,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota celica gt",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 102.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 175.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.9,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2480,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 110,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.27,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.35,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 22.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 73,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4500,
                    "display": "true"
                },
                "citympg": {
                    "values": 30,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 33,
                    "display": "true"
                },
                "price": {
                    "values": 10698.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 175,
                    "display": "false"
                },
                "car_ID": {
                    "values": 176,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corona",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 102.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 175.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.9,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2414,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.31,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.54,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.7,
                    "display": "true"
                },
                "horsepower": {
                    "values": 92,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4200,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 9988.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 176,
                    "display": "false"
                },
                "car_ID": {
                    "values": 177,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corolla",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 102.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 175.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.9,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2414,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.31,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.54,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.7,
                    "display": "true"
                },
                "horsepower": {
                    "values": 92,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4200,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 10898.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 177,
                    "display": "false"
                },
                "car_ID": {
                    "values": 178,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota mark ii",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 102.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 175.6,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 53.9,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2458,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 122,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.31,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.54,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.7,
                    "display": "true"
                },
                "horsepower": {
                    "values": 92,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4200,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 11248.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 178,
                    "display": "false"
                },
                "car_ID": {
                    "values": 179,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corolla liftback",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 102.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 183.5,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.7,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2976,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 171,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.27,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.35,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 161,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 20,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 16558.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 179,
                    "display": "false"
                },
                "car_ID": {
                    "values": 180,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota corona",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 102.9,
                    "display": "true"
                },
                "carlength": {
                    "values": 183.5,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.7,
                    "display": "true"
                },
                "carheight": {
                    "values": 52.0,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3016,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 171,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.27,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.35,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.3,
                    "display": "true"
                },
                "horsepower": {
                    "values": 161,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 15998.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 180,
                    "display": "false"
                },
                "car_ID": {
                    "values": 181,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyota starlet",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 104.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 187.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3131,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 171,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.27,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.35,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.2,
                    "display": "true"
                },
                "horsepower": {
                    "values": 156,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 20,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 15690.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 181,
                    "display": "false"
                },
                "car_ID": {
                    "values": 182,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "toyouta tercel",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 104.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 187.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 54.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3151,
                    "display": "true"
                },
                "enginetype": {
                    "values": "dohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 161,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.27,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.35,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.2,
                    "display": "true"
                },
                "horsepower": {
                    "values": 156,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5200,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 15750.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 182,
                    "display": "false"
                },
                "car_ID": {
                    "values": 183,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "vokswagen rabbit",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 171.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2261,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.01,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 23.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 52,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 37,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 46,
                    "display": "true"
                },
                "price": {
                    "values": 7775.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 183,
                    "display": "false"
                },
                "car_ID": {
                    "values": 184,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "volkswagen 1131 deluxe sedan",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 171.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2209,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 109,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 85,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5250,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 7975.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 184,
                    "display": "false"
                },
                "car_ID": {
                    "values": 185,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "volkswagen model 111",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 171.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2264,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.01,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 23.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 52,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 37,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 46,
                    "display": "true"
                },
                "price": {
                    "values": 7995.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 185,
                    "display": "false"
                },
                "car_ID": {
                    "values": 186,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "volkswagen type 3",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 171.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2212,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 109,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 85,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5250,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 8195.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 186,
                    "display": "false"
                },
                "car_ID": {
                    "values": 187,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "volkswagen 411 (sw)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 171.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2275,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 109,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 85,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5250,
                    "display": "true"
                },
                "citympg": {
                    "values": 27,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 34,
                    "display": "true"
                },
                "price": {
                    "values": 8495.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 187,
                    "display": "false"
                },
                "car_ID": {
                    "values": 188,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "volkswagen super beetle",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 171.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2319,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.01,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 23.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4500,
                    "display": "true"
                },
                "citympg": {
                    "values": 37,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 42,
                    "display": "true"
                },
                "price": {
                    "values": 9495.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 188,
                    "display": "false"
                },
                "car_ID": {
                    "values": 189,
                    "display": "true"
                },
                "symboling": {
                    "values": 2,
                    "display": "true"
                },
                "CarName": {
                    "values": "volkswagen dasher",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 97.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 171.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 65.5,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.7,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2300,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 109,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 10.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 100,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 26,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 32,
                    "display": "true"
                },
                "price": {
                    "values": 9995.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 189,
                    "display": "false"
                },
                "car_ID": {
                    "values": 190,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "vw dasher",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "convertible",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 159.3,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.6,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2254,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 109,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 90,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 29,
                    "display": "true"
                },
                "price": {
                    "values": 11595.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 190,
                    "display": "false"
                },
                "car_ID": {
                    "values": 191,
                    "display": "true"
                },
                "symboling": {
                    "values": 3,
                    "display": "true"
                },
                "CarName": {
                    "values": "vw rabbit",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "two",
                    "display": "true"
                },
                "carbody": {
                    "values": "hatchback",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 94.5,
                    "display": "true"
                },
                "carlength": {
                    "values": 165.7,
                    "display": "true"
                },
                "carwidth": {
                    "values": 64.0,
                    "display": "true"
                },
                "carheight": {
                    "values": 51.4,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2221,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 109,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 90,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 29,
                    "display": "true"
                },
                "price": {
                    "values": 9980.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 191,
                    "display": "false"
                },
                "car_ID": {
                    "values": 192,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "volkswagen rabbit",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 100.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 180.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2661,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "five",
                    "display": "true"
                },
                "enginesize": {
                    "values": 136,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 110,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 24,
                    "display": "true"
                },
                "price": {
                    "values": 13295.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 192,
                    "display": "false"
                },
                "car_ID": {
                    "values": 193,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "volkswagen rabbit custom",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 100.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 180.2,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2579,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 97,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.01,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 23.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 68,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4500,
                    "display": "true"
                },
                "citympg": {
                    "values": 33,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 38,
                    "display": "true"
                },
                "price": {
                    "values": 13845.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 193,
                    "display": "false"
                },
                "car_ID": {
                    "values": 194,
                    "display": "true"
                },
                "symboling": {
                    "values": 0,
                    "display": "true"
                },
                "CarName": {
                    "values": "volkswagen dasher",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "fwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 100.4,
                    "display": "true"
                },
                "carlength": {
                    "values": 183.1,
                    "display": "true"
                },
                "carwidth": {
                    "values": 66.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.1,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2563,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 109,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.19,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 88,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 25,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 31,
                    "display": "true"
                },
                "price": {
                    "values": 12290.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 194,
                    "display": "false"
                },
                "car_ID": {
                    "values": 195,
                    "display": "true"
                },
                "symboling": {
                    "values": -2,
                    "display": "true"
                },
                "CarName": {
                    "values": "volvo 145e (sw)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 104.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 188.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.2,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2912,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 141,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.78,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 114,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 23,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 12940.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 195,
                    "display": "false"
                },
                "car_ID": {
                    "values": 196,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "volvo 144ea",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 104.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 188.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 57.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3034,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 141,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.78,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 114,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 23,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 13415.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 196,
                    "display": "false"
                },
                "car_ID": {
                    "values": 197,
                    "display": "true"
                },
                "symboling": {
                    "values": -2,
                    "display": "true"
                },
                "CarName": {
                    "values": "volvo 244dl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 104.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 188.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.2,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2935,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 141,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.78,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 114,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 15985.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 197,
                    "display": "false"
                },
                "car_ID": {
                    "values": 198,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "volvo 245",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 104.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 188.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 57.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3042,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 141,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.78,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 114,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 24,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 16515.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 198,
                    "display": "false"
                },
                "car_ID": {
                    "values": 199,
                    "display": "true"
                },
                "symboling": {
                    "values": -2,
                    "display": "true"
                },
                "CarName": {
                    "values": "volvo 264gl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 104.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 188.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 56.2,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3045,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 130,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 162,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5100,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 22,
                    "display": "true"
                },
                "price": {
                    "values": 18420.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 199,
                    "display": "false"
                },
                "car_ID": {
                    "values": 200,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "volvo diesel",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "wagon",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 104.3,
                    "display": "true"
                },
                "carlength": {
                    "values": 188.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 67.2,
                    "display": "true"
                },
                "carheight": {
                    "values": 57.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3157,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 130,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.62,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 7.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 162,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5100,
                    "display": "true"
                },
                "citympg": {
                    "values": 17,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 22,
                    "display": "true"
                },
                "price": {
                    "values": 18950.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 200,
                    "display": "false"
                },
                "car_ID": {
                    "values": 201,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "volvo 145e (sw)",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 109.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 188.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 2952,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 141,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.78,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 114,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 23,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 28,
                    "display": "true"
                },
                "price": {
                    "values": 16845.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 201,
                    "display": "false"
                },
                "car_ID": {
                    "values": 202,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "volvo 144ea",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 109.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 188.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.8,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3049,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 141,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.78,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.7,
                    "display": "true"
                },
                "horsepower": {
                    "values": 160,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5300,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 19045.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 202,
                    "display": "false"
                },
                "car_ID": {
                    "values": 203,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "volvo 244dl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "std",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 109.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 188.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3012,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohcv",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 173,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.58,
                    "display": "true"
                },
                "stroke": {
                    "values": 2.87,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 8.8,
                    "display": "true"
                },
                "horsepower": {
                    "values": 134,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5500,
                    "display": "true"
                },
                "citympg": {
                    "values": 18,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 23,
                    "display": "true"
                },
                "price": {
                    "values": 21485.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 203,
                    "display": "false"
                },
                "car_ID": {
                    "values": 204,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "volvo 246",
                    "display": "true"
                },
                "fueltype": {
                    "values": "diesel",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 109.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 188.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3217,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "six",
                    "display": "true"
                },
                "enginesize": {
                    "values": 145,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "idi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.01,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.4,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 23.0,
                    "display": "true"
                },
                "horsepower": {
                    "values": 106,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 4800,
                    "display": "true"
                },
                "citympg": {
                    "values": 26,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 27,
                    "display": "true"
                },
                "price": {
                    "values": 22470.0,
                    "display": "true"
                }
            },
            {
                "index": {
                    "values": 204,
                    "display": "false"
                },
                "car_ID": {
                    "values": 205,
                    "display": "true"
                },
                "symboling": {
                    "values": -1,
                    "display": "true"
                },
                "CarName": {
                    "values": "volvo 264gl",
                    "display": "true"
                },
                "fueltype": {
                    "values": "gas",
                    "display": "true"
                },
                "aspiration": {
                    "values": "turbo",
                    "display": "true"
                },
                "doornumber": {
                    "values": "four",
                    "display": "true"
                },
                "carbody": {
                    "values": "sedan",
                    "display": "true"
                },
                "drivewheel": {
                    "values": "rwd",
                    "display": "true"
                },
                "enginelocation": {
                    "values": "front",
                    "display": "true"
                },
                "wheelbase": {
                    "values": 109.1,
                    "display": "true"
                },
                "carlength": {
                    "values": 188.8,
                    "display": "true"
                },
                "carwidth": {
                    "values": 68.9,
                    "display": "true"
                },
                "carheight": {
                    "values": 55.5,
                    "display": "true"
                },
                "curbweight": {
                    "values": 3062,
                    "display": "true"
                },
                "enginetype": {
                    "values": "ohc",
                    "display": "true"
                },
                "cylindernumber": {
                    "values": "four",
                    "display": "true"
                },
                "enginesize": {
                    "values": 141,
                    "display": "true"
                },
                "fuelsystem": {
                    "values": "mpfi",
                    "display": "true"
                },
                "boreratio": {
                    "values": 3.78,
                    "display": "true"
                },
                "stroke": {
                    "values": 3.15,
                    "display": "true"
                },
                "compressionratio": {
                    "values": 9.5,
                    "display": "true"
                },
                "horsepower": {
                    "values": 114,
                    "display": "true"
                },
                "peakrpm": {
                    "values": 5400,
                    "display": "true"
                },
                "citympg": {
                    "values": 19,
                    "display": "true"
                },
                "highwaympg": {
                    "values": 25,
                    "display": "true"
                },
                "price": {
                    "values": 22625.0,
                    "display": "true"
                }
            }
        ]
    }

    
}