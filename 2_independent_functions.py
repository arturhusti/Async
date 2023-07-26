import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


def accept_connection(server_socket):
    while True:
        # reading operation - waiting for client accept
        client_socket, addr = server_socket.accept()
        print('connection from addres: ', addr)
        send_message(client_socket)


def send_message(client_socket):
    while True:
        # reading operation - waiting data from client
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello\n'.encode()
            # writing operation - send data
            client_socket.send(response)

    client_socket.close()


if __name__ == '__main__':
    accept_connection(server_socket)
