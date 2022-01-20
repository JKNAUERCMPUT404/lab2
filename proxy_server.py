#!/usr/bin/env python3
import client
import multiprocessing
import socket

#define address & buffer size
HOST = ""
PROXY_PORT = 8001
REMOTE_PORT = 80
BUFFER_SIZE = 1024

def send_bytes(conn, data):
    print("Sending data to client")
    try:
        conn.sendall(data)
    except (socket.error, msg):
        print(f'Failed to send data. Error code: {str(msg[0])} , Error message : {msg[1]}')
    print("Data send to client successfully")

def proxy_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Allow multiple connections
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind socket to the address
        s.bind((HOST, PROXY_PORT))

        # Set to listening mode
        s.listen(2)

        # Coninue to listen for new connections
        while True:
            try:
                conn, addr = s.accept()

                # Receive data from the client
                client_data = b""
                while True:
                    data = conn.recv(BUFFER_SIZE)
                    if not data:
                        break
                    client_data += data

                # Forward client data to google
                remote = "www.google.com"
                remote_ip = client.get_remote_ip(remote)
                g_socket = client.create_tcp_socket()
                g_socket.connect((remote_ip, REMOTE_PORT))
                client.send_data(g_socket, client_data.decode())
                g_socket.shutdown(socket.SHUT_WR)

                # Receive response from google and send back to client
                full_data = b""
                while True:
                    data = g_socket.recv(BUFFER_SIZE)
                    if not data:
                        break
                    full_data += data
                
                send_bytes(conn, full_data)
            except Exception as e:
                print(e)
            finally:
                g_socket.close()
                conn.close()
            
if __name__ == "__main__":
    p = multiprocessing.Process(target=proxy_server)
    p.start()
    p.join()