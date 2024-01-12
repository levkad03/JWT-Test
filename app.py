from flask import Flask
from extensions import db, jwt
from auth import auth_bp
from users import user_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_ECHO'] = True
app.config['FLASK_JWT_SECRET_KEY'] = 'f8e8888797be153d6dff2abf'

db.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')


if __name__ == '__main__':
    app.run(debug=True)