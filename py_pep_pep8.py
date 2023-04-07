#pip --version
#pip install numpy
#pip install package_name==version
#pip uninstall numpy : to uninstall package

#pip show numpy : Python pip show command to display the details of a particular package
#pip list : pip list command displays a list of packages installed in the system.
#pip search numpy : Search for a particular existing package.
#pip install -r requirements.txt : install package from requirement file
#pip freeze : pip freeze command is used to list packages that don’t come pre-installed with Python. 
#pip list –outdated :command is used to list all the packages that are outdated.
#pip install --user --upgrade package_name : used to update a package.

#REQUIREMENT FILE ##
###A requirement.txt python file is a type of file that usually stores information about all the libraries, modules, and packages which are specific to project that are used while developing a particular project.

#pip freeze > requirements.txt

#Pipenv is a packaging tool for Python that solves some common problems associated with the typical workflow using pip, virtualenv, and the good old requirements.txt.
#$ pip install pipenv
#pipenv install numpy

##PEP8 : PEP-8(Python Enhancement Proposal), is a document that provides guidelines and best practices on how to write Python code. The primary focus of PEP8 is to improve the readability and consistency of Python code.

###A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most Python developers use.
#$ pip install virtualenv
#Test your installation:

#$ virtualenv --version
#Using virtualenv

#You can create a virtualenv using the following command:
#$ virtualenv my_name

#To create a Python 2.7 virtual environment, use the following command:
#$ virtualenv -p /usr/bin/python2.7 virtualenv_name

#Activate:
#source virtualenv_name/bin/activate

#in windows
#$ cd <envname>
#$ Scripts\activate 

#Now you can install dependencies related to the project in this virtual environment. For example, if you are using Django 1.9 for a project, you can install it like you install other packages.

#virtualenv_name)$ pip install Django==1.9
#The Django 1.9 package will be placed in virtualenv_name folder and will be isolated from the complete system. Once you are done with the work, you can deactivate the virtual environment by the following command:

#(virtualenv_name)$ deactivate
