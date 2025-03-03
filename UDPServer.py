import socket

def udpServer(host="0.0.0.0", port=5001):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")

    while True:
        data, addr = server.recvfrom(1024)
        server.sendto(data, addr)  

udpServer()
