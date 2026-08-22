#!!! does not follow PEP8's recomendation on docstring and line length
#waaaaaaaaaaaaah i want a labubu :< T^T
#actually its not pep8/257 aligned never mind...

# couldn't test it because I just changed OS to Kali, had no internet to install vs-code , and was using the basic text editor  and i cant spell anyways
"""This program is able to take a file and en/decrypt its contents."""

import scrypt
from getpass import getpass
from functools import wraps
        

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
    
        Exceptions raised: FileNotFoundError, OSError,  scrypt.error
        """       
        try:
            with open(self.filename, 'rb') as file:
                contents = file.read()
        except FileNotFoundError:
            print('Error: The file that you are trying to decrypt does not exist.')
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

    @format_
    def encrypt(self):
        """The function encrypts files contents of a given file.
    
        Exceptions raised: FileNotFoundError, PermissionError, OSError, scrypt.error
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
        except OSError as e:
            print(f'Error: {e.args}')
            return

