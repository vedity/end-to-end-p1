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
	model_class_name text,
	model_created_on TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Inserting Data into the model_master table.
insert into mlaas.model_master_tbl values (1,'Linear_Regression','Simple Linear Regression Model','Regression', 'Multi','Single_Target','LinearRegressionClass');
insert into mlaas.model_master_tbl values (2,'Ridge_Regression','Simple Ridge Regression Model','Regression','Multi','Single_Target','RidgeRegressionClass');
insert into mlaas.model_master_tbl values (3,'Lasso_Regression','Simple LASSO Regression Model','Regression','Multi','Single_Target','LassoRegressionClass');
insert into mlaas.model_master_tbl values (4,'ElasticNet_Regression','Simple ElasticNet Regression Model','Regression','Multi','Single_Target','ElasticNetClass');
insert into mlaas.model_master_tbl values (5,'KNeighbors_Regression','KNeighbours Regression Model','Regression','Multi','Single_Target', 'KNeighborsRegressionClass');
insert into mlaas.model_master_tbl values (6,'Decision_Tree_Regressor','Decision Tree Regression Model','Regression','Multi','Single_Target', 'DecisionTreeRegressionClass');
insert into mlaas.model_master_tbl values (7,'Random_Forest_Regressor','Decision Tree Regression Model','Regression','Multi','Single_Target', 'RandomForestRegressionClass');
insert into mlaas.model_master_tbl values (8,'XGBoost_Regression','Simple XGBoost Regression Model','Regression','Multi','Single_Target','XGBoostRegressionClass');
insert into mlaas.model_master_tbl values (9,'Gradient_Boosting_Machine_Regressor','Gradient Boosting Machine Regression Model','Regression','Multi','Single_Target', 'GradientBoostingRegressionClass');
-- insert into mlaas.model_master_tbl values (10,'Linear_Regression_Keras','Simple Regression Model Using Nueral Network','Regression', 'Multi', 'Single_Target','LinearRegressionKerasClass');

-------------------------------------------------------CLASSIFICATION---------------------------------------------------------

insert into mlaas.model_master_tbl values (11,'Logistic_Regression','Simple Logistic Regression Model','Classification','Binary','Single_Target','LogisticRegressionClass');
insert into mlaas.model_master_tbl values (12,'SVM_Classification','SVM Classifcation Model','Classification','Multi','Single_Target', 'SVMClassificationClass');
insert into mlaas.model_master_tbl values (13,'KNeighbors_Classification','KNeighbours Classifcation Model','Classification','Multi','Single_Target', 'KNeighborsClassificationClass');
insert into mlaas.model_master_tbl values (14,'Naive_Bayes_Classification','Simple Naive Bayes Classification Model','Classification','Binary','Single_Target','NaiveBayesClassificationClass');
insert into mlaas.model_master_tbl values (15,'Decision_Tree_Classifier','Decision Tree Classification Model','Classification','Multi','Single_Target', 'DecisionTreeClassificationClass');
insert into mlaas.model_master_tbl values (16,'Random_Forest_Classifier','Decision Tree Classification Model','Classification','Multi','Single_Target', 'RandomForestClassificationClass');
insert into mlaas.model_master_tbl values (17,'XGBoost_Classification','Simple XGBoost Classification Model','Classification','Multi','Single_Target','XGBoostClassificationClass');
insert into mlaas.model_master_tbl values (18,'Gradient_Boosting_Machine_Classifier','Gradient Boosting Classification Model','Classification','Multi','Single_Target', 'GradientBoostingClassificationClass');
-- insert into mlaas.model_master_tbl values (19,'Logistic_Regression_Keras','Simple Linear Classification Model Using Nueral Network','Classification', 'Binary', 'Single_Target','KerasLogisticRegressionClass');

CREATE TABLE mlaas.model_hyperparams_tbl
(
	model_id int4 NULL,
	param_name varchar NULL,
	param_value varchar NULL,
	display_type varchar NULL
);


insert into mlaas.model_hyperparams_tbl values (1, '', '[]', '');


insert into mlaas.model_hyperparams_tbl values (2, 'alpha', '[0.001, 1]', 'validation');
insert into mlaas.model_hyperparams_tbl values (2, 'solver', '["auto", "sparse_cg", "saga"]', 'dropdown');


insert into mlaas.model_hyperparams_tbl values (3, 'alpha', '[0.001, 1]', 'validation');
insert into mlaas.model_hyperparams_tbl values (3, 'selection', '["cyclic", "random"]', 'dropdown');


insert into mlaas.model_hyperparams_tbl values (4, 'alpha', '[0.001, 1]', 'validation');
insert into mlaas.model_hyperparams_tbl values (4, 'l1_ratio', '[0, 1]', 'validation');
insert into mlaas.model_hyperparams_tbl values (4, 'selection', '["cyclic", "random"]', 'dropdown');


insert into mlaas.model_hyperparams_tbl values (5, 'n_neighbors', '[2, 40]', 'validation');
insert into mlaas.model_hyperparams_tbl values (5, 'metric', '["euclidean", "manhattan", "minkowski"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (5, 'algorithm', '["auto", "ball_tree", "kd_tree"]', 'dropdown');


insert into mlaas.model_hyperparams_tbl values (6, 'criterion', '["mse", "friedman_mse", "mae", "poisson"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (6, 'max_depth', '[2, 30]', 'validation');
insert into mlaas.model_hyperparams_tbl values (6, 'max_features', '["auto", "sqrt", "log2"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (6, 'min_samples_leaf', '[1, 20]', 'validation');



insert into mlaas.model_hyperparams_tbl values (7, 'n_estimators', '[1, 2000]', 'validation');
insert into mlaas.model_hyperparams_tbl values (7, 'criterion', '["friedman_mse", "mse", "mae"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (7, 'max_depth', '[2, 30]', 'validation');
insert into mlaas.model_hyperparams_tbl values (7, 'max_features', '["auto", "sqrt", "log2"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (7, 'min_samples_leaf', '[1, 20]', 'validation');


insert into mlaas.model_hyperparams_tbl values (8, 'learning_rate', '[0.001, 1]', 'validation');
insert into mlaas.model_hyperparams_tbl values (8, 'n_estimators', '[1, 200]', 'validation');
insert into mlaas.model_hyperparams_tbl values (8, 'max_depth', '[3, 12]', 'validation');
insert into mlaas.model_hyperparams_tbl values (8, 'min_child_weight', '[1, 10]', 'validation');
insert into mlaas.model_hyperparams_tbl values (8, 'gamma', '[0, 1]', 'validation');
insert into mlaas.model_hyperparams_tbl values (8, 'reg_alpha', '[0, 1]', 'validation');
insert into mlaas.model_hyperparams_tbl values (8, 'reg_lambda', '[0, 1]', 'validation');


insert into mlaas.model_hyperparams_tbl values (9, 'loss', '["ls", "lad","quantile"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (9, 'learning_rate', '[0.001, 20]', 'validation');
insert into mlaas.model_hyperparams_tbl values (9, 'subsample', '[0.1, 1]', 'validation');
insert into mlaas.model_hyperparams_tbl values (9, 'n_estimators', '[1, 2000]', 'validation');
insert into mlaas.model_hyperparams_tbl values (9, 'criterion', '["mse", "friedman_mse", "mae"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (9, 'max_depth', '[2, 30]', 'validation');
insert into mlaas.model_hyperparams_tbl values (9, 'max_features', '["auto", "sqrt", "log2"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (9, 'min_samples_leaf', '[1, 20]', 'validation');


-- insert into mlaas.model_hyperparams_tbl values (10, 'epochs', '[]', '');
-- insert into mlaas.model_hyperparams_tbl values (10, 'learning_rate', '[0.001, 1]', 'validation');
-- insert into mlaas.model_hyperparams_tbl values (10, 'batch_size', '[8, 16, 32, 64, 128, 256]', 'dropdown');
-- insert into mlaas.model_hyperparams_tbl values (10, 'loss', '["Mean_Absolute_Error", "Mean_Squared_Error", "Mean_Absolute_Percentage_Error"]', 'dropdown');
-- insert into mlaas.model_hyperparams_tbl values (10, 'optimizer', '["SGD", "RMSProp", "Adam"]', 'dropdown');

------------------------------------------CLASSIFICATION--------------------------------------------------

insert into mlaas.model_hyperparams_tbl values (11, 'C', '[0.001, 10]', 'validation');
insert into mlaas.model_hyperparams_tbl values (11, 'penalty', '["l1", "l2", "elasticnet"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (11, 'solver', '["auto", "lbfgs", "saga"]', 'dropdown');


insert into mlaas.model_hyperparams_tbl values (12, 'C', '[0, 100]', 'validation');
insert into mlaas.model_hyperparams_tbl values (12, 'gamma', '[0, 100]', 'validation');
insert into mlaas.model_hyperparams_tbl values (12, 'kernel', '["linear", "poly", "rbf", "sigmoid"]', 'dropdown');


insert into mlaas.model_hyperparams_tbl values (13, 'n_neighbors', '[2, 40]', 'validation');
insert into mlaas.model_hyperparams_tbl values (13, 'metric', '["euclidean", "manhattan", "minkowski"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (13, 'algorithm', '["auto", "ball_tree", "kd_tree"]', 'dropdown');



insert into mlaas.model_hyperparams_tbl values (14, '', '[]', '');



insert into mlaas.model_hyperparams_tbl values (15, 'criterion', '["gini", "entropy"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (15, 'max_depth', '[2, 30]', 'validation');
insert into mlaas.model_hyperparams_tbl values (15, 'max_features', '["auto", "sqrt", "log2"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (15, 'min_samples_leaf', '[1, 20]', 'validation');


insert into mlaas.model_hyperparams_tbl values (16, 'n_estimators', '[1, 2000]', 'validation');
insert into mlaas.model_hyperparams_tbl values (16, 'criterion', '["gini", "entropy"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (16, 'max_depth', '[2, 30]', 'validation');
insert into mlaas.model_hyperparams_tbl values (16, 'max_features', '["auto", "sqrt", "log2"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (16, 'min_samples_leaf', '[1, 20]', 'validation');


insert into mlaas.model_hyperparams_tbl values (17, 'learning_rate', '[0.001, 1]', 'validation');
insert into mlaas.model_hyperparams_tbl values (17, 'n_estimators', '[1, 200]', 'validation');
insert into mlaas.model_hyperparams_tbl values (17, 'max_depth', '[3,12]', 'validation');
insert into mlaas.model_hyperparams_tbl values (17, 'min_child_weight', '[1,10]', 'validation');
insert into mlaas.model_hyperparams_tbl values (17, 'gamma', '[0,1]', 'validation');
insert into mlaas.model_hyperparams_tbl values (17, 'reg_alpha', '[0,1]', 'validation');
insert into mlaas.model_hyperparams_tbl values (17, 'reg_lambda', '[0,1]', 'validation');



insert into mlaas.model_hyperparams_tbl values (18, 'loss', '["deviance", "exponential"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (18, 'learning_rate', '[0.001, 20]', 'validation');
insert into mlaas.model_hyperparams_tbl values (18, 'subsample', '[0.1, 1]', 'validation');
insert into mlaas.model_hyperparams_tbl values (18, 'n_estimators', '[1, 2000]', 'validation');
insert into mlaas.model_hyperparams_tbl values (18, 'criterion', '["mse", "friedman_mse", "mae"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (18, 'max_depth', '[2, 30]', 'validation');
insert into mlaas.model_hyperparams_tbl values (18, 'max_features', '["auto", "sqrt", "log2"]', 'dropdown');
insert into mlaas.model_hyperparams_tbl values (18, 'min_samples_leaf', '[1, 20]', 'validation');



-- insert into mlaas.model_hyperparams_tbl values (19, 'epochs', '[]', '');
-- insert into mlaas.model_hyperparams_tbl values (19, 'learning_rate', '[0.001, 1]', 'validation');
-- insert into mlaas.model_hyperparams_tbl values (19, 'batch_size', '[8, 16, 32, 64, 128, 256]', 'dropdown');
-- insert into mlaas.model_hyperparams_tbl values (19, 'loss', '["binary_crossentropy","categorical_crossentropy"]', 'dropdown');
-- insert into mlaas.model_hyperparams_tbl values (19, 'optimizer', '["SGD", "RMSProp", "Adam"]', 'dropdown');



create table mlaas.auto_model_params
 (
	model_id int4, 
	version_name varchar,
	hyperparam varchar
  );



insert into mlaas.auto_model_params values (1, 'Initial Version for Simple Linear Regressor', '{}');
insert into mlaas.auto_model_params values (2, 'Initial Version for Ridge Regressor', '{"alpha": 1, "solver": "auto"}');
insert into mlaas.auto_model_params values (3, 'Initial Version for Lasso Regressor', '{"alpha": 1, "selection": "cyclic"}');
insert into mlaas.auto_model_params values (4, 'Initial Version for Elasticnet Regressor', '{"alpha": 1, "l1_ratio": 0.5, "selection": "cyclic"}');
insert into mlaas.auto_model_params values (5, 'Initial Version for KNeighbor Regressor', '{"n_neighbors": 11, "metric": "minkowski", "algorithm": "auto"}');
insert into mlaas.auto_model_params values (6, 'Initial Version of DecisionTree Regression', '{"criterion": "mse", "max_depth": "None", "max_features": "auto", "min_samples_leaf": 1}');
insert into mlaas.auto_model_params values (7, 'Initial Version of RandomForest Regression', '{"n_estimators": 100, "criterion": "mse", "max_depth": "None", "max_features": "auto", "min_samples_leaf": 1}');
insert into mlaas.auto_model_params values (8, 'Initial Version for XGBoost Regressor', '{"n_estimators":100,"max_depth":6,"min_child_weight":1,"learning_rate":0.3,"gamma":0,"reg_alpha":0,"reg_lambda":1}');
insert into mlaas.auto_model_params values (9, 'Initial Version of Gradient Boosting Regression', '{"loss": "ls", "learning_rate":0.1, "subsample":1, "n_estimators": 100, "criterion": "friedman_mse", "max_depth": "None", "max_features": "auto", "min_samples_leaf": 1}');
-- insert into mlaas.auto_model_params values (10, 'With 3 Layer', '{"loss": "Mean_Squared_Error", "optimizer": "adam", "learning_rate": 0.01, "batch_size": 16, "epochs": 10}');


-----------------------------------------------------CLASSIFCATION-------------------------------------------------------
insert into mlaas.auto_model_params values (11, 'Initial Version for Logistic Regressor', '{"C": 1, "penalty": "l2", "solver": "lbfgs"}');
insert into mlaas.auto_model_params values (12, 'Initial Version for SVM Classifier', '{"C": 2, "gamma": "scale", "kernel": "rbf"}');
insert into mlaas.auto_model_params values (13, 'Initial Version for KNeighbor Classifier', '{"n_neighbors": 11, "metric": "minkowski", "algorithm": "auto"}');
insert into mlaas.auto_model_params values (14, 'Initial Version for Simple Naive Bais Classifier', '{}');
insert into mlaas.auto_model_params values (15, 'Initial Version of DecisionTree Classification', '{"criterion": "gini", "max_depth": "None", "max_features": "auto", "min_samples_leaf": 1}');
insert into mlaas.auto_model_params values (16, 'Initial Version of RandomForest Classification', '{"n_estimators": 100, "criterion": "gini", "max_depth": "None", "max_features": "auto", "min_samples_leaf": 1}');
insert into mlaas.auto_model_params values (17, 'Initial Version for XGBoost Regressor', '{"n_estimators":100,"max_depth":6,"min_child_weight":1,"learning_rate":0.3,"gamma":0,"reg_alpha":0,"reg_lambda":1}');
insert into mlaas.auto_model_params values (18, 'Initial Version of Gradient Boosting Classification', '{"loss": "deviance", "learning_rate":0.1, "subsample":1, "n_estimators": 100, "criterion": "friedman_mse", "max_depth": "None", "max_features": "auto", "min_samples_leaf": 1}');
-- insert into mlaas.auto_model_params values (19, 'binary version', '{"loss": "binary_crossentropy", "optimizer": "adam", "learning_rate": 0.01, "batch_size": 16, "epochs": 10}');



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
	dag_state varchar,
	dag_created_on TIMESTAMPTZ NOT NULL DEFAULT NOW()
);


create sequence unq_num_seq
increment 1;

SELECT setval('unq_num_seq', 1);

CREATE TABLE mlaas.activity_master_tbl (
	"index" serial NOT NULL,
	activity_id text NULL,
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
	noise_flag text NULL,
	"date_format" text NULL
);

--Create activity_deatil table
CREATE TABLE mlaas.activity_detail_tbl (
    "index" bigserial NOT NULL,
    activity_id text NULL,
    user_name text NULL,
    project_id int8 NULL,
    dataset_id int8 NULL,
    activity_description text NULL,
    start_time timestamp NOT NULL DEFAULT now(),
    end_time timestamp NULL,
    column_id text NULL,
    "parameter" text NULL
);

CREATE TABLE mlaas.dag_management_tbl (
	"index" serial NOT NULL,
	dag_id text NOT NULL,
	allocated boolean NOT NULL DEFAULT false,
	dag_type_id int NOT NULL
);

CREATE TABLE mlaas.dag_type_tbl (
	dag_type_id int NOT NULL,
	dag_type text NOT NULL
);

--Create feature master table
CREATE TABLE mlaas.feature_master_tbl (
	id int8 NULL,
	feature_method text NULL,
	algo_target_type text NULL
);


--Create feature information table
create  table mlaas.feature_info_tbl(
"index" bigserial NOT NULL,
schema_id int8 NOT NULL,
feature_value text NOT NULL,
feature_selection_type text NULL
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

--Insert preprocess_tab_tbl
Insert into mlaas.preprocess_tab_tbl values(1,'Missing Value Handling');
Insert into mlaas.preprocess_tab_tbl values(2,'Transformation');



--Insert parent_activity_tbl
Insert into mlaas.parent_activity_tbl values(1,'Missing Value Handling',1);
Insert into mlaas.parent_activity_tbl values(2,'Noise Handling',1);
Insert into mlaas.parent_activity_tbl values(3,'Outlier Handling',2);
Insert into mlaas.parent_activity_tbl values(4,'Scaling',2);
Insert into mlaas.parent_activity_tbl values(5,'Encoding',2);
Insert into mlaas.parent_activity_tbl values(6,'Math Operations',2);
Insert into mlaas.parent_activity_tbl values(7,'Transformations',2);
Insert into mlaas.parent_activity_tbl values(8,'Feature Engineering',2);
Insert into mlaas.parent_activity_tbl values(9,'Duplicate Data Handling',1);


--Insert into feature master table
Insert into  mlaas.feature_master_tbl values (1,'Anova F-test','categorical');
Insert into  mlaas.feature_master_tbl values (2,'Chi Square','categorical');
Insert into  mlaas.feature_master_tbl values (3,'Coorelation','numerical');
Insert into  mlaas.feature_master_tbl values (4,'Mutual Information','categorical');
Insert into  mlaas.feature_master_tbl values (5,'Recursive Feature Elimination','categorical');

--Insert activity master
-- COLUMNS => "index", activity_id, activity_name, activity_description, "language", operation, code, parent_activity_id, user_input, check_typ
Insert into mlaas.activity_master_tbl values (DEFAULT,'in_2','Delete Dataset','You have deleted dataset','US','Delete',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'in_3','Create Project','You have created project','US','Create',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'in_1','Create Dataset','You have created dataset','US','Create',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'in_4','Delete Project','You have deleted project','US','Delete',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'sm_5','Column name updated','You have updated the name of Columns','US','Update',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'sm_6','Selected Target Column','You have selected Columns  *  of dataset $ as Target Columns','US','Select',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'sm_7','Ignored Column','You have ignored Columns *','US','Ignore',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'sm_8','Auto Feature Selection','Auto Feature Selection on project * started','US','Started',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'sm_9','Auto Feature Selection','Auto Feature Selection on project * ended','US','Ended',0,-1,0,0);

Insert into mlaas.activity_master_tbl values (DEFAULT,'in_8','Created new dataset','You have saved new dataset','US','Create',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_1','Discard Missing Values','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_1','Discard Missing Values','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_1','Discard Missing Values','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_11','Discard Noise','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_11','Discard Noise','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_11','Discard Noise','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_21','Delete Above','operation on column * failed','US','Operation',0,3,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_21','Delete Above','operation on column * in process','US','Operation',1,3,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_21','Delete Above','operation on column * completed','US','Operation',2,3,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_31','Delete Below','operation on column * failed','US','Operation',0,3,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_31','Delete Below','operation on column * in process','US','Operation',1,3,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_31','Delete Below','operation on column * completed','US','Operation',2,3,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_41','Remove Noise','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_41','Remove Noise','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_41','Remove Noise','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_51','Mean Imputation','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_51','Mean Imputation','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_51','Mean Imputation','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_61','Median Imputation','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_61','Median Imputation','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_61','Median Imputation','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_71','Mode Imputation','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_71','Mode Imputation','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_71','Mode Imputation','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_81','Arbitarry Value Imputation','operation on column * failed','US','Operation',0,1,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_81','Arbitarry Value Imputation','operation on column * in process','US','Operation',1,1,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_81','Arbitarry Value Imputation','operation on column * completed','US','Operation',2,1,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_91','End_or_Tail Imputation','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_91','End_or_Tail Imputation','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_91','End_or_Tail Imputation','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_101','Frequent Category Imputation','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_101','Frequent Category Imputation','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_101','Frequent Category Imputation','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_111','Add Missing Category','operation on column * failed','US','Operation',0,1,1,3);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_111','Add Missing Category','operation on column * in process','US','Operation',1,1,1,3);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_111','Add Missing Category','operation on column * completed','US','Operation',2,1,1,3);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_121','Random Sample Imputation','operation on column * failed','US','Operation',0,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_121','Random Sample Imputation','operation on column * in process','US','Operation',1,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_121','Random Sample Imputation','operation on column * completed','US','Operation',2,1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_131','Replace Noise with Mean','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_131','Replace Noise with Mean','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_131','Replace Noise with Mean','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_141','Replace Noise with Median','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_141','Replace Noise with Median','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_141','Replace Noise with Median','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_151','Replace Noise with Mode','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_151','Replace Noise with Mode','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_151','Replace Noise with Mode','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_161','Replace Noise with End_or_Tail Value','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_161','Replace Noise with End_or_Tail Value','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_161','Replace Noise with End_or_Tail Value','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_171','Replace Noise with Random Value','operation on column * failed','US','Operation',0,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_171','Replace Noise with Random Value','operation on column * in process','US','Operation',1,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_171','Replace Noise with Random Value','operation on column * completed','US','Operation',2,2,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_181','Replace Noise with Arbitry Value','operation on column * failed','US','Operation',0,2,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_181','Replace Noise with Arbitry Value','operation on column * in process','US','Operation',1,2,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_181','Replace Noise with Arbitry Value','operation on column * completed','US','Operation',2,2,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_191','Remove outliers using Extreme Value analysis','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_191','Remove outliers using Extreme Value analysis','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_191','Remove outliers using Extreme Value analysis','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_201','Remove outliers using Z-score Detection Method','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_201','Remove outliers using Z-score Detection Method','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_201','Remove outliers using Z-score Detection Method','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_202','Remove outliers using Local Factor Outlier Detection','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_202','Remove outliers using Local Factor Outlier Detection','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_202','Remove outliers using Local Factor Outlier Detection','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_211','Replace Outliers with Mean using Extreme Value Analysis Detection','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_211','Replace Outliers with Mean using Extreme Value Analysis Detection','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_211','Replace Outliers with Mean using Extreme Value Analysis Detection','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_221','Replace Outliers with Mean using Z-score Detection','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_221','Replace Outliers with Mean using Z-score Detection','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_221','Replace Outliers with Mean using Z-score Detection','operation on column * completed','US','Operation',2,3,0,0);




Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_231','Replace Outliers with Median using Extreme Value Analysis Detection','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_231','Replace Outliers with Median using Extreme Value Analysis Detection','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_231','Replace Outliers with Median using Extreme Value Analysis Detection','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_241','Replace Outliers with Median using Z-score Detection','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_241','Replace Outliers with Median using Z-score Detection','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_241','Replace Outliers with Median using Z-score Detection','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_242','Replace Outliers with Mean using Local Factor Outlier Detection','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_242','Replace Outliers with Mean using Local Factor Outlier Detection','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_242','Replace Outliers with Mean using Local Factor Outlier Detection','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_243','Replace Outliers with Median using Local Factor Outlier Detection','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_243','Replace Outliers with Median using Local Factor Outlier Detection','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_243','Replace Outliers with Median using Local Factor Outlier Detection','operation on column * completed','US','Operation',2,3,0,0);

Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_244','Replace Outliers using IQR Proximity Rule','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_244','Replace Outliers using IQR Proximity Rule','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_244','Replace Outliers using IQR Proximity Rule','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_245','Replace Outliers using Gussian Approximation','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_245','Replace Outliers using Gussian Approximation','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_245','Replace Outliers using Gussian Approximation','operation on column * completed','US','Operation',2,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_246','Replace Outliers using Interquartile Range','operation on column * failed','US','Operation',0,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_246','Replace Outliers using Interquartile Range','operation on column * in process','US','Operation',1,3,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_246','Replace Outliers using Interquartile Range','operation on column * completed','US','Operation',2,3,0,0);








Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_251','Logarithmic transformation','operation on column * failed','US','Operation',0,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_251','Logarithmic transformation','operation on column * in process','US','Operation',1,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_251','Logarithmic transformation','operation on column * completed','US','Operation',2,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_252','Square root transformation','operation on column * failed','US','Operation',0,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_252','Square root transformation','operation on column * in process','US','Operation',1,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_252','Square root transformation','operation on column * completed','US','Operation',2,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_253','Reciprocal transformation','operation on column * failed','US','Operation',0,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_253','Reciprocal transformation','operation on column * in process','US','Operation',1,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_253','Reciprocal transformation','operation on column * completed','US','Operation',2,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_254','Power transformation','operation on column * failed','US','Operation',0,7,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_254','Power transformation','operation on column * in process','US','Operation',1,7,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_254','Power transformation','operation on column * completed','US','Operation',2,7,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_255','Box-Cox Transformation','operation on column * failed','US','Operation',0,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_255','Box-Cox Transformation','operation on column * in process','US','Operation',1,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_255','Box-Cox Transformation','operation on column * completed','US','Operation',2,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_256','Yeo-Johnson Transformation','operation on column * failed','US','Operation',0,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_256','Yeo-Johnson Transformation','operation on column * in process','US','Operation',1,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_256','Yeo-Johnson Transformation','operation on column * completed','US','Operation',2,7,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_261','Label Encoding','operation on column * failed','US','Operation',0,5,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_261','Label Encoding','operation on column * in process','US','Operation',1,5,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_261','Label Encoding','operation on column * completed','US','Operation',2,5,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_271','One Hot Encoding','operation on column * failed','US','Operation',0,5,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_271','One Hot Encoding','operation on column * in process','US','Operation',1,5,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_271','One Hot Encoding','operation on column * completed','US','Operation',2,5,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_281','Add to Column','operation on column * failed','US','Operation',0,6,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_281','Add to Column','operation on column * in process','US','Operation',1,6,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_281','Add to Column','operation on column * completed','US','Operation',2,6,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_291','Subtract from Column','operation on column * failed','US','Operation',0,6,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_291','Subtract from Column','operation on column * in process','US','Operation',1,6,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_291','Subtract from Column','operation on column * completed','US','Operation',2,6,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_301','Divide from column','operation on column * failed','US','Operation',0,6,1,5);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_301','Divide from column','operation on column * in process','US','Operation',1,6,1,5);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_301','Divide from column','operation on column * completed','US','Operation',2,6,1,5);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_311','Multiply into column','operation on column * failed','US','Operation',0,6,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_311','Multiply into column','operation on column * in process','US','Operation',1,6,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_311','Multiply into column','operation on column * completed','US','Operation',2,6,1,2);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_321','Extract Datetime Features','operation on column * failed','US','Operation',0,8,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_321','Extract Datetime Features','operation on column * in process','US','Operation',1,8,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_321','Extract Datetime Features','operation on column * completed','US','Operation',2,8,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_331','Remove Duplicate Records','operation  failed','US','Operation',0,9,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_331','Remove Duplicate Records','operation  in process','US','Operation',1,9,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_331','Remove Duplicate Records','operation  completed','US','Operation',2,9,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_332','Remove Duplicate Columns','operation failed','US','Operation',0,9,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_332','Remove Duplicate Columns','operation  in process','US','Operation',1,9,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_332','Remove Duplicate Columns','operation  completed','US','Operation',2,9,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_333','Remove Low Variance column','operation  failed','US','Operation',0,9,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_333','Remove Low Variance column','operation  in process','US','Operation',1,9,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'dp_333','Remove Low Variance column','operation completed','US','Operation',2,9,0,0);

Insert into mlaas.activity_master_tbl values (DEFAULT,'md_41','Created Experiment','You have created experiment "#" for project "$"','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'md_42','Selected Auto Modeling','You have selected Auto Modeling for experiment "#" of project "$"','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'md_43','Selected Manual Modeling','You have selected Manual Modeling for experiment "#" of project "$"','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'md_44','Defined Modeling Parameters','You have selected the algorithm "*" and defined the parameters for experiment "#" of project "$"','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'md_45','Started Modeling','Modelling has been started for experiment "#" of project "$"','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'md_46','Stopped Modeling','Modelling has been stopped for experiment "#" of project "$"','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'md_47','Completed Modeling','Modeling of experiment "#" has been completed successfully','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'md_48','Completed Modeling','Modeling of experiment "#" has been completed with an error','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'ss_1','Started Scale And Split','Scaling and Spliting of * has been started','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'ss_2','Completed Scale And Split','Scaling and Spliting of * has been completed','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'cl_1','Cleanup Started','Cleanup started for dataset * of project &','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'cl_2','Cleanup Ended','Cleanup ended for dataset * of project &','US','Operation',0,-1,0,0);
Insert into mlaas.activity_master_tbl values (DEFAULT,'cl_3','Dataset Created','You have created New dataset *','US','Operation',0,-1,0,0);

----------------------- Inserting into mlaas.dag_type_tbl -----------------------
Insert into mlaas.dag_type_tbl values (1,'Cleanup Dag');
Insert into mlaas.dag_type_tbl values (2,'Manual Modelling Dag');
