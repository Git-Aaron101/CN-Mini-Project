import socket
import time

def download_file():
    HOST = "example.com"
    PORT = 80
import socket
import time

def download_file():
    HOST = "example.com"   # safer than google
    PORT = 80

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)   # IMPORTANT: prevents hanging
    client.connect((HOST, PORT))

    request = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"
    client.send(request.encode())

    start = time.time()

    data = b''
    try:
        while True:
            chunk = client.recv(4096)
            if not chunk:
                break
            data += chunk
    except socket.timeout:
        # stop if server doesn't close connection
        pass

    end = time.time()
    client.close()

    size = len(data)
    time_taken = end - start if (end - start) > 0 else 0.001

    speed = (size * 8) / time_taken / 1000000  # Mbps

    return size, time_taken, speed
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