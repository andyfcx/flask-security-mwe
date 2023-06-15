from flask import Flask, request, jsonify
from auth import Role, User
from flask_login import login_required
from sqlalchemy.orm import sessionmaker
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, SQLAlchemySessionUserDatastore
from flask_security import roles_required, auth_required
from database import db, db_session

app = Flask(__name__)
security = Security(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'
app.config['SECURITY_PASSWORD_SALT'] = 'salt'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
app.config['SECURITY_SEND_PASSWORD_CHANGED_EMAIL'] = False
app.config['SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL'] = False
app.config['SECURITY_SEND_PASSWORD_RESET_EMAIL'] = False
app.config['SECURITY_SEND_CONFIRMATION_EMAIL'] = False
app.config['SECURITY_SEND_LOGIN_EMAIL'] = False
app.config['SECURITY_SEND_CONFIRMATION_EMAIL'] = False
app.config['SECURITY_SEND_RESET_PASSWORD_EMAIL'] = False
app.config['SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL'] = False
app.config['SECURITY_SEND_PASSWORD_CHANGED_EMAIL'] = False
app.config['SECURITY_SEND_PASSWORD_RESET_EMAIL'] = False

db.init_app(app)
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
app.security = Security(app, user_datastore)


# @login_required
@app.route('/', methods=['GET'])
@auth_required()
def index():
    return 'Hello World!'

with app.app_context():
    # create database, user, roles
    db.create_all()
    db.session.commit()
    db.session.close()
    # create user
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    user_datastore.create_user(username='XXXXX', email='XXXXXXXXXXXXXXX', password='admin')



if __name__ == '__main__':
    app.run(debug=True, port=4000)