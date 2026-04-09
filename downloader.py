import socket
import ssl
import time

def download_file():
    HOST = "192.168.1.10"   # replace with server IP
    PORT = 5000

    context = ssl.create_default_context()
    context.load_verify_locations("cert.pem")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_client = context.wrap_socket(client, server_hostname="localhost")

    secure_client.settimeout(5)
    secure_client.connect((HOST, PORT))

    start = time.time()

    packet_count = 0
    total_bytes = 0
    data = b''

    try:
        while True:
            chunk = secure_client.recv(4096)
            if not chunk:
                break
            data += chunk
            packet_count += 1
            total_bytes += len(chunk)
    except socket.timeout:
        pass

    end = time.time()
    secure_client.close()

    size = len(data)
    time_taken = end - start if (end - start) > 0 else 0.001
    speed = (size * 8) / time_taken / 1000000

    return size, time_taken, speed, packet_count