# project


``` python
print("Hello World")
```
TEST!
## Setting up a virtual environment
- why do i need a VE?\
Ensure all packages are the same versions - makes it standardised
``` bash
virtualenv venv  
```
Run the above command in the bash terminal - if things don't work, use python3/ python3 -m/ python3 -m pip.

## Activating the virtual environment
- How to enter the virtual environment:

```bash
source venv/bin/activate
```
This command allows for the virtual environment to be accessed through the terminal.

## Exiting the virtual environment

``` bash
deactivate
```
Virtual environment is deactivated - add to terminal


## installing django
Here's the command to install Django: 
``` bash 
pip3 install django 
```
MAKE SURE YOU'RE IN THE VIRTUAL ENVIRONMENT!!

``` bash
python -m django --version

```
This checks what version we are accessing for django to make sure we're in the right one.\

## requirements
- What is the point of requirements?\
Requirements are a list of packages and their corresponding versions.
- Why do we need requirements?\
Having a requirements file means that the people who have installed/downloaded the code know what packages to install within the environment.

Stating the command:

```bash 
pip3 freeze > requirements.txt
```
will allow for a new requirements.txt file to open up and this contains the three packages that are in use as well as their versions.\
You should also use this command when you are installing new packages - ensures the requirements file is kept up-to-date. 

This is what is included in the text file:

```bash
asgiref==3.7.2
Django==4.2.7
sqlparse==0.4.4
```
## creating venv from requirements

``` bash
virtualenv venv
source venv/bin/activate
```
As above, line 1 of code creates a virtual environment named venv.
Line 2 activates the virtual environment and allows you to enter it

``` bash
pip3 install -r src/requirements.txt 
```
This command allows you to install the packages within the requirements file into your virtual environment\
-r = read file

## Git

version control system - allows you to access your VE from mulitple devices, also keeps track of different versions of code, update different versions

``` bash
git commit
git pull
git push

```
Git commit - sets changes up to be sent to github\
Git pull - takes version from git, checks for any changes made\
Git push - launches the version onto git\

## The Development Server

cd - a term that allows you to change directories 

``` bash
python3 manage.py runserver
```
This command allows for me to run the server and check if it works - performs system checks and identifies any issues

If you have unapplied migrations it wants you to run:

```bash
python3 manage.py migrate
```
This will apply all the migrations to successfully allow the app to run.

``` bash
cd ..
```
Takes you out of the current directory and goes one above
- manage.py is only in the mysite directory - can only be accessed 

``` bash
python manage.py runserver
```

use this constantly to ensure your website is working!!\
make sure you're in the right directory - cd to vegify each time!\

