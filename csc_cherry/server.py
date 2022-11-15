import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.8.120', 43960))

server.listen()

while True:
    user, adres = server.accept()
    print('User connected!')
    user.send('Server is working!'.encode('utf-8'))

    data = user.recv(1024)
    print(data.decode('utf-8'))
    user.send('Server is working!!!'.encode('utf-8'))