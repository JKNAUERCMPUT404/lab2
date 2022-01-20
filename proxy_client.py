import client
import multiprocessing
import socket

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def proxy_client():
    # Create socket and connect to the proxy server
    s = client.create_tcp_socket()
    s.connect((HOST, PORT))

    # Send payload to the proxy server
    payload = "GET / HTTP/1.0\r\nHost: \r\n\r\n"
    client.send_data(s, payload)
    s.shutdown(socket.SHUT_WR)
    
    # Listen on socket until proxy server returns response
    full_data = b""
    while True:
        data = s.recv(BUFFER_SIZE)
        if not data:
            break
        full_data += data
    print(full_data)
    s.close()

if __name__ == "__main__":
    p = multiprocessing.Process(target=proxy_client)
    p.start()
    p.join()