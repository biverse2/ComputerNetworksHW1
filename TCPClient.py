import socket
import time

def tcpClient(serverIP, type="latency", port=7054, messageSize=64):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((serverIP, port))

    message = b'X' * messageSize

    if type == "latency":
        start = time.time()
        client.sendall(message)
        client.recv(messageSize)
        end = time.time()
        print(f"TCP RTT for {messageSize} bytes: {(end-start) * 1000:.2f} ms")

    elif type == "throughput":
        totalData = 1024 * 1024
        numMessages = totalData // messageSize
        start = time.time()
        for _ in range(numMessages):
            client.sendall(numMessages):
            client.recv(8)
        end = time.time()
        throughput =(totalData* 8) / (end - start)
        print (f"TCP throughput: {throughput/ 1e6:.2f} Mbps")

    client.close()

tcpClient("SERVER_IP_HERE", test_type="latency")
