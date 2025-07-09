import socket
def start():
    sv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sv.bind(("127.0.0.1",65432))
    sv.listen(1)
    print("Server đang lắng nghe tại 127.0.0.1:65432...")
    conn,addr=sv.accept()
    print(f"connected by {addr}")
    while True:
        data=conn.recv(1024)
        if not data:
            break
        print("du lieu nhan dc :",data.decode())
        conn.sendall(data)
    conn.close()
    sv.close()

def udp_sv():
    sv=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sv.bind(('0.0.0.0',9999))
    print ("sv dang chay tren port 9999 ")
    while True:
        data,addr=sv.recvfrom(1024)
        print(f"du lieu nhan dc :{data.decode()} tu {addr}")
        sv.sendto(data,addr)


udp_sv()