from Model.loginModel.userCredentials import User

testUser = User("Raul", "Sekiro")

def authenticateCredentials(username, password):
    return testUser.validate(username, password)