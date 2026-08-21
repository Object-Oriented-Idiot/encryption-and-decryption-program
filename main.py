#!!! does not follow PEP8's recomendation on docstring and line length
#todo soon: change the implementation from scrypt to smth diffrent, what if encryption fails and the file contents r lost, rename file.type to file.type.encrypted, mix a salt into the password(??), do entire folders/multiple files
#waaaaaaaaaaaaah i want a labubu :< T^T
"""This program is able to take a file and en/decrypt its contents."""

import scrypt
from getpass import getpass
from functools import wraps


def check_password(password):
    """This function check's if the User's input matches the password provided.
    
    Intended arguments: the password that will be used to en/decrypt the file of the user's choice
    Return values: True if User's input match password, False if it does not
    """
    ui = getpass('Please input the password needed to view this file.')
    if ui == password:
        return True
    else:
        print('Incorrect password.')
        return False
        

def format_(function):
    """This decorator(function) notifies the user when the process of en/decryption starts and finished.

    Intended arguments: the encrypt function or the decrypt function
    Return values: Returns two messages about the progress each time it is called
    """
    @wraps(function)
    def inner(self):
        print(f'{function.__name__.capitalize()}ion process started- this may take some time.')
        result = function(self)
        print(f'{function.__name__.capitalize()}ion process finished- thank you for waiting.')
        return result
    return inner


class FileConverter():
    """This class takes a file and is able to encrypt and decrypt it.

    Public methods: encrypt, decrypt
    """

    def __init__(self, filename):
        """The initialiser processes the filename and sets a password used for encryption/decryption.
        
        Type: Initialising function for an instance
        Intended arguments: the filename of the file to be en/decrypted
        """
        self.filename = filename 
        self.password = getpass('Please enter a password you can use to accsess your file.')
        while not self.password:
            self.password = getpass('Please enter a password you can use to accsess your file which is not empty.')
        
    @format_
    def decrypt(self):
        """The function decrypts files contents of a given file.
    
        Exceptions raised: FileNotFoundError, PermissionError, OSError, Exception, scrypt.error
        """       
        try:
            if check_password(self.password):
                with open(self.filename, 'rb') as file:
                    contents = file.read()
        except FileNotFoundError:
            print('Error: The file that you are trying to decrypt does not exist.')
            return
        except PermissionError:
            print('Error: The file does not seem to be compatible with reading.')
            return
        except OSError as e:
            print(f'Error: {e.args}')
            return
            
        if len(contents):
            try:
                 new_contents = scrypt.decrypt(contents, self.password) 
            except scrypt.error as e:
                    print(f'Error: {e.args}')
                    return
                
        else:
            print('file seems to be empty')
            return
        try:
            with open(self.filename, 'wb') as file:
                file.write(new_contents)
        except FileNotFoundError:
            print('Error: The file that you are trying to decrypt does not exist.')
            return
        except PermissionError:
            print('Error: The file does not seem to be compatible with reading.')
            return
        except OSError as e:
            print(f'Error: {e.args}')
            return

    @format_
    def encrypt(self):
        """The function encrypts files contents of a given file.
    
        Side effects: If any extra arguments are inserted, a message is outputed
        Exceptions raised: FileNotFoundError, PermissionError, OSError, Exception, scrypt.error
        """
        try:
            with open(self.filename, 'rb') as file:
                    contents = file.read()
        except FileNotFoundError:
            print('Error: The file that you are trying to encrypt does not exist.')
            return
        except PermissionError:
            print('Error: The file does not seem to be compatible with reading.')
            return
        except OSError as e:
            print(f'Error: {e.args}')
            return
            
        try:
            new_contents = scrypt.encrypt(contents, self.password) 
        except scrypt.error as e:
            print(f'Error: {e.args}')
            return
            
        try:
            with open(self.filename, 'wb') as file:
                file.write(new_contents)
        except FileNotFoundError:
            print('Error: The file that you are trying to encrypt does not exist.')
            return
        except PermissionError:
            print('Error: The file does not seem to be compatible with reading.')
            return
        except OSError as e:
            print(f'Error: {e.args}')
            return

