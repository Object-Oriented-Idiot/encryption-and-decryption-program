#!!! does not follow PEP8's recomendation on docstring and line length
#waaaaaaaaaaaaah i want another labubu :< T^T 
#actually its not pep8/257 aligned never mind...

# couldn't test it because I just changed OS to Kali, had no internet to install vs-code , and was using the basic text editor  and i cant spell anyways
"""This program is able to take a file and en/decrypt its contents."""

import scrypt
import copy
from getpass import getpass
from functools import wraps
from abc import ABC, abstractmethod
from pathlib import Path


types = ( '.txt', '.csv', '.json',
         '.xml', '.docx', '.rtf',
         '.md', '.png', '.zip', 
        '.pdf') #used a tuple becuse i never use tuples normally and i dont want tuples to feel left out 


def format_(function):
    """This decorator(function) notifies the user when the process of en/decryption starts and finished.

    bruh i hate docstrings
    Intended arguments: the encrypt function or the decrypt function
    Return values: Returns two messages about the progress each time it is called
    """
    @wraps(function)
    def inner(self):
        print(f'{function.__name__.capitalize()}ion process started- this may take some time.')
        try:
            result = function(self)
        finally:
            print(f'{function.__name__.capitalize()}ion process finished- thank you for waiting.')
        return result
    return inner

class FileConverter(ABC): 
    """This class takes a file and is able to encrypt and decrypt it.

    Public methods: encrypt, decrypt
    """
    def __init__(self, filename):
        """The initialiser processes the filename and sets a password used for encryption/decryption.
        
        Type: Initialising function for an instance
        Intended arguments: the filename of the file to be en/decrypted
        """
        self.filename = filename 
        self.path = Path(self.filename).resolve()
        if self.path.stem.endswith('_encrypted'):
            self.encrypted = True
        else:
            self.encrypted = False
        if self.path.suffix not in types:
                print('File type currenlty unsuported')
                raise Exception('File type unsuported')
        if not self.path.is_file():
                raise FileNotFoundError('File not found')
        self.password = getpass('Please enter a password you can use to accsess your file.')
        while not self.password:
            self.password = getpass('Please enter a password you can use to accsess your file which is not empty.')


    def rename(self): 
        try:
            if self.encrypted:
                self.new_filename = self.path.stem + '_encrypted' + self.path.suffix
            else:
                self.new_filename = self.path.stem.removesuffix('_encrypted') + self.path.suffix
            try:
                self.new_path = self.path.with_name(self.new_filename)
                self.path.rename(self.new_path)
            except FileExistsError:
                print('Error: File exists')
            self.path = self.new_path
            self.filename = self.new_filename
            self.encrypted = not self.encrypted
        except:
            Input = str(input('Error:Rename failed.\n Would you like to try again?(Y/N)'))
            if Input in ['yeah', ' yes', 'uhm sure ig', ' YES', 'yea', 'mhm', 'YEYSYEYSYYEYSYEYSYEYSYYEYSYYEYSYEYYS',
                         'help me my dog is chasing me on two feet becuse i ate its food and now it has red eyes im really scared',
                         'Yes', 'yEs','y', 'Y', 'yeS', 'YeS', 'yES', 'YEs', 'yes bbg', 'VEGETABLES.', 'zeep zorp']
                  self.rename()
            elif Input in ['N', 'n', 'no', 'NO', 'No', 'nO']:
                  return
            else:
                  print('input not recognised, not trying again')
                  return
        
    @abstractmethod #just experimenting, no subclass yet
    def __str__(self):
        pass

    @format_
    def decrypt(self):
        """The function decrypts files contents of a given file.
    
        Exceptions raised: FileNotFoundError, OSError,  scrypt.error
        """       
        try:
             with self.path.open('rb') as file:
                 contents = file.read()
             self.second_copy = copy.deepcopy(contents)
        except FileNotFoundError:
            print('Error: The file that you are trying to decrypt does not exist.')
            return
            
        if len(contents):
            try:
                new_contents = scrypt.decrypt(contents, self.password) 
                with self.path.open('wb') as file:
                    file.write(new_contents)
            except scrypt.error as e:
                print(f'Error: {e.args}')
                with self.path.open('wb') as file:
                    file.write(self.second_copy)
                return
                
        else:
            print('file seems to be empty')
            return
        try:
            self.encrypted = False
            self.rename()
        except FileNotFoundError as e:
                print(e.args)

    @format_
    def encrypt(self):
        """The function encrypts files contents of a given file.
    
        Exceptions raised: FileNotFoundError, PermissionError, OSError, scrypt.error
        """
        try:
            with self.path.open('rb') as file:
                contents = file.read()
            self.second_copy = copy.deepcopy(contents)
        except FileNotFoundError:
            print('Error: The file that you are trying to encrypt does not exist.')
            return
        except PermissionError:
            print('Error: The file does not seem to be compatible with reading.')
            return
            
        try:
            contents = scrypt.encrypt(contents, self.password) 
        except scrypt.error as e:
            print(f'Error: {e.args}')
            return
            
        try:
            with self.path.open('wb') as file:
                file.write(contents)
        except OSError as e:
            print(f"Error: {e.args}, attempting to restore file's original contents")
            with self.path.open('wb') as file:
                file.write(self.second_copy)
            
            return
        try:
            self.encrypted = True
            self.rename()
        except FileNotFoundError as e:
                print(e.args)


#my (out of school)freinds just took photos of each other and shoved them in AI to make them bald and now they are crying about it AND I HAVE TO SOLVE THIS MESS
