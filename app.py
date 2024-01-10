from flask import Flask
from extensions import db
from auth import auth_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')


if __name__ == '__main__':
    app.run(debug=True)