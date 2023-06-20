# Copyright (C) 2022 NG:ITL
import socket
import select
import pynng

IMAGE_WIDTH = 1280
IMAGE_HEIGHT = 720
IMAGE_DEPTH = 3

IMAGE_SIZE = IMAGE_WIDTH * IMAGE_HEIGHT * IMAGE_DEPTH

SERVER_INBOUND_IP = '127.0.0.1'
SERVER_INBOUND_PORT = 50000

NNG_ADDRESS = "ipc:///tmp/RAAI/broker.ipc"

class LiveImageBroker:

    def __init__(self) -> None:
        self.server_inbound_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_inbound_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_inbound_sock.bind((SERVER_INBOUND_IP, SERVER_INBOUND_PORT))
        self.server_inbound_sock.listen(1)

        self.outbound_sock = pynng.Pub0()
        self.outbound_sock.listen(NNG_ADDRESS)
        print(f'Publishing to the address {NNG_ADDRESS}')

        self.client_inbound_sock = None

        self.image_count = 0

    def run(self) -> None:
        while True:
            socket_list = [self.server_inbound_sock]
            if self.client_inbound_sock:
                socket_list.append(self.client_inbound_sock)

            read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

            if self.server_inbound_sock in read_sockets:
                self.handle_incoming_inbound_connection()

            if self.client_inbound_sock and self.client_inbound_sock in read_sockets:
                self.handle_client_inbound_data()

    def close_client_inbound_socket(self):
        self.client_inbound_sock.close()
        self.client_inbound_sock = None
        print(f'Inbound client disconnected')

    def handle_incoming_inbound_connection(self) -> None:
        self.client_inbound_sock, address = self.server_inbound_sock.accept()
        print(f'Inbound client connected: {address}')

    def handle_client_inbound_data(self) -> None:
        try:
            data = self.client_inbound_sock.recv(IMAGE_SIZE, socket.MSG_WAITALL)
            self.image_count = self.image_count + 1
            if len(data) != IMAGE_SIZE:
                self.close_client_inbound_socket()
            elif self.outbound_sock:
                self.outbound_sock.send(data)
        except:
            self.close_client_inbound_socket()
