### **TABLE OF CONTENT**
- ##### **OVERVIEW**
- ##### **BASIC BUSINESS NEEDS**
- ##### **HEADER COMMENT**
- ##### **PYTHON CODE**
- ##### **PYTHON IMPORTANT NOTES**
- ##### **SQL CODE**
- ##### **DJANGO REST API**


## Overview
Objective of this document is to provide you with a set of coding standards and development guidelines for Development and Customization.

## Basic Business Needs
Development guidelines address the following requirements:

- ##### CODE USING OOPS CONCEPT
  You should be able to do code using oops concept from all development languages, including Python etc.

- ##### EXCEPTION HANDLING
  You should be able to handle results and exceptions in a consistent and flexible manner.

- ##### NOMENCLATURE
  You should use consistent naming standards.

- ##### ROBUST VALIDATION
  You should be able to fully validate all incoming information.

- ##### DOCUMENTATION
  You should be able to document available custom components and any modifications done to them in a standard way.

## Header Comment

The naming conventions start with Header Comment in each code:

HEADER COMMENT : MAINTAIN CHANGE HISTORY AND DATES

(E.G. 

/*CHANGE HISTORY

--CREATED BY--------CREATION DATE--------VERSION--------PURPOSE----------------------

 INFOSENSE          25-NOV-2020           1.0           Intial Version 
 INFOSENSE          28-NOV-2020        1.1           Modification for Business Rule ****************************************************************************************/

)

## Python Code

**Naming Standard** :- Function names, variable names, and filenames should be descriptive.

**module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.**

   | Type of element | Standard Adopted | Example |
   | --------------- | ---------------- | ------- |
   | Local/Global Variable| lower_with_under|  current_record|
   |Constant Variable | CAPS_WITH_UNDER	| TRAIN_SIZE |
   | Constant Path Variable | 	CAPS_WITH_UNDER | 	MASTER_PATH | 
   | Data Frame | 	lower_with_under<df> | 	scaled_df |
   | List Variable | 	lower_with_under<lst> | 	events_lst |
   | Class Name | 	CapWords | 	ScaleClass |
   | Object Declaration | 	CapWords | 	ScaleObject |
   | Method Declaration  | Public Method : lower_with_under() |  scaling_function() |   
   |                     | Private Method : lower_with_under() |  _scaling_function() | 
 | Parameters  | lower_with_under   | Input_df | 
 | Package Name |  lower_with_under | 	scaling_operation | 
 | Module Name |  lower_with_under  | 	scaling |   




####  **Class Declaration** :- 


Class name should be in CapWords and related to functionality.
Suppose if we are making class for scaling then name should be “ScaleClass”

**For example** :-


**Class** ScaleClass :

	----------------------------------------

	Method declaration 

	------------------------------------------


#### **Object Declaration** :-


Object name should be in CapWords and related to class name.

Suppose if our class name is “ScaleClass” then object name should be “ScaleObject”

**For Example** :- 

**Class** ScaleClass:

	----------------------------------

	Method declaration
	
	-----------------------------------

ScaleObject = ScaleClass()








#### **Method Declaration** :-

Method name  inside class should also be in lower_with_under() and related to class functionality.

Suppose we define method for std scaling then we define method as “std_scaling”

**For example** :-

**Class** ScaleClass :


	**def** std_scaling(self):

	-------------------------------------------
			Code here
	------------------------------------------

ScaleObject =ScaleClass()



#### **Parameters** :-

inside method’s function definition parameters name should be in lower_with_under and parameter name should be related to method’s functionality.

For example :-

**Class** ScaleClass :


	**def** std_scalling(self,input_df):

	-------------------------------------------
			Code here
	------------------------------------------

ScaleObject =ScaleClass()







#### **Package Name** :-

Package name should be in small case ( i.e. all letter should be in small case ) and then “-“(underscore) and then “any name related to packaging functionality”

Like :-  scaling_operation

**File Name** :-

Python script name should be in small case and also related to class functionality.

Like :- scaling.py



#### **Doc String** :- 

In every class’s method we have to write doc string (i.e. string about the function’s functionality)
In doc string we can write what the input parameter is and output parameter.
In doc string First word should be in CapWord and rest of the words in lower case.
E.g.

class ConversionClass(TypeConversionClass):

    def convert_values(self,input_df):

         """
        This function is used for selecting the original features.
        E.g.
        Original Features : "Name","Age","Salary"
        After Conversion Features : "Name","Age","Salary","Name_Str"
        It will take input parameter as a dataframe.
        And it will also return dataframe

        Input : DataFrame
        Output : DataFrame
        Dataframe : unscaled dataframe 
        """

        column_lst=df.dtypes.index.tolist()
        convert_df=super().convertValues(input_df)
        return_df=convert_df[column_lst]
        return return_df


## Python Important Notes

Magic class methods (not a complete list)

Magic methods (which begin and end with double
underscore) add functionality to your classes consistent
with the broader language.

| Magic method| What it does|
| ------------- | --------- |
| __init__(self,[...]) | Constructor |
| __del__(self) | Destructor pre-garbage collection |
| __str__(self) | Human readable string for class contents. Called by |
| __repr__(self)| Machine readable unambiguous Python string expression for class contents. Called by repr(self) Note: str(self) will call __repr__ if __str__ is not defined. |
| __eq__(self, other) |  Behaviour for ==|
| __ne__(self, other)  | Behaviour for !=|
| __lt__(self, other)  | Behaviour for <|
| __gt__(self, other) |Behaviour for >|
| __le__(self, other)| Behaviour for <=|
| __ge__(self, other) |Behaviour for >=|
| __add__(self, other)| Behaviour for +|
| __sub__(self, other)| Behaviour for -|
| __mul__(self, other)| Behaviour for *|
| __div__(self, other)| Behaviour for /|
| __mod__(self, other)| Behaviour for %|
| __pow__(self, other)| Behaviour for **|
| __pos__(self, other)| Behaviour for unary +|
| __neg__(self, other)| Behaviour for unary -|
| __hash__(self)| Returns an int when hash() called. Allows class instance to be put in a dictionary|
| __len__(self)| Length of container|
| __contains__(self, i)| Behaviour for in and not in operators|
| __missing__(self, i) |What to do when dict key i is missing|
| __copy__(self)| Shallow copy constructor|
| __deepcopy__(self,memodict={})| Deep copy constructor|
| __iter__(self)| Provide an iterator|
| __nonzero__(self)| Called by bool(self)|
| __index__(self)| Called by x[self]|
| __setattr__(self,name, val)| Called by self.name = val|
| __getattribute__(self,name)| Called by self.name|
| __getattr__(self,name)| Called when self.name does not exist|
| __delattr__(self,name)| Called by del self.name|
| __getitem__(self, key)| Called by self[key]|
| __setitem__(self, key,val)| Called by self[key] = val|
| __delitem__(self, key)| del self[key]|
      

You can refer more notes from below pdf link .

[Python_Notes.pdf](uploads/14b7fbc31729cceaddf4114d9e9dc282/Python_Notes.pdf)

## SQL Code

In addition to naming convention all database objects should be named without using any special characters. Use only ASCII characters, numbers and underscores but they should always start by a letter. The naming convention adopted for Database Objects are as follows:

| Object Type | Standard Adopted | Example|
| ----------- | ---------------- | ------ |
 | Table	      |         Table name is a description containing a one or two word explanation of the purpose. Prefix with mlaas. |mlaas_project_tbl|
 | View	       |        table_v Here table is the name of the root table the view is based on. The criteria is a qualifier of the objects shown by the view. Use the criteria qualifier if using table name alone is not unique. The view is based on a join of 2 or more tables. The view contains a WHERE clause. |mlaas_project_v|
 | External Table	 |      Table name is a description of a one or two word explanation of the purpose.Prefix with mlaas_ and Suffix with _ext |mlaas_project_ext|
 | Procedures  | 	         Is a description of a one or two word explanation of the purpose. Suffix with _prc | mlaas_dataset_to_db_prc| 
 | Functions |  	         Is a description of a one or two word explanation of the purpose.Suffix with _fun|  mlaas_dataset_to_db_fun| 
 | Trigger	  |             table_ti Here table is the name of the table on which the trigger is based and i is a unique ID starting with 1. | mlaas_project_t1 | 
 | Index	  |             Table_column_indx Suffix Table name and  column name with _indx |  mlaas_project_indx| 
 | Sequence | 	         Table_column_s Suffix Table name and column name _s|  mlaas_project _s| 
 | Synonyms | 	         Is the same as the table name or view name. | mlaas_project_tbl |




#### **FOR PROCEDURE/FUNCTION CODE**
**Key Notes**:
- Prefix "Schema Name" before any database object used in a Procedure/Function. 
- E.g. ingest. mlaas_dataset_to_db_prc, where ingest is the schema name.
- Scope prefix. Use, either l for local or g for global variable name.
- <root name> is the root name of the identifier, the part of the name that provides the description.


| Type of element | Standard Adopted | Example|
| --------------- | ---------------- | ------ |
| Variable declared in a Procedure block (anonymous, nested, subprogram)| 	l rootname | 	ltotal_sales  |         
| Constant declared in a Procedure block (anonymous, nested, subprogram)| 	c rootname	|     cmax_salary |
| Variable declared at the global level	                              |   g rootname	|     gtotal_sales |
| Constant declared at the global level	                              |   gc rootname | 	gcmax_salary |




#### **For Exception Handling** :


BEGIN TRY  
     { sql_statement | statement_block }  
END TRY  
BEGIN CATCH  
     [ { sql_statement | statement_block } ]  
END CATCH  
[ ; ]


**Example**:
  
BEGIN TRY  
    -- Generate divide-by-zero error.  
    SELECT 1/0;  
END TRY  
BEGIN CATCH  
    -- Execute error retrieval routine.  
    SELECT @lerror = Error_Message() 
END CATCH;   


#### ** FOR COLUMN NAME CONVENTIONS ** :

•	All field names should be snake-cased For example, project_id, project_name etc.
•	Boolean fields should be prefixed with is_, has_, or does_. For example, is_customer, has_unsubscribed, etc.
•	Date-only fields should be suffixed with _date. For example, report_date.
•	Date+time fields should be suffixed with _at. For example, created_at, posted_at, etc.

#### ** FOR COLUMN ORDER CONVENTIONS **:
Put the primary key first, followed by foreign keys, then by all other columns. If the table has any system columns (created_at, updated_at, is_deleted, etc.), put those last.



## DJANGO REST API
Create a directory in which you wish to maintain all your Django projects.
Go to terminal.Command for creating a project
```bash
django-admin startproject project_name
eg: django-admin startproject Mlaas
```
change the directory to your project you created:
```bash
cd project_name
eg: cd Mlaas
```
Command for creating an application under the project
```bash
python manage.py startapp app_name
eg: python manage.py startapp ingest
```
Running the django project.Use Command
```bash
python manage.py runserver
```
## HTTP methods
| Methods |Discription|
| --------------- | ---------------------- |
| GET | Provides a read only access to a resource |         
| POST | Used to create a new resource |
| DELETE |  Used to remove a resource |
| PUT  | Used to update a existing resource or create a new resource |

Open Views.py In your App which you created.
  Import following restframe work library

```bash
from rest_framework.views import APIView
from rest_framework.response import Response
```
Create class and inherit APIView init
```bash
class class_name(APIView):
eg: class CreateProjectClass(APIView):
```
create function of Http method you required within a class and that method will return Json Response
```bash
class class_name(APIView):
   def get(self,request):
        ..code..
       return Resposne()
   def post(self,request):
        ..code..
       return Resposne()
   def put(self,request):
        ..code..
       return Resposne()
   def delete(self,request):
        ..code..
       return Resposne()
```

Fetching any arguments within a method while calling that API class you can use request parameter
```bash
class class_name(APIView):
   def get(self,request):
        user_name = request.POST.get('user')
       return Resposne({"access username":user_name})
```
then go to urls.py file,import view.py init.
```bash
from app_name import views
eg : from ingest import views
```
add the url pattern and assign the class that you created in views.py ,as_view() method which treat the class as a view function.
```bash
urlpatterns = [
   path('mlaas/ingest/create_project/',CreateProjectClass.as_view()),
         
]
```
Finaly,you need to call that url pattern within a browser or some Testing Api software
```bash
http://127.0.0.1:8000/mlaas/ingest/create_project/
```