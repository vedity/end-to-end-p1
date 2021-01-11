import { MenuItem } from './menu.model';

export const MENU: MenuItem[] =
[
        {
            "id": 1,
            "label": "MENU",
            "isTitle": "true"
        },
        {
            "id": 2,
            "label": "Projects",
            "icon": "bx-home-circle",
            "subItems": [
                {
                    "id": 3,
                    "label": "Create Project",
                    "link": "/create",
                    "parentId": 2.0
                },
                {
                    "id": 4,
                    "label": "Create Dataset",
                    "link": "/dataset",
                    "parentId": 2.0
                },
                {
                    "id": 5,
                    "label": "All Projects",
                    "link": "/project",
                    "parentId": 2.0
                }
            ]
        },
        {
            "id": 6,
            "label": "Data Preprocess",
            "icon": "bx-home-circle",
            "subItems": [
                {
                    "id": 7,
                    "label": "Data Exploration ",
                    "link": null,
                    "parentId": 6.0
                },
                {
                    "id": 8,
                    "label": "Data Visualization",
                    "link": null,
                    "parentId": 6.0
                },
                {
                    "id": 9,
                    "label": "Data Clean-up",
                    "link": null,
                    "parentId": 6.0
                }
            ]
        },
        {
            "id": 10,
            "label": "Data Model",
            "icon": null,
            "subItems": [
                {
                    "id": 11,
                    "label": "Data splitter",
                    "link": null,
                    "parentId": 10.0
                },
                {
                    "id": 12,
                    "label": "Performance Metrics",
                    "link": null,
                    "parentId": 10.0
                }
            ]
        },
        {
            "id": 13,
            "label": "Prediction Results",
            "icon": "bx-home-circle",
            "subItems": [
                {
                    "id": 14,
                    "label": "Prediction and summary",
                    "link": null,
                    "parentId": 13.0
                }
            ]
        }
    ]

