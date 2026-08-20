#i am PARANOID of code faliure and therefore put 22 exception catching branches...
#!!! does not follow PEP8's recomendation on docstring and line length

"""This program is able to take a file and en/decrypt its contents."""

import scrypt
from getpass import getpass
from functools import wraps


def check_password(password, *args, **kwargs):
    """This function check's if the User's input matches the password provided.
    Type: Function
    Intended arguments: the password that will be used to en/decrypt the file of the user's choice
    Return values: True if User's input match password, False if it does not
    Side effects: If any extra arguments are inserted, a message is outputed
    """
    if len(*args) > 0 or len(**kwargs) > 0:
        print('Error: extra arguments taken in as input. These will be ignored.')
    UI = str(input('Please input the password needed to view this file.'))
    if UI == password:
        return True
    else:
        print('Incorrect password.')
        return False
        

def format_(function, *args, **kwargs):
    @wraps(function)
    """This decorator(function) notifies the user when the process of en/decryption starts and finished.

    Type: Decorator
    Intended arguments: the encrypt function or the decrypt function
    Return values: Returns two messages about the progress each time it is called
    Side effects: If any extra arguments are inserted, a message is outputed
    """
    if len(*args) > 0 or len(**kwargs) > 0:
        print('Error: extra arguments taken in as input. These will be ignored.')
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

    def __init__(self, filename, *args, **kwargs):
        """The initialiser processes the filename and sets a password used for encryption/decryption.
        
        Type: Initialising function for an instance
        Intended arguments: the filename of the file to be en/decrypted
        Side effects: If any extra arguments are inserted, a message is outputed
        """
        if len(*args) > 0 or len(**kwargs) > 0:
            print('Error: extra arguments taken in as input. These will be ignored.')
        self.filename = filename 
        self.password = getpass('Please enter a password you can use to accsess your file.')
        if not self.password:
            self.password = getpass('Please enter a password you can use to accsess your file.')
        
    @format_
    def decrypt(self, *args, **kwargs):
    """The function decrypts files contents of a given file.
    
        Type: Function
        Side effects: If any extra arguments are inserted, a message is outputed
        Exceptions raised: FileNotFoundError, PermissionError, EOFError, OSError, Exception, scrypt.error
        """        
        if len(*args) > 0 or len(**kwargs) > 0:
            print('Error: extra arguments taken in as input. These will be ignored.')
        try:
            if check_password(self.password):
                with open(self.filename, 'rb') as file:
                    contents = file.read()
        except FileNotFoundError:
            print('Error: The file that you are trying to encrypt does not exist.')
            exit()
        except PermissionError:
            print('Error: The file does not seem to be compatible with reading.')
            exit()
        except EOFError:
            print('Error: File is empty.')
            exit()
        except OSError as e:
            print(f'Error: {e.args}')
            exit()
        except Exception as e:
            print(f'Error: {e.args}')
            exit()
            
        if len(contents):
            try:
                 new_contents = scrypt.decrypt(contents, self.password) 
            except scrypt.error as e:
                    print(f'Error: {e.args}')
                    exit()
                
            else:
                print('file seems to be empty')
            try:
                with open(self.filename, 'wb') as file:
                    file.write(new_contents)
            except FileNotFoundError:
                print('Error: The file that you are trying to encrypt does not exist.')
                exit()
            except PermissionError:
                print('Error: The file does not seem to be compatible with reading.')
                exit()
            except EOFError:
                print('Error: File is empty.')
                exit()
            except OSError as e:
                print(f'Error: {e.args}')
                exit()
            except Exception as e:
                print(f'Error: {e.args}')
                exit()

    @format_
    def encrypt(self, *args, **kwargs):
    """The function encrypts files contents of a given file.
    
        Type: Function
        Side effects: If any extra arguments are inserted, a message is outputed
        Exceptions raised: FileNotFoundError, PermissionError, EOFError, OSError, Exception, scrypt.error
        """
        if len(*args) > 0 or len(**kwargs) > 0:
            print('Error: extra arguments taken in as input. These will be ignored.')
        try:
            with open(self.filename, 'rb') as file:
                    contents = file.read()
        except FileNotFoundError:
            print('Error: The file that you are trying to encrypt does not exist.')
            exit()
        except PermissionError:
            print('Error: The file does not seem to be compatible with reading.')
            exit()
        except EOFError:
            print('Error: File is empty.')
            exit()
        except OSError as e:
            print(f'Error: {e.args}')
            exit()
        except Exception as e:
            print(f'Error: {e.args}')
            exit()
            
        try:
            new_contents = scrypt.encrypt(contents, self.password) 
        except scrypt.error as e:
            print(f'Error: {e.args}')
            exit()
            
        try:
            with open(self.filename, 'wb') as file:
                file.write(new_contents)
        except FileNotFoundError:
            print('Error: The file that you are trying to encrypt does not exist.')
            exit()
        except PermissionError:
            print('Error: The file does not seem to be compatible with reading.')
            exit()
        except EOFError:
            print('Error: File is empty.')
            exit()
        except OSError as e:
            print(f'Error: {e.args}')
            exit()
        except Exception as e:
            print(f'Error: {e.args}')
            exit()

