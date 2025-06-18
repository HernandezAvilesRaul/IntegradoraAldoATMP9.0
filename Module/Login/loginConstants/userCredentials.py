class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate(self, input_username, input_password):
        return self.username == input_username and self.password == input_password