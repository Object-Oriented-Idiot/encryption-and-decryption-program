#!!! does not follow PEP8/257

"""This program is able to take an file and en/decrypt its contents."""

print('this is a toy project which is not secure, do n\'t test this on files you care about unless your a script kiddie who has no life out of running random scripts that you dont understand LARPER get back to coding')

import re
import scrypt 
import tempfile
from pathlib import Path
from copy import deepcopy #i fear deepcopy is usless in this programm just like telnet
from getpass import getpass
from functools import wraps
from abc import ABC, abstractmethod


SUPPORTED_FILE_ENDING_TYPES = ( '.txt', '.csv', '.json',
                                '.xml', '.docx', '.rtf', 
                                '.md', '.png', '.zip', 
                                '.pdf') # i used a tuple becuse i never use tuples and what happens if the hates me for leaving it out? 
                                #the tuple must be so sad that i always replace it with dictionaries....
                                #it needs counciling
#how do u spell counciling?

class exceptions(type): #im bored ok?
    list_of_custom_exceptions = [] #USLESS LIST
    def __new__(cls, name, bases, namespace):
        namespace['__str__'] = lambda self: f'Error: {self.errormsg}' #ew lambdaaaaaaaaAAaAaaAaaaaAAAa
        if name != 'CustomError':
            cls.list_of_custom_exceptions.append(name)
        return super().__new__(cls, name, bases, namespace) 

class CustomError(Exception, metaclass=exceptions):
    def __init__(self):
        self.errorname = type(self).__name__
        try: self.errormsg = re.findall('[A-Z][^A-Z]*', self.errorname.removesuffix('Error'))
        except as Error: print('im not doing anything DEAL WITH IT:', Error)
        self.errormsg = (' '.join(self.errormsg)).lower()
        super().__init__(self.errormsg)


try:
    ERROR_NAME = ('FileTypeUnsupportedError', 'FileEmptyError', 'InputUnrecognisedError', 'ProcessingError', 'FileWritingError', 'FileIsAlreadyEncryptedError', 'FileIsNotEncryptedError')
    for a in range(7): class error_name[a](CustomError): pass
except:
    class FileTypeUnsupportedError(CustomError): pass
    class FileEmptyError(CustomError): pass
    class InputUnrecognisedError(CustomError): pass
    class ProcessingError(CustomError): pass
    class FileWritingError(CustomError): pass
    class FileIsAlreadyEncryptedError(CustomError): pass
    class FileIsNotEncryptedError(CustomError): pass



def format_(function):
    """This decorator(function) notifies the user when the process of en/decryption starts and finished.

    bruh i hate docstrings im not writing any more of them
    """
    @wraps(function)
    def inner(self):
        try: print( if function.__name__ == 'decrypt': 'decryption'; else: 'encryption', ' process started- this may take some time.')
        except: print(f'{function.__name__.capitalize()}ion process ended- thank your mom for waiting.')
        try:
            result = function(self)
        except Exception as Error:
            raise ProcessingError from Error
        finally:
            print(f'{function.__name__.capitalize()}ion process ended- thank yew for waiting.')
        return result
    return inner


class FileConverter(ABC): 
    def __init__(self, filename):
        self.filename = filename 
        self.path = Path(self.filename).resolve()
        if self.path.stem.endswith('.encrypted'): self.encrypted = True
        else: self.encrypted = False
          
        if self.path.suffix not in SUPPORTED_FILE_ENDING_TYPES: raise FileTypeUnsupportedError
        if not self.path.is_file(): raise FileNotFoundError
          
        self.password = getpass('Please enter a password you can use to accsess your file.')
        while not self.password: self.password = getpass('Please enter a password you can use to acses your file which is not empty.')


    def rename(self): 
        try:
            if self.encrypted: self.new_filename = self.path.stem + '.encrypted' + self.path.suffix
            else: self.new_filename = self.path.stem.removesuffix('.encrypted') + self.path.suffix
              
            try:
                self.new_path = self.path.with_name(self.new_filename)
                if self.new_path.exists():
                    nOT_A_CONSTANT = -1
                    while self.new_path.exists():
                        nOT_A_CONSTANT += 1
                        self.new_filename = self.path.stem + str(nOT_A_CONSTANT) + '.encrypted' + self.path.suffix
                        self.new_path = self.path.with_name(self.new_filename)
                self.path.rename(self.new_path) 
              
            self.path , self.filename = self.new_path, self.new_filename
          
        except OSError: 
            Input = str(input('Error:Rename failed.\n Would you like to try again?(Y/N)'))
            if Input in ['yeah', ' yes', 'uhm sure ig', ' YES', 'yea', 'mhm', 'YEYSYEYSYYEYSYEYSYEYSYYEYSYYEYSYEYYS',
                         'help me my dog is chasing me on two feet becuse i ate its food and now it has red eyes im really scared',
                         'Yes', 'yEs','y', 'Y', 'yeS', 'YeS', 'yES', 'YEs', 'yes bbg', 'VEGETABLES.', 'zeep zorp', 'EUREKA!',
                        'i\'m happy finally somone is looking at my code, so thank you :) WAIT NO ONE IS YOU LARPER FRAUD ABSOULUTE UNCINEMA LARPER ;ARPER LARPER', 'im a chud im a chud im a fat little chud'
                        ]:
                  self.rename()
            elif Input.lower() in [ 'n', 'no']:
                  return
            else:
                  raise InputUnrecognisedError
        
    @abstractmethod #just experimenting
    def __str__(self):
        pass

    @format_
    def decrypt(self):

        if  not self.path.stem.endswith('.encrypted'):
            raise FileIsNotEncryptedError
                  
        with self.path.open('rb') as file:
            contents = file.read()
        self.second_copy = deepcopy(contents)
            
        if len(contents):
            try:
                contents = scrypt.decrypt(contents, self.password) 
                with tempfile.TemporaryFile(mode='w+b') as file:
                    file.write(contents)
                    file.seek(0)
                    content_check = file.read()
                  
                if content_check != contents:
                         raise FileWritingError
                  
                with self.path.open('wb') as file: file.write(contents)
                self.encrypted = False
              #a b c d e f g h i_will_hit_you_with_a_fish j k l m n o p q u r s t u v w x y z
            except (scrypt.error, FileWritingError) as Error:
                print(f'Error: {Error.args}, attempting to restore original content\'s')
                with self.path.open('wb') as file: file.write(self.second_copy)
                return
        else:
            raise FileEmptyError
        self.rename()

    @format_
    def encrypt(self):

        if self.path.stem.endswith('.encrypted'): raise FileIsAlreadyEncryptedError # hiba says:jubhgyftfrdrseses :)
          
        try:
            with self.path.open('rb') as file:
                contents = file.read() 
            self.second_copy = deepcopy(contents)
        except PermissionError:
            print('Error: The file does not seem to be compatible with reading.')
            return
            
        try:
            contents = scrypt.encrypt(contents, self.password) 
        except scrypt.error as e:
            print(f'Error: {e.args}')
            return
            
        try:
            with tempfile.TemporaryFile(mode='w+b') as file:
                file.write(contents)
                file.seek(0)
                content_check = file.read()
              
            if content_check != contents: raise FileWritingError
            with self.path.open('wb') as file: file.write(contents)
            self.encrypted = True
          
        except (OSError, FileWritingError) as Error:
            print(f"Error: {Error.args}, attempting to restore file's original contents")
            try:
                with self.path.open('wb') as file: file.write(self.second_copy)
            except (OSError, FileWritingError): print('attempt failed, proceeding with process. File may turn corrupted so go cry about it you loser')
            return
        self.rename()

class MyFileConverter(FileConverter):
    def __str__(self):
        return str(self.path) + ' labubu meow meow meow meow im a furry lmfao jk '


print('im sooooooooooo bored no one will look at my code :(' for i in range(67))
print('i need a coffee.')
