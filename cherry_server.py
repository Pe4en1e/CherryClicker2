import socket



# client.send(method.encode())
# client.recv(1024)
# client.send(login.encode())
# client.recv(1024)
# client.send(passwd.encode())
# result = client.recv(1024)
# print(result.decode())

class auth():
    def reg(x, y):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('95.165.142.147', 1332))
        method = 'reg'
        client.send(method.encode())
        client.recv(1024)
        client.send(str(x).encode())
        client.recv(1024)
        client.send(str(y).encode())
        result = client.recv(1024)
        client.close()
        print(result.decode())
        return result.decode()
    
    def login(x, y):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('95.165.142.147', 1332))
        method = 'login'
        client.send(method.encode())
        client.recv(1024)
        client.send(str(x).encode())
        client.recv(1024)
        client.send(str(y).encode())
        result = client.recv(1024)
        client.close()
        print(result.decode())
        return result.decode()
