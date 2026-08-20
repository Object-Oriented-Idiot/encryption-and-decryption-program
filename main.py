#docstrings
#try exept error handling
#add *args and **kwargs things
import scrypt
from getpass import getpass
from functools import wraps

def check_password(password):
    UI = str(input('Please input the password needed to view this file.'))
    if UI == password:
        return True
    else:
        print('Incorrect password.')
        return False

def format_(function):
    @wraps(function)    
    def inner(self):
        print(f'{function.__name__.capitalize()}ion process started- this may take some time.')
        result = function(self)
        print(f'{function.__name__.capitalize()}ion process finished- thank you for waiting.')
        return result
    return inner


class FileConverter():
    def __init__(self, filename):
        self.filename = filename 
        self.password = getpass.getpass('Please enter a password you can use to accsess your file.')
        if not self.password:
            self.password = getpass.getpass('Please enter a password you can use to accsess your file.')
        
    @format_
    def decrypt(self):
        if check_password(self.password):
            with open(self.filename, 'rb') as file:
                contents = file.read()
            if len(contents):
                 new_contents = scrypt.decrypt(contents, self.password)
            else:
                print('file seems to be empty')
            with open(self.filename, 'wb') as file:
                file.write(new_contents)


    @format_
    def encrypt(self):
        with open(self.filename, 'rb') as file:
                contents = file.read()
        new_contents = scrypt.encrypt(contents, self.password)
        with open(self.filename, 'wb') as file:
            file.write(new_contents)
    
