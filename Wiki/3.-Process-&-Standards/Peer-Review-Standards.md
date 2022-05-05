<hr>

[[_TOC_]]

### About this Document:

We have to create a **Merge Request** every time we want to **Merge** the code into any of the **Protected branches**(Development, Master, Uat). Whenever a Merge Request is created, a **Peer Review** is carried out to find **possible vulnerabilities** before merging the code.

The main aim of this document is to **describe** the **rules** you should be following while conducting the **Peer Review**. 

## Rules for the Peer Review

The below table shows the things you should be looking for while conducting a **Peer Review**,

| Rule | Explanation |
| ------ | ------ |
| **Commenting** | The code should be _properly commented_ in a way that it is **easily understandable** for the other programmers. |
| **Check Tables,Columns, Data Type, Size of Column** | Check proper utilization of column data type, size and also check table is necessary or not in case of SQL DB |
| **Merge Request Description** | The Merge Request should have a **proper description** explaining _**' What these changes are doing? '**_ & _**' Why are you making the changes? '**_.| 
| **Changes** | Look into the **Changes section** of the Merge Request and check if the Merge Request is _**changing**_ or _**deleting**_ any code that it's not supposed to do. |
| **Possible Errors** | Try to look for any possible **Errors** while looking at the code, this will save a good amount of **debugging time** later. |