import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.8.120', 43960))

while True:
    data = client.recv(1024)

    print(data.decode('utf-8'))

    x = input()
    client.send(x.encode('utf-8'))