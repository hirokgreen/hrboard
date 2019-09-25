# HR Board
HR Solution
---

Django 2.0 Project


# Basic Instructions

* fork from https://github.com/hirokgreen/hrboard and then
* clone your copy
* `cd hrboard`

* create virtualenv with python3 using virtualenvwrapper or virtualenv 
(follow https://virtualenvwrapper.readthedocs.io/en/latest/)

with virtualenvwrapper - 

* `mkvirtualenv -p python3 hrboard` (next time only activate env by typing `workon hrboard`)


* Install all the **requirements** using `pip install -r requirements.txt`
* Complete the migrations. `python manage.py migrate`
* Start the server. `python manage.py runserver`
* The server should be up and running :smile:

# Endpoints

* admin: `/admin`
* employee Sign In: `/api-auth/login/`
* Board: `/`

