## JWT-Test

This is a test api for user authentication using JWT-tokens
The app is built with <b>Python</b> and <b>Flask</b> framework

To get started, setup the virtual environment
```
python -m venv venv 
```

After that, activate it

```
venv/Scripts/activate
```

Install the libraries

```
pip install -r requirements.txt
```
Create the database by running
```
flask shell
```

In the interactive shell run the following
```
Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
App: app
Instance: D:\Python labs\JWT-Test\instance
>>> from models import User
>>> db.create_all()
```

Run the application with ``flask run``
