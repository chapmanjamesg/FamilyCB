# FamilyCB Backend Capstone

## Steps to get This project started:

* Clone down the repo and `cd` into it

* Create your OSX virtual environment in Terminal:

  * `python -m venv FamilyCBEnv`
  * `source ./FamilyCBEnv/bin/activate`

* Or create your Windows virtual environment in Command Line:

  * `python -m venv FamilyCBEnv`
  * `source ./FamilyCBEnv/Scripts/activate`

* Install the app's dependencies:

  * `pip install -r requirements.txt`
  * `pip install django-safedelete`

* Build your database from the existing models:

  * `python manage.py makemigrations`
  * `python manage.py migrate`

* Create a superuser for your local version of the app:

  * `python manage.py createsuperuser`
* If you get this message `Superuser creation skipped due to not running in a TTY. You can run `manage.py createsuperuser` in your project to create one manually.`

  *`winpty python manage.py createsuperuser`

* Populate your database with initial data from fixtures files: (_NOTE: every time you run this it will remove existing data and repopulate it) 

  * `python manage.py loaddata recipe`
  * `python manage.py loaddata comment`
  * `python manage.py loaddata ingredient`

* Fire up your dev server and get to work!

  * `python manage.py runserver`


## Official FamilyCB ERD

Our team of database developers and administrators developed this ERD for you to reference when creating your models.

https://dbdiagram.io/d/5e663ebd4495b02c3b87fd7f

Not that the column names do not conform to the Python community standards (PEP) for naming conventions. Make sure your models use snake case.


