from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id, full_name, email, phone, username):
        self._id = user_id
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.username = username

    def get_id(self):
        return str(self._id)