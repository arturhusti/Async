import socket
from select import select

reading = {}
writing = {}

tasks = []


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        yield ('r', server_socket)
        # reading operation - waiting for client accept
        client_socket, addr = server_socket.accept()
        print('connection from addres: ', addr)
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        yield ('r', client_socket)
        # reading operation - waiting data from client
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello\n'.encode()

            yield ('w', client_socket)
            # writing operation - send data
            client_socket.send(response)

    client_socket.close()


def event_loop():

    while any([tasks, reading, writing]):

        while not tasks:
            rfr, rfw, _ = select(reading, writing, [])  # reading, writing, exceptions

            for sock_read in rfr:
                # reading -> {sock: generator}
                tasks.append(reading.pop(sock_read))

            for sock_write in rfw:
                # writing -> {sock: generator}
                tasks.append(writing.pop(sock_write))

        try:
            task = tasks.pop(0)

            # next(task) -> (reading/writing, socket)
            reason, sock = next(task)

            if reason == 'r':
                reading[sock] = task
            if reason == 'w':
                writing[sock] = task

        except StopIteration:
            pass


tasks.append(server())
event_loop()
