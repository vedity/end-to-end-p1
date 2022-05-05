> **Note: Make sure you have done the [Testing Setup](https://gitlab.com/isgtest/end-to-end-p1/-/wikis/Setups/Testing-Setup-(Using-Docker-compose-file)) before downloading the production images.** 

# How To get the Production Website running in your Machine

### 1) Download this file anywhere on your machine:

(right-click the below file & select the "**save link as**" option, make sure you keep the filename as **docker-compose.yml**)

[docker-compose.yml](uploads/6ad46fc8a180c162980e5bf1ec550ad3/docker-compose.yml)

### 2) Open your terminal & go to the directory where this file is stored

```bash
cd Path/to/the/Directory
```

### 3) Compose up the file

You will need to perform the _**compose up**_ to build the _containers_ in your machine. Write the following _command_ in the **terminal**:

```batch
docker volume prune -f && docker-compose down && docker-compose pull && docker-compose up
```

Wait _(~5 mins)_ till the **containers** get built **automatically** & that's it! Now the **containers** are running in your localhost. So now you can proceed with the tests.

# Testing the Images

Wait for at least ~5 minutes after the containers are built, before going to the below URL,

Go to the below URL,

**Angular Server** (Website): [Click Here](http://localhost:4200/account/login?returnUrl=%2Fproject)

Login Credentials:

| Username| Password|
| ------ | ------ |
| raj| raj|
| mehul| mehul|
| swati| swati|
| bhavin| bhavin|
| vipul| vipul|
| riddhi| riddhi|
| jay| jay|
| abhishek| abhishek|
| shivani| shivani|
| mansi| mansi|
| shivani| shivani|
| nisha| nisha|