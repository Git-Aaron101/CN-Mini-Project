import socket
import time

def download_file():
    HOST = "example.com"
    PORT = 80

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
    client.send(request.encode())

    start = time.time()

    data = b''
    while True:
        chunk = client.recv(4096)
        if not chunk:
            break
        data += chunk

    end = time.time()
    client.close()

    size = len(data)
    time_taken = end - start
    speed = (size * 8) / time_taken / 1000000  # Mbps

    return size, time_taken, speed