import socket as so
from utils import *



s = so.socket()
print("Connection made")



port = 8787
s.bind(('localhost',port))
admin = input("Enter name of admin : ")
key = input("Enter key for security : ")

s.listen(1)

print('Waiting for connections')

while True:
    c, addr = s.accept()
    while True:
        
            
        msg = c.recv(1024).decode()
        # print("recieved msg ",msg)
        decrypted_msg = decrypt(msg,int(key))
        if decrypted_msg == ";":
            break
        
        
        c.send(bytes(decrypted_msg,'utf-8'))



