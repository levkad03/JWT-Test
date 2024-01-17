from flask import Flask, jsonify
from extensions import db, jwt
from auth import auth_bp
from users import user_bp
from models import User

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_ECHO'] = True
app.config['FLASK_JWT_SECRET_KEY'] = 'f8e8888797be153d6dff2abf'

# initialize extensions
db.init_app(app)
jwt.init_app(app)

# register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')

# jwt error handlers
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify({
        'message': 'The token has expired.',
        'error': 'token_expired'
    }), 401

    
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'message': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401
    

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'message': 'Request does not contain an access token.',
        'error': 'authorization_header'
    }), 401


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(username=identity).one_or_none()


@jwt.additional_claims_loader
def make_additional_claims(identity):
    if identity == "user56":
        return {'is_admin': True}
    return {'is_admin': False}

if __name__ == '__main__':
    app.run(debug=True)