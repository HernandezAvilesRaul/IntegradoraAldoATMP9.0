class User:
    def __init__(self, username, password): 
        self.username = username
        self.password = password

    def validate(self, inputUsername, inputPassword):
        return self.password == inputPassword and inputUsername == self.username
        