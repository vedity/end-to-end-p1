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
        badge: {
            variant: 'info',
            text: '3',
        },
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


];

