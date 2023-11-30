# My-Pass
A password managing web application made with Flask


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

#### Installation and Launching

After Downlaoding / Cloning this repo, run the following code in the root directory to install the required libraries and start up the application;

```
# install dependencies
$ pip install -r requirements.txt

# run the application
$ python app.py
```

Set up model on DB
```
$ python
>>> from project_folder import create_app
>>> app = create_app()
>>> app.app_context().push()
>>> from project_folder import db
>>> db.create_all()
```
