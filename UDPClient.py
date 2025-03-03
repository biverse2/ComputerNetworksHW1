import socket
import time

def udp_client(serverIp, port=5001, messageSize=64, testType="latency"):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = b'X' * messageSize

    if type == "latency":
        start = time.time()
        client.sendto(message, (serverIp, port))
        client.recvfrom(messageSize)  
        end = time.time()
        print(f"UDP RTT for {messageSize} bytes: {(end - start) * 1000:.2f} ms")

    elif type == "throughput":
        totalData = 1024 * 1024  
        numMessages = totalData // messageSize
        start = time.time()
        for _ in range(numMessages):
            client.sendto(message, (serverIp, port))
            client.recvfrom(8) 
        end = time.time()
        throughput = (totalData * 8) / (end - start) 
        print(f"UDP Throughput: {throughput / 1e6:.2f} Mbps")

    client.close()

udp_client("SERVER_IP_HERE", type="latency")  
