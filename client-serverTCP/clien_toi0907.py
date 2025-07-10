#import 2 thu vien can thiet
import socket
import threading

def receive_messages(client): # hàm nhận tin nhắn
    while True:
        try:
            message = client.recv(1024).decode() # nhận tin nhắn từ server
            if message:
                print("\n" + message) # in ra tin nhắn
        except:
            print("[-] Connection closed by server.")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    print("[*] Connected to server.")
    name = input("ip:")

    # Thread nhận tin nhắn
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        msg = input("nhap tin nhan (exit de thoat):")
        if msg.lower() == 'exit':
            break
        client.send(f"{name}: {msg}".encode())

    client.close()

if __name__ == "__main__":
    start_client()
