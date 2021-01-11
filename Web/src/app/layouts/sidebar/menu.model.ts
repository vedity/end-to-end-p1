export interface MenuItem {
    id?: number;
    label?: string;
    icon?: string;
    link?: string;
    subItems?: any;
    isTitle?: string;
    badge?: any;
    parentId?: number;
    isLayout?: boolean;
}
