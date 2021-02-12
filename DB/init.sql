CREATE schema mlaas;
CREATE TABLE mlaas.menu_table (
 	id int,
 	firstName varchar(255),
 	lastName varchar(255),
 	address text
 	);

CREATE TABLE mlaas.user_auth_table (
 	id int,
 	firstName varchar(255),
 	lastName varchar(255),
 	address text
 	);

CREATE TABLE mlaas.model_experiment_tbl (
 	exp_unq_id bigserial,
    experiment_id  integer,
    experiment_name  text,
    experiment_desc text,
    run_uuid text,
    project_id bigint,
    dataset_id bigint,
    user_id integer,
    model_id  integer,
    model_mode  text,
    exp_created_on TIMESTAMPTZ NOT NULL DEFAULT NOW()              
 	);

CREATE TABLE mlaas.model_master_tbl (
 	model_id integer,
    model_name text,
    model_desc text,
    model_parameter text,
    model_type text,
    algorithm_type text
    );

CREATE TABLE mlaas.cleaned_ref_tbl (
 	unq_id bigserial,
    project_id integer,
    dataset_id integer,
    user_id integer,
    input_features text,
    target_features text,
    scaled_data_table text
    );