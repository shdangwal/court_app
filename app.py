from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

from db import db
from ma import ma
from blacklist import BLACKLIST
from resources.transaction import (
    Transaction,
    TransactionList
)
from resources.student import (
    Student,
    StudentList
)
from resources.pending import PendingFees
from resources.user import (
    UserRegister,
    UserLogin,
    User,
    TokenRefresh,
    UserLogout
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["JWT_BLACKLIST_ENABLED"] = True  # enable blacklist feature
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = [
    "access",
    "refresh",
]  # allow blacklisting for access and refresh tokens

app.secret_key = "jose"  # could do app.config['JWT_SECRET_KEY'] if we prefer
api = Api(app)


@app.before_first_request
def create_tabeles():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["jti"] in BLACKLIST


api.add_resource(Transaction, "/transaction/<int:amt>")
api.add_resource(TransactionList, "/transactions")
api.add_resource(Student, "/student/<string:name>")
api.add_resource(StudentList, "/students")
api.add_resource(PendingFees, "/pending")
api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
