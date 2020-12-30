import { MenuItem } from './menu.model';

export const MENU: MenuItem[] =
 [
    {
        id: 1,
        label: 'MENU',
        isTitle: true
    },
    {
        id: 2,
        label: 'Data Ingestion',
        icon: 'bx-home-circle',
        subItems: [
            {
                id: 3,
                label: 'Project List',
                link: '/project',
                parentId: 2
            },
            {
                id: 4,
                label: 'Create Project',
                link: '/create',
                parentId: 2
            },
            {
                id: 5,
                label: 'Dataset List',
                link: '/dataset',
                parentId: 2
            },
            {
                id: 6,
                label: 'Data Detail',
                link: '/datadetail',
                parentId: 2
            },
        ]
    },
    {
        id: 7,
        label: 'Schema Mapping',
        icon: 'bx-home-circle',
        link: 'schema/create',
    },

];

