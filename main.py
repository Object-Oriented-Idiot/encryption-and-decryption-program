#todo:
#make password private
#cli 
#fix encrypt method
#random shi idk

import scrypt
import secrets

def check_password(password)
    UI = str(input('Please input the password needed to view this file.'))
    if UI == password:
        return True
    else:
        print('Incorrect password.')
        return False

def format(function, password) 
    if function.__name__ == decrypt:
        if check_password(password):
            print('decryption process started- this may take some time.')
    else:
        print('encryptoin process started- this may take some time.')
    def inner():
        return function()
    return inner


class idk(filename):
    def __init__(self, filename):
        self.filename = filename
        self.password = str(input('Please enter a password you can use to accsess your file.')
            if !(len(self.password)):
                self.password = str(input('Please enter a password you can use to accsess your file.')
        
    @format(self.password)
    def decrypt(self):
        def upd(self):
            file = open(self.filename, 'rb')
            contents = []
            new_contents = []
            contents = file.read()
            file.close()
            if len(contents):
                 new_contents = decrypt_(contents)
            else:
                print('file seems to be empty')
            file = open(filename, 'wb')
            for item in new_contents:
                item = item.encode("utf-8")
                file.write(item)
            file.close()

        def decrypt_(self):
            result = []
            result.append(scrypt.decrypt(self.filename, self.password))
            return result
        upd('file.txt')
        print('decyption process finished, ty for waiting!')

    @format
    def encrypt(file):
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
    
        upd('file.txt')
        print('encryption process finished, ty for waiting!')

