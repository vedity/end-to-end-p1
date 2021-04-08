export class scaleandsplit{
    random_state?:string;
    train_random_state?:string;
    split_method ?:string;
    cv?: number;
    test_ratio ?:number;
    scaling_op ?:string;
    split_ratio?:number;
    valid_ratio ?:number;

}

export class saveAsModal{
    isPrivate?: boolean;
    dataset_name?: string;
    description?: string;
}