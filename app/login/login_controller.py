class User:
    def __init__(self):
        self._users = [
            {
                "email":"admin@gmail.com",
                "password":"admin123"
            },
            {
                "email":"user@gmail.com",
                "password":"user123"
            }
        ]

    def get_users(self):
        return self._users

class LoginController:
    def __init__(self):
        self.user = User()

    def login(self, email, password):
        users = self.user.get_users()
        match_user = None
        login_status = None
        error_message = None

        for user in users:
            if user.get('email') == email and user.get('password') == password:
                match_user = user
        
        if match_user:
            login_status = True
            error_message = ""
        else:
            login_status = False
            error_message = "Incorrect email or password!"
        return login_status, error_message, match_user