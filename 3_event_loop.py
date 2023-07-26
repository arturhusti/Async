import socket
from select import select


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

monitor_reading = []


def accept_connection(server_socket):
    # reading operation - waiting for client accept
    client_socket, addr = server_socket.accept()
    print('connection from addres: ', addr)
    monitor_reading.append(client_socket)


def send_message(client_socket):
    # reading operation - waiting data from client
    request = client_socket.recv(4096)

    if request:
        response = 'Hello\n'.encode()
        # writing operation - send data
        client_socket.send(response)
    else:
        monitor_reading.remove(client_socket)
        client_socket.close()


def event_loop():
    while True:

        rfr, _, _ = select(monitor_reading, [], [])  # read, write, errors

        for sock_read in rfr:
            if sock_read is server_socket:
                accept_connection(sock_read)
            else:
                send_message(sock_read)


if __name__ == '__main__':
    monitor_reading.append(server_socket)
    event_loop()
