import socket
import ssl

HOST = '127.0.0.1'
PORT = 5000

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("SSL Server running...")

with context.wrap_socket(server, server_side=True) as secure_server:
    while True:
        conn, addr = secure_server.accept()
        print("Connected:", addr)

        data = b'x' * 1024 * 1024  # 1 MB
        conn.sendall(data)

        conn.close()
