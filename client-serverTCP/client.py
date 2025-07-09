import socket
import time

def client():
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect(("127.0.0.1", 65432))
    while True:
        msg = input("Nhập tin nhắn (hoặc 'exit' để thoát): ")
        if msg.lower() == "exit":
            break;
        cli.sendall(msg.encode())  
        data = cli.recv(1024)     
        print("Server gửi lại:", data.decode())
    cli.close()


def udp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', 9999)
    while True:
        start = time.time()
        message = str(start).encode()
        client.sendto(message, server_address)
        try:
            client.settimeout(1)
            data, _ = client.recvfrom(1024)
            end = time.time()
            rtt = (end - start) * 1000  # ms
            print(f"phanhoi: {rtt:.2f} ms")
        except socket.timeout:
            print("Timeout: không nhận được phản hồi.")
        time.sleep(1)  # Gửi mỗi 1 giây
udp_client()
