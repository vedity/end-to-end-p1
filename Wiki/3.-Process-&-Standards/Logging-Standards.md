| LOGGING LEVEL | DESCRIPTION |
| ------ | ------ |
| DEBUG | These are used to give Detailed information, typically of interest only when diagnosing problems. |
| INFO | These are used to Confirm that things are working as expected. |
| ERROR |  This tells that due to a more serious problem, the software has not been able to perform some function. |

### **Which log will be added and Where log will be added while coding**

### 1)  **INFO** :

Add in every function after the function definition end (i.e.“function execution start” ) and before  the function return statement (i.e. “function execution end” )

**Message Format** :- module_name  :   class_name  :  function_name  :  execution start

**Example** :- data ingestion : ingestclass : IngestClass : execution start
                  
               logging.info("data ingestion : ingestclass : word_count : execution start")

 ### 2) **DEBUG** :

In between function where actual logic is happing.

**Message Format** :- Small description about the logic and parameter. 

**Example** :- This file has %d words., “num_words"
                  
                logging.debug("data ingestion : ingestclass : word_count : this file has %d words. “,num_words")

### 3) **ERROR** :

In every except block.

**Message Format** :- "exception“

**Message Format** :- "traceback"
                  
              logging.error("data ingestion : ingestclass : word_count : exception : " + str(exception))

              logging.error("data ingestion : ingestclass : word_count : " + traceback.format_exc())

 

```bash

from my_logger import custom_logger as cl
import logging
import traceback

user_name = 'admin'
log_enable = True

LogObject = cl.LogClass(user_name,log_enable)
LogObject.log_setting()

logger = logging.getLogger('ingestion')

class IngestClass:
   
   def word_count(words):
		logging.info("data ingestion : IngestClass : word_count : execution start")
		try:
		    # count the number of words in a file and log the result
		    a = len(words)/0
		    num_words = len(words)
		    logging.debug("data ingestion : ingestclass : word_count : this file has %d words", num_words)
		    logging.info("data ingestion : IngestClass : word_count : execution start")
		    return num_words
 		except Exception as e:
		     logging.error("data ingestion : IngestClass : word_count : " + str(e))
		     logging.error("data ingestion : IngestClass : word_count : "+traceback.format_exc())
        
IngestObject = IngestClass()
print(IngestObject.word_count('my application'))

```