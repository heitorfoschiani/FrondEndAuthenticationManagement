# Author: Heitor Foschiani de Souza
# Email: heitor.foschiani@outlook.com
# Phone-number: (11) 9 4825-3334

from flask import Flask, render_template, redirect, url_for, jsonify, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask_cors import CORS
import jwt
from datetime import datetime, timedelta

import api_requests
from forms import FormCreateAccount, FormLogin


app = Flask(__name__)
app.config["SECRET_KEY"] = "my-secret-key"
CORS(app)


# User management
login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, user_id, access_token):
        self.id = user_id
        self.access_token = access_token

@login_manager.user_loader
def load_user(user_id):
    access_token = session["access_token"]
    if not access_token:
        return None

    user = User(
        user_id = user_id, 
        access_token = access_token
    )

    return user

# User management routes
@app.route("/create-account", methods=["GET", "POST"])
def create_account():
    form_create_account = FormCreateAccount()

    if form_create_account.validate_on_submit():
        full_name = form_create_account.full_name.data
        email = form_create_account.email.data.lower()
        phone = form_create_account.phone.data
        username = form_create_account.username.data.lower()
        password = form_create_account.password.data

        # registring user in the server
        response = api_requests.register_user(full_name, email, phone, username, password)

        # getting back user informations
        if response.status_code == 200:
            # login user
            js = response.json()

            user_id = js["user_id"]
            access_token = js["access_token"]
            refresh_token = js["refresh_token"]

            session["user_id"] = user_id
            session["access_token"] = access_token
            session["refresh_token"] = refresh_token

            user = User(
                user_id = user_id, 
                access_token = access_token
            )
            login_user(user)

            return redirect(url_for("home"))
        elif response.status_code == 401:
            if "email" in response.text:
                form_create_account.email.errors.append("This email already exist")
            elif "username" in response.text:
                form_create_account.username.errors.append("This username already exist")
    
    return render_template("create_account.html", form_create_account=form_create_account)

@app.route("/login", methods=["GET", "POST"])
def login():
    form_login = FormLogin()

    if form_login.validate_on_submit():
        username = form_login.username.data.lower()
        password = form_login.password.data

        # requesting permission on the back-end (API)
        response = api_requests.authenticate_user(username, password)
        if response.status_code == 404:
            form_login.username.errors.append("Non-existent username.")
        elif response.status_code == 401:
            form_login.password.errors.append("Incorrect password.")
        elif response.status_code == 500:
            form_login.password.errors.append("Error on server.")
        elif response.status_code == 200:
            # login user
            js = response.json()

            user_id = js["user_id"]
            access_token = js["access_token"]
            refresh_token = js["refresh_token"]

            session["user_id"] = user_id
            session["access_token"] = access_token
            session["refresh_token"] = refresh_token

            user = User(
                user_id = user_id, 
                access_token = access_token
            )
            login_user(user)

            return redirect(url_for("home"))
        else:
            form_login.password.errors.append("Something get wrong")
    
    return render_template("login.html", form_login=form_login)

@app.route("/get-access-token", methods=["GET"])
def get_access_token():
    if current_user.is_authenticated and "access_token" in session:
        access_token = session["access_token"]
        decoded_jwt = jwt.decode(access_token, options={"verify_signature": False})

        exp_time = datetime.fromtimestamp(decoded_jwt["exp"])
        now = datetime.now()

        if (exp_time - now) <= timedelta(minutes=1):
            response = api_requests.refresh_authentication(session["refresh_token"])
            if response.status_code == 200:
                js = response.json()

                user_id = js["user_id"]
                access_token = js["access_token"]
                refresh_token = js["refresh_token"]

                session["user_id"] = user_id
                session["access_token"] = access_token
                session["refresh_token"] = refresh_token

        return jsonify(access_token=access_token), 200
    else:
        return jsonify(error="unauthorized"), 401

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


# App routes
@app.route("/")
def home():
    if current_user.is_authenticated:
        return render_template("home.html")
    else:   
        return redirect(url_for("login"))