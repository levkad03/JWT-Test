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

App uses **Docker**

to run the db type 
```
docker compose -f docker-compose.yaml up -d
```

Create the database by running
```
flask db init
flask db migrate
flask db upgrade
```

Run the application with ``flask run``
