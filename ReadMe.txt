I've developed this project on a windows machine. So, may be if you are on a mac, processes will be a bit different. Since I have only windows, so I'm describing processes to run the project
for a windows machine.

Firstly, some softwares needs to be pre-installed on the system.
They are: 
1. Postgresql with pgadmin4 (We can use any database, but to run this project prostgresql is needed since I've mentioned it in the project settings file,
and pgadmin is the interface to look into the database manually). Keep the username 'postgres' & the password '1234' as mentioned in the project settings file. 
You can use other username and password, but then you'll have to change it in the project settings file also.
2. Virtualenv

Now the running processes step by step:

Step-1//
In the terminal go to the location you want the project to reside with cd command.For example,
'E:', then 'E:\my\directory'

Step-2//
In this step, we will create a virtual environment for the dependencies of our project so that, they don't interfere or create a problem for other softwares installed on the system.
With this command 'virtualenv myEnv'
This command will create a virtual environment for us in a folder named myEnv and auto install some packages there. 
Now we need to activate the environment. With this command 'myEnv\Scripts\activate'
after activating, we enter the environment folder with this command 'cd myEnv'

Step-3//
Now, please copy the 'requirements.txt' file from the zipped file I've sent and paste it inside the myEnv folder. This .txt file has a list of packages and dependencies that are needed specifically
for this projet.
now we, install it with this command 'pip install -r requirements.txt'
pip is a package manager installed while creating the environment. This package manager will recursively install each dependencies for the project from the .txt file.

Step-4//
Now, please copy the project from the zip file I've sent named 'family_project' and paste it into the myEnv folder.
enter the project folder with this command 'cd family_project'

Step-5//
At this stage we are almost good to go. We've already set fundamentals for running this project. We just have to setup the database now. 
please open the pgadmin4 from your system. It opened in a tab in the browser. Complete necessary authentication with your password. Create a new database named 'FamilyDB'.
Now run the following commands serially:
'python manage.py migrate'
'python manage.py sqlmigrate 0001'
'python manage.py makemigrations'
'python manage.py migrate'

Step-6:
We are now ready to run the project. To run the project, run the following command:
'python manage.py runserver'








