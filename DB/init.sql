CREATE schema mlaas;
CREATE schema mlflow;

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

CREATE TABLE mlaas.model_master_tbl 
(
	model_id integer,
	model_name text,
	model_desc text,
	model_type text,
	algorithm_type text,
	target_type text,
	model_created_on TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Inserting Data into the model_master table.
insert into mlaas.model_master_tbl values (1,'Linear_Regression_Sklearn','Simple Linear Regression Model','Regression', 'Multi','Single_Target');

insert into mlaas.model_master_tbl values (2,'Linear_Regression_Keras','Simple Linear Regression Model Using Nueral Network','Regression', 'Multi', 'Single_Target');

insert into mlaas.model_master_tbl values (3,'XGB_Regressor','Ensemble Regression Model','Regression', 'Multi', 'Single_Target');

insert into mlaas.model_master_tbl values (4,'Logistic_Regression_Sklearn','Simple Logistic Regression Model','Classification','Binary','Single_Target');

CREATE TABLE mlaas.model_hyperparams_tbl
(
	model_id int4 NULL,
	param_name varchar NULL,
	param_value varchar NULL,
	display_type varchar NULL
);


insert into mlaas.model_hyperparams_tbl values (1, '', '[]', '');

insert into mlaas.model_hyperparams_tbl values (2, 'epochs', '[]', '');

insert into mlaas.model_hyperparams_tbl values (2, 'learning_rate', '[0.001, 1]', 'validation');

insert into mlaas.model_hyperparams_tbl values (2, 'batch_size', '[8, 16, 32, 64, 128, 256]', 'dropdown');

insert into mlaas.model_hyperparams_tbl values (2, 'loss', '["Mean_Absolute_Error", "Mean_Squared_Error", "Mean_Absolute_Percentage_Error"]', 'dropdown');

insert into mlaas.model_hyperparams_tbl values (2, 'optimizer', '["SGD", "RMSProp", "Adam"]', 'dropdown');

insert into mlaas.model_hyperparams_tbl values (2, 'activation', '["Relu", "Sigmoid", "Tanh"]', 'dropdown');

insert into mlaas.model_hyperparams_tbl values (3, '', '[]', '');

insert into mlaas.model_hyperparams_tbl values (4, '', '[]', '');


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

CREATE TABLE mlaas.activity_master_tbl (
	"index" int8 NULL,
	activity_id int8 NULL,
	activity_name text NULL,
	activity_description text NULL,
	"language" text NULL,
	operation text NULL,
	code int8 NULL,
	parent_activity_id int8 NULL,
	user_input int8 NULL,
	check_type int8 NULL
);


CREATE TABLE mlaas.menu_tbl (
	id int8 NULL,
	modulename text NULL,
	menuname text NULL,
	parent_id float8 NULL,
	url text NULL,
	icon text NULL
);

CREATE TABLE mlaas.parent_activity_tbl (
	parent_activity_id int8 NULL,
	parent_activity_name text NULL,
	tab_id int8 NULL
);

CREATE TABLE mlaas.preprocess_tab_tbl (
	tab_id int8 NULL,
	tab_name text NULL
);


CREATE TABLE mlaas.user_auth_tbl (
	uid int8 NULL,
	user_name text NULL,
	"password" text NULL
);

CREATE TABLE mlaas.cleanup_dag_status (
	dag_index bigserial NOT NULL,
	dag_id text,
	status varchar(1) NOT NULL DEFAULT '0'
);

CREATE TABLE mlaas.project_tbl (
	project_id bigserial NOT NULL ,
	project_name text NULL,
	project_desc text NULL,
	dataset_status int4 NOT NULL DEFAULT '-1'::integer,
	model_status int4 NOT NULL DEFAULT '-1'::integer,
	deployment_status int4 NOT NULL DEFAULT '-1'::integer,
	user_name text NULL,
	original_dataset_id int8 NULL,
	dataset_id int8 NULL,
	schema_id bigserial NOT NULL ,
	cleanup_dag_id text,
	model_dag_id text,
	input_features text NULL,
	target_features text NULL,
	scaled_split_parameters text NULL,
	problem_type text NULL,
	created_on timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE mlaas.dataset_tbl (
	dataset_id bigserial NOT NULL,
	dataset_name text NULL,
	file_name text NULL,
	file_size text NULL,
	no_of_rows int4 NOT NULL DEFAULT 0,
	dataset_table_name text NULL,
	dataset_visibility text NULL,
	user_name text NULL,
	dataset_desc text NULL,
	page_name text NULL,
	created_on timestamptz NOT NULL DEFAULT now()
);


CREATE TABLE mlaas.schema_tbl (
	"index" bigserial NOT NULL,
	schema_id int8 NULL,
	column_name text NULL,
	changed_column_name text NULL,
	data_type text NULL,
	column_attribute text NULL,
	missing_flag text NULL,
	noise_flag text NULL
);

--Create activity_deatil table
CREATE TABLE mlaas.activity_detail_tbl (
    "index" bigserial NOT NULL,
    activity_id int8 NULL,
    user_name text NULL,
    project_id int8 NULL,
    dataset_id int8 NULL,
    activity_description text NULL,
    start_time timestamp NOT NULL DEFAULT now(),
    end_time timestamp NULL,
    column_id text NULL,
    "parameter" text NULL
);
 

--Insert menu_tbl
Insert into  mlaas.menu_tbl values (2,'DI','Data Ingestion',null,null,' mdi-database-import');
Insert into  mlaas.menu_tbl values (3,'DI','Datasets','2','/dataset',null);
Insert into  mlaas.menu_tbl values (4,'DI','Projects','2','/project',null);
Insert into  mlaas.menu_tbl values (5,'DP','Data Pre-Proecessing',null,null,'mdi-database-sync');
Insert into  mlaas.menu_tbl values (6,'DP','Schema Mapping','5','/schema',null);
Insert into  mlaas.menu_tbl values (7,'DP','Data Cleanup','5','/cleanup',null);

--Insert user_auth_tbl
Insert into mlaas.user_auth_tbl values(1,'mehul','mehul');
Insert into mlaas.user_auth_tbl values(2,'riddhi','riddhi');
Insert into mlaas.user_auth_tbl values(3,'vipul','vipul');
Insert into mlaas.user_auth_tbl values(4,'jay','jay');
Insert into mlaas.user_auth_tbl values(5,'abhishek','abhishek');
Insert into mlaas.user_auth_tbl values(6,'shivani','shivani');
Insert into mlaas.user_auth_tbl values(7,'mansi','mansi');
Insert into mlaas.user_auth_tbl values(8,'swati','swati');
Insert into mlaas.user_auth_tbl values(9,'bhavin','bhavin');
Insert into mlaas.user_auth_tbl values(10,'raj','raj');
Insert into mlaas.user_auth_tbl values(11,'nisha','nisha');
Insert into mlaas.user_auth_tbl values(12,'mann','mann');
Insert into mlaas.user_auth_tbl values(13,'bhavsik','bhavsik');
Insert into mlaas.user_auth_tbl values(14,'prayagraj','prayagraj');
Insert into mlaas.user_auth_tbl values(15,'brijraj','brijraj');
Insert into mlaas.user_auth_tbl values(16,'karishma','karishma');
Insert into mlaas.user_auth_tbl values(17,'denisha','denisha');


--Insert parent_activity_tbl
Insert into mlaas.parent_activity_tbl values(1,'Missing Value Handling',1);
Insert into mlaas.parent_activity_tbl values(2,'Noise Handling',1);
Insert into mlaas.parent_activity_tbl values(3,'Outlier Handling',2);
Insert into mlaas.parent_activity_tbl values(4,'Scaling',2);
Insert into mlaas.parent_activity_tbl values(5,'Encoding',2);
Insert into mlaas.parent_activity_tbl values(6,'Math Operations',2);


--Insert preprocess_tab_tbl
Insert into mlaas.preprocess_tab_tbl values(1,'Missing Value Handling');
Insert into mlaas.preprocess_tab_tbl values(2,'Transformation');


--Insert activity master
Insert into mlaas.activity_master_tbl values (1,2,'Delete Dataset','You have deleted dataset','US','Delete',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (2,3,'Create Project','You have created project','US','Create',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (3,1,'Create Dataset','You have created dataset','US','Create',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (4,4,'Delete Project','You have deleted project','US','Delete',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (5,5,'Column name updated','You have updated the name of Columns','US','Update',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (6,6,'Selected Target Column','You have selected Columns  *  of dataset $ as Target Columns','US','Select',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (7,7,'Ignored Column','You have ignored Columns *','US','Ignore',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (8,8,'Created new dataset','You have saved new dataset','US','Create',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (9,9,'Discard Missing Values','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (10,9,'Discard Missing Values','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (11,9,'Discard Missing Values','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (12,10,'Discard Noise','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (13,10,'Discard Noise','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (14,10,'Discard Noise','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (15,11,'Delete Above','operation on column * failed','US','Operation',0,3,1,2);
Insert into mlaas.activity_master_tbl values (16,11,'Delete Above','operation on column * in process','US','Operation',1,3,1,2);
Insert into mlaas.activity_master_tbl values (17,11,'Delete Above','operation on column * completed','US','Operation',2,3,1,2);
Insert into mlaas.activity_master_tbl values (18,12,'Delete Below','operation on column * failed','US','Operation',0,3,1,2);
Insert into mlaas.activity_master_tbl values (19,12,'Delete Below','operation on column * in process','US','Operation',1,3,1,2);
Insert into mlaas.activity_master_tbl values (20,12,'Delete Below','operation on column * completed','US','Operation',2,3,1,2);
Insert into mlaas.activity_master_tbl values (21,13,'Remove Noise','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (22,13,'Remove Noise','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (23,13,'Remove Noise','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (24,14,'Mean Imputation','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (25,14,'Mean Imputation','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (26,14,'Mean Imputation','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (27,15,'Median Imputation','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (28,15,'Median Imputation','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (29,15,'Median Imputation','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (30,16,'Mode Imputation','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (31,16,'Mode Imputation','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (32,16,'Mode Imputation','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (33,17,'Arbitarry Value Imputation','operation on column * failed','US','Operation',0,1,1,2);
Insert into mlaas.activity_master_tbl values (34,17,'Arbitarry Value Imputation','operation on column * in process','US','Operation',1,1,1,2);
Insert into mlaas.activity_master_tbl values (35,17,'Arbitarry Value Imputation','operation on column * completed','US','Operation',2,1,1,2);
Insert into mlaas.activity_master_tbl values (36,18,'End_or_Tail Imputation','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (37,18,'End_or_Tail Imputation','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (38,18,'End_or_Tail Imputation','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (39,19,'Frequent Category Imputation','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (40,19,'Frequent Category Imputation','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (41,19,'Frequent Category Imputation','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (42,20,'Add Missing Category','operation on column * failed','US','Operation',0,1,1,3);
Insert into mlaas.activity_master_tbl values (43,20,'Add Missing Category','operation on column * in process','US','Operation',1,1,1,3);
Insert into mlaas.activity_master_tbl values (44,20,'Add Missing Category','operation on column * completed','US','Operation',2,1,1,3);
Insert into mlaas.activity_master_tbl values (45,21,'Random Sample Imputation','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (46,21,'Random Sample Imputation','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (47,21,'Random Sample Imputation','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (48,22,'Replace Noise with Mean','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (49,22,'Replace Noise with Mean','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (50,22,'Replace Noise with Mean','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (51,23,'Replace Noise with Median','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (52,23,'Replace Noise with Median','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (53,23,'Replace Noise with Median','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (54,24,'Replace Noise with Mode','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (55,24,'Replace Noise with Mode','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (56,24,'Replace Noise with Mode','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (57,25,'Replace Noise with End_or_Tail Value','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (58,25,'Replace Noise with End_or_Tail Value','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (59,25,'Replace Noise with End_or_Tail Value','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (60,26,'Replace Noise with Random Value','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (61,26,'Replace Noise with Random Value','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (62,26,'Replace Noise with Random Value','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (63,27,'Replace Noise with Arbitry Value','operation on column * failed','US','Operation',0,2,1,2);
Insert into mlaas.activity_master_tbl values (64,27,'Replace Noise with Arbitry Value','operation on column * in process','US','Operation',1,2,1,2);
Insert into mlaas.activity_master_tbl values (65,27,'Replace Noise with Arbitry Value','operation on column * completed','US','Operation',2,2,1,2);
Insert into mlaas.activity_master_tbl values (66,28,'Remove outliers with Extreme Value analysis','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (67,28,'Remove outliers with Extreme Value analysis','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (68,28,'Remove outliers with Extreme Value analysis','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (69,29,'Remove outliers with Z-score Detection Method','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (70,29,'Remove outliers with Z-score Detection Method','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (71,29,'Remove outliers with Z-score Detection Method','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (72,30,'Replace Outliers with Mean using Extreme Value Analysis Detection','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (73,30,'Replace Outliers with Mean using Extreme Value Analysis Detection','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (74,30,'Replace Outliers with Mean using Extreme Value Analysis Detection','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (75,31,'Replace Outliers with Mean using Z-score Detection','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (76,31,'Replace Outliers with Mean using Z-score Detection','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (77,31,'Replace Outliers with Mean using Z-score Detection','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (78,32,'Replace Outliers with Median using Extreme Value Analysis Detection','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (79,32,'Replace Outliers with Median using Extreme Value Analysis Detection','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (80,32,'Replace Outliers with Median using Extreme Value Analysis Detection','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (81,33,'Replace Outliers with Median using Z-score Detection','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (82,33,'Replace Outliers with Median using Z-score Detection','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (83,33,'Replace Outliers with Median using Z-score Detection','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (84,34,'Apply Log Transformation','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (85,34,'Apply Log Transformation','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (86,34,'Apply Log Transformation','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (87,35,'Label Encoding','operation on column * failed','US','Operation',0,5,0,0);
Insert into mlaas.activity_master_tbl values (88,35,'Label Encoding','operation on column * in process','US','Operation',1,5,0,0);
Insert into mlaas.activity_master_tbl values (89,35,'Label Encoding','operation on column * completed','US','Operation',2,5,0,0);
Insert into mlaas.activity_master_tbl values (90,36,'One Hot Encoding','operation on column * failed','US','Operation',0,5,0,0);
Insert into mlaas.activity_master_tbl values (91,36,'One Hot Encoding','operation on column * in process','US','Operation',1,5,0,0);
Insert into mlaas.activity_master_tbl values (92,36,'One Hot Encoding','operation on column * completed','US','Operation',2,5,0,0);
Insert into mlaas.activity_master_tbl values (93,37,'Add to Column','operation on column * failed','US','Operation',0,6,1,2);
Insert into mlaas.activity_master_tbl values (94,37,'Add to Column','operation on column * in process','US','Operation',1,6,1,2);
Insert into mlaas.activity_master_tbl values (95,37,'Add to Column','operation on column * completed','US','Operation',2,6,1,2);
Insert into mlaas.activity_master_tbl values (96,38,'Subtract from Column','operation on column * failed','US','Operation',0,6,1,2);
Insert into mlaas.activity_master_tbl values (97,38,'Subtract from Column','operation on column * in process','US','Operation',1,6,1,2);
Insert into mlaas.activity_master_tbl values (98,38,'Subtract from Column','operation on column * completed','US','Operation',2,6,1,2);
Insert into mlaas.activity_master_tbl values (99,39,'Divide from column','operation on column * failed','US','Operation',0,6,1,5);
Insert into mlaas.activity_master_tbl values (100,39,'Divide from column','operation on column * in process','US','Operation',1,6,1,5);
Insert into mlaas.activity_master_tbl values (101,39,'Divide from column','operation on column * completed','US','Operation',2,6,1,5);
Insert into mlaas.activity_master_tbl values (102,40,'Multiply into column','operation on column * failed','US','Operation',0,6,1,2);
Insert into mlaas.activity_master_tbl values (103,40,'Multiply into column','operation on column * in process','US','Operation',1,6,1,2);
Insert into mlaas.activity_master_tbl values (104,40,'Multiply into column','operation on column * completed','US','Operation',2,6,1,2);
Insert into mlaas.activity_master_tbl values (105,41,'Created Experiment','You have created experiment','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (106,42,'Selected Auto Modeling','You have selected Auto Modeling for experiment','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (107,43,'Selected Manual Modeling','You have selected Manual Modeling for experiment','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (108,44,'Defined Modeling parameters','You have selected the algorithm * and defined the parameters for experiment #','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (109,45,'Started Modeling','Modelling has been started for experiment','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (110,46,'Stopped Modeling','Modelling has been stopped for experiment','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (111,47,'Completed Modeling','Modeling of experiment * has been completed successfully','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (112,48,'Completed Modeling','Modeling of experiment * has been completed with an error','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (113,49,'Started Scale And Split','Scaling and Spliting of * has been started','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (114,50,'Completed Scale And Split','Scaling and Spliting of * has been completed','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (115,51,'Cleanup Started','Cleanup started for dataset * of project &','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (116,52,'Cleanup Ended','Cleanup ended for dataset * of project &','US','Operation',0,-1,0,0);




