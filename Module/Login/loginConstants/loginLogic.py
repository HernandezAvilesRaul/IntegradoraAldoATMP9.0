from .userCredentials import user

users =[
    user('sekiro', 'perro'),
    user('raul', 'fornite'),
    user('aldo', 'profesor')
]

admin = user('admin', '123')

def authenticateCredentials(username, password):
    return admin.validateUsers(username, password)
    