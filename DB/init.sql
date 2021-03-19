CREATE schema mlaas;
CREATE schema mlflow;
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



CREATE TABLE mlflow.model_experiment_tbl
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

CREATE TABLE mlflow.model_master_tbl (
 	model_id integer,
   model_name text,
   model_desc text,
   model_parameter text,
   model_type text,
   algorithm_type text,
   model_created_on TIMESTAMPTZ NOT NULL DEFAULT NOW()
    );

CREATE TABLE mlflow.cleaned_ref_tbl (
 	unq_id bigserial,
    project_id integer,
    dataset_id integer,
    user_id integer,
    input_features text,
    target_features text,
    scaled_data_table text
    );

CREATE TABLE mlflow.model_dags_tbl
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


-- CREATE OR REPLACE VIEW mlaas.score_view
-- AS SELECT a.experiment_id,
-- a.project_id,
-- a.run_uuid,
-- a.cv_score,
-- mr.value AS holdout_score
-- FROM ( SELECT met.experiment_id,
-- met.project_id,
-- met.run_uuid,
-- m.key,
-- m.value AS cv_score
-- FROM mlaas.model_experiment_tbl met,
-- mlaas.metrics m
-- WHERE met.run_uuid = m.run_uuid AND m.key = 'cv_score') a,
-- mlaas.metrics mr
-- WHERE a.run_uuid = mr.run_uuid AND mr.key = 'holdout_score';

CREATE TABLE mlflow.manual_model_params_tbl (
	user_id int4 NULL,
	project_id int4 NULL,
	dataset_id int4 NULL,
	exp_name varchar NULL,
	model_id int4 NULL,
	hyperparameters varchar null
);

CREATE TABLE mlflow.model_hyperparams_tbl (
	model_id int4 NULL,
	hyperparameter varchar NULL,
	param_value varchar NULL,
	display_type varchar NULL
);






