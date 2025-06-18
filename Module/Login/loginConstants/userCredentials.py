class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validateUsers(self,inputUsername, inputPassword):
        return self.password == inputPassword and self.username == inputUsername
    