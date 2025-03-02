import socket

def tcpServer(host="0.0.0.0", port = 7054):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(1)
    print(f"TCP Server listening on {host}:{port}")

    conn,addr = server.accept()
    print(f"Connected by {addr}")

    while (1):
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)

    conn.close()

tcpServer()
