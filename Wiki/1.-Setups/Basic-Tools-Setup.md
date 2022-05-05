## **Scope**
#### Scope of this document is to provide guideline for end-to-end pipeline to let developer use:
- #### Docker Desktop
- #### Git for source control
- #### Visual Code IDE for development
- #### GitLab for CI/CD

## **Docker Desktop**
### **1. **Install Docker**:**
- #### Use Docker Installation Link -> https://docs.docker.com/get-docker/

### **2. Docker Desktop Installation Steps on Windows**
- #### Double-click Docker Desktop Installer.exe to run the installer.
#### If you haven’t already downloaded the installer (Docker Desktop Installer.exe), you can get it from Docker Hub. It typically downloads to your Downloads folder, or you can run it from the recent downloads bar at the bottom of your web browser.
- #### When prompted, ensure the Enable Hyper-V Windows Features option is selected on the Configuration page.
- #### Follow the instructions on the installation wizard to authorize the installer and proceed with the install.
- #### When the installation is successful, click Close to complete the installation process.
- #### If your admin account is different to your user account, you must add the user to the docker-users group. Run Computer Management as an administrator and navigate to  Local Users and Groups > Groups > docker-users. Right-click to add the user to the group. Log out and log back in for the changes to take effect.

### **3. How To Start Docker Desktop:**
- ####  Docker Desktop does not start automatically after installation. To start Docker Desktop, search for Docker, and select Docker Desktop in the search results.

![image](uploads/5e8336cb22c173c481b9727c7cab8823/image.png)
 
#### When the whale icon in the status bar stays steady, Docker Desktop is up-and-running, and is accessible from any terminal window.

![image](uploads/1a044d89ecf7fba282d4fff3f3bd0b4a/image.png)
 
#### If the whale icon is hidden in the Notifications area, click the up arrow on the taskbar to show it. To learn more, see Docker Settings.

## **Download & Install Git**

- #### Git Installation  Link: https://git-scm.com/downloads
- #### Press the Download button to install the .exe file

![image](uploads/92c7320bbeeff4b2d0f33baaf5d9c49a/image.png)


### **Setup**
- #### Run the installer.
- #### Keep everything on default and click next until you see this page.
- #### Tick mark Enable experimental support for pseudo consoles.
- #### Click install to start the installation.

![image](uploads/0695aa4c9ed42a722ade6dce7fe3ba25/image.png)

### **Open Git Bash**

- #### On your desktop, Right click and select “**Git Bash Here**”

![image](uploads/35fc0ba234dfdba40300f4089a7b5518/image.png)

- #### To Validate successful installation Type “**git --version**”, You should see some output like this

![image](uploads/b585b4be821aedde459fcbbf30b731ef/image.png)

### **Initializing Git (One Time Setup)**
#### After the successful installation, you must initialize the git by providing your name & email so
that Gitlab or any other remote version controlling system knows who you are.

- #### To provide your name write: **git config –global user.name “Your Name”**

![image](uploads/d0e30d2d2db4b2f515d92a3632264779/image.png)

- #### To provide your email address write: **git config –global user.email xyz@a.com**

![image](uploads/8ec0aef24ccfc362e7e997e55c96c6c9/image.png)


#### NOTE: Make sure your email is authorized to make commits to IsgGroup group. If you
have any “you are not authorized to push commits to this repository” conflicts, then
ask Bhavin Mehta to authorize your email.


## **Download & Install VS Code**

- #### Visual Studio Code Installation Link: https://code.visualstudio.com/

### **Install below Extension in VS code for GitLab and VS code Integration**

- #### GitLab Workflow
- #### GitLab VS Code Extension
- #### GitLens — Git supercharged

![image](uploads/edf6659159878c5b403408903a9d8b65/image.png)


## **Steps to clone the project in our system**

### **Step 1: Create New Directory**

- #### Create Directory to store all git repositories. I have created GIT Repository named folder.

![image](uploads/2b61e9040bbedbc661bfde10900785b9/image.png)

### **Step 2:  Cloning a Repository**

- #### Login in GitLab. GitLab Link: https://gitlab.com/
- #### Go to Repository which we want to clone.
- #### Press the clone button and then copy the https link.

![image](uploads/c3a40b60016a0583d5c66f444a6f3ef7/image.png)

### **Step 3:  Cloning a Repository in Our System**

- #### Open VS code
- #### Click on Clone Repository 

![image](uploads/022c50020dda49fa5aebdeb9dc624fca/image.png)

- #### Paste https link which we have copied while Cloning and Press Enter


![image](uploads/d749f8742da5e7690d58153145b2a7e0/image.png)


- #### Select Repository Location, we have created earlier to store GIT Repository(eg.GIT Repository)



![image](uploads/68afa1f094cef8e04f13d312aa188866/image.png)


- #### GIT Repositories is stored into the selected Repository Location(eg.GIT Repository) 
- #### In VS code, Open the folder (e.g.end-to-end-p1) which we have cloned in selected Repository Location(eg.GIT Repository) 

![image](uploads/0aec0c032117ca3ac7b105f7a4cfdc6d/image.png)

- #### Now VS code folder structure look like this:

![image](uploads/a8a19255fa623584d27f4987dee9c514/image.png)




## **Run Code**

- #### To Run the code, Make sure your docker-desktop is running(refer.. How To Start Docker Desktop in Docker Desktop Topic) 
- #### right click on docker-compose.yml. and select compose-up

![image](uploads/3559935835ba8fdc85673347005c80f2/image.png)

#### After successfully container running: 
- #### Click on Docker Extension in VS code
- #### Expand the Container(eg.end-to-end-p1)
- #### right click on Image(which we wanted to Run e.g end-to-end-p1_angular_1) and select **Open in Browser**


![image](uploads/9742d82a288a9b830bfe7c88d45ff8be/image.png)

## **Stop Code**

- #### right click on docker-compose.yml.and select compose-down

![image](uploads/bc9f003d11898eba0db5233b9c89a3a4/image.png)