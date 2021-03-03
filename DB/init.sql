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

CREATE TABLE mlaas.model_experiment_tbl
(
   exp_unq_id bigserial,
   experiment_id  integer,
   run_uuid text,
   project_id bigint,
   dataset_id bigint,
   user_id integer,
   model_id  integer,
   model_mode  text,
   dag_run_id varchar,
   status varchar NOT NULL DEFAULT 'running', 
   exp_created_on TIMESTAMPTZ NOT NULL DEFAULT NOW()              
);

CREATE TABLE mlaas.model_master_tbl (
 	model_id integer,
   model_name text,
   model_desc text,
   model_parameter text,
   model_type text,
   algorithm_type text,
   model_created_on TIMESTAMPTZ NOT NULL DEFAULT NOW()
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

CREATE TABLE mlaas.model_dags_tbl
(
unq_id bigserial,
dag_id varchar,
exp_name varchar,
run_id varchar,
execution_date timestamptz,
project_id bigint,
dataset_id bigint,
user_id integer,
model_mode varchar,
dag_created_on TIMESTAMPTZ NOT NULL DEFAULT NOW()
);


create sequence unq_num_seq
increment 1;


SELECT setval('unq_num_seq', 1);
