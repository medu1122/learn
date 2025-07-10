# im port 2 thu vien can thiet
import socket
import threading # chạy đa luồng , tức là 2 cleant chạy


# tao lisst chua client
clients = [] # danh sách client
# ham xu ly client bao gom :print dia chi da kn , chay vong lap nhan tin nhan , gui tin nhan den client khac
def handle_client(conn, addr): # hàm xử lý client
    print(f"[+] {addr} connected.") # in ra địa chỉ của client đã kết nối
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"[{addr}] {message}")
            # Gửi message đến client khác
            for client in clients: # duyet qua tung client khac roi gui tin nhan
                if client != conn:
                    client.send(f"[{addr}] {message}".encode())
        except:
            break

    conn.close()
    clients.remove(conn)
    print(f"[-] {addr} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(10) #open ket noi và max so luong 
    print("[*] Server is listening...")
    while True:
        conn, addr = server.accept() # accept la ham de chap nhan ket noi tu client
        clients.append(conn) # them client vao danh sach
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # tao thread de xu ly client . trong đó target là chức năng của thread , args là tham số truyền vào hàm handle_client
        thread.start()

if __name__ == "__main__":
    start_server()
