from tkinter import messagebox
import scrypt
import secrets


file = open('salt.txt','rb')
salt = file.readline()
file.close()

def upd(filename):
    print('decryption process started- this may take some time.')
    file = open(filename, 'rb')
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

def decrypt_(victim):
    result = []
    result.append(scrypt.decrypt(victim, salt))
    return result
    
upd('hi.txt')
print('decyption process finished, ty for waiting!')
