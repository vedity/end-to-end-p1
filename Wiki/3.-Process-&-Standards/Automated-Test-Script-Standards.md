###   **UnitTest** :
    
Unit Testing is the first level of software testing where the smallest testable parts of a software are tested. This is used to validate that each unit of the software performs as designed.

-  Unittest classes will be excuted in alphabatic order of class name. So here we have to define class name in which order we want to perforn unittest.

-  In each class or method the name should contain keyword "test".

-  "unittest" is the library which is been provided by the python itself for unit testing.

- We have to inherit default class unittest.TestCase in user defined class. and to do so import unittest

```bash
import unittest

 class TestAIngestPostDatasetClass(unittest.TestCase):
        def testA_scenario1_insert_dataset(self):

 class TestBIngestPostDatasetClass(unittest.TestCase):
         def testA_scenario1_insert_invalidfile(self):

```

- Unittest functions will be excuted in alphabatic order of function name.So here we have to define function in which order we want to perforn unittest.
###   **Example** :
```bash
 def testA_scenario1_insert_dataset(self):

 def testB_scenario2_insert_invalidfile(self):

```

- We have to pass url as argument for which we want to perform unittest and for that import requests library.

```bash
import requests

 def testA_scenario1_insert_dataset(self):
       response = requests.get("http://localhost:8000/create_dataset/")

```

- we will get response from given url and then we have to convert it in json and for that import json library.

```bash
import requests
import json
 def testA_scenario1_insert_dataset(self):
       response = requests.get("http://localhost:8000/create_dataset/")
       json_response = response.json()

```
- Then we will compare returned status code to check whether our testcase is correct or not

- assertEqual will be used to compare url response status with given argument.

```bash
import requests
import json
 def testA_scenario1_insert_dataset(self):
       response = requests.get("http://localhost:8000/create_dataset/")
       json_response = response.json()
       status = json_response["status_code"]
       self.assertEqual(status,"200")


```
- command to run test case is:

```bash

python -m unittest file_name

Example:  python -m unittest ingest_test

```

When we run from the command line, the above script produces an output that looks like this:
```bash
----------------------------------------------------------------------
Ran 3 tests in 0.000s
OK

```

- If ant testcase is failed then it will give output as follow:

```bash

----------------------------------------------------------------------
Ran 1 test in 0.001s
FAILED (failures=1)

```