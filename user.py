from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id, access_token):
        self.id = user_id
        self.access_token = access_token