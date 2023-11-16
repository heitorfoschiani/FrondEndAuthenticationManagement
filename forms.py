from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
import re


class FormCreateAccount(FlaskForm):
    full_name = StringField("full_name")
    email = StringField("email")
    phone = StringField("phone", render_kw={"autocomplete": "off"})
    username = StringField("username")
    password = PasswordField("password")
    password_confirm = PasswordField("password_confirm")
    remember_data = BooleanField("remember_me")
    submit = SubmitField("create account")

    def validate(self, *args, **kwargs):
        is_valid = super(FormCreateAccount, self).validate()
        if not is_valid:
            return False
        
        # checking if the full name field is filled
        if self.full_name.data == "":
            self.full_name.errors.append("Full name is required")
            return False
        
        # checking if the phone number field is filled
        if self.phone.data == "":
            self.phone.errors.append("Phone is required")
        else:
            phone_regex = r"^\+?\d{10,14}$"
            if not re.match(phone_regex, self.phone.data):
                self.phone.errors.append("Invalid phone number format")
                return False
            
        # checking if the username field is filled
        if self.username.data == "":
            self.username.errors.append("Username is required")
            return False
        # checking if the password field have at least 6 characters
        if len(self.password.data) < 6:
            self.password.errors.append("Password must contain at least 6 characters")
            return False
        
        # checking if the the confirm password field is equal password field
        if self.password_confirm.data != self.password.data:
            self.password_confirm.errors.append("This filed must be equal password")
            return False
        
        return True

class FormLogin(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")
    remember_data = BooleanField("remember_me")
    submit = SubmitField("login")

    def validate(self, *args, **kwargs):
        is_valid = super(FormLogin, self).validate()
        if not is_valid:
            return False
        
        # Checking if the username field is filled
        if self.username.data == "":
            self.username.errors.append("Username is required")
            return False
        
        # Checking if the password field have at least 6 characters
        if len(self.password.data) < 6:
            self.password.errors.append("Password must contain at least 6 characters")
            return False

        return True

