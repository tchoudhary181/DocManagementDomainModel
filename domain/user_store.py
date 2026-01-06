class UserStore:
    def __init__(self):
        self._users = {}

    def add_user(self, user):
        if user.get_id() in self._users:
            raise ValueError("User already exists.")
        self._users[user.get_id()] = user

    def get_user(self, user_id):
        if user_id not in self._users:
            raise KeyError("User not found.")
        return self._users[user_id]

    def user_exists(self, user_id):
        return user_id in self._users

    def list_users(self):
        return list(self._users.values())

    def remove_user(self, user_id):
        if user_id not in self._users:
            raise KeyError("User not found.")
        del self._users[user_id]
