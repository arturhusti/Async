import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    print('before server accept')
    client_socket, addr = server_socket.accept()
    print('connection from addres: ', addr)

    while True:
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello\n'.encode()
            client_socket.send(response)

    print('we are in a main While loop')
    client_socket.close()