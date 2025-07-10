import socket
import threading

client=[]
def XuLyClient (conn,addr):
    print(f"{addr} da truy cap ")
    while True:
        try:
            #he thong nhan tin nhan roi in ra 
            message=conn.recv(1024).decode()
            if not message:
                break
            print (f"{addr}" : {message})

            for client in client:
                if client!=conn:
                    client.send(f"{addr} : {message}".encode())
        except:
            break
     
def run_server ():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',12345))
    server.listen(10)
    print("server dang chay")
    while True:
        conn,addr=server.accept()
        client.append(conn)
        thread=threading.Thread(target=XuLyClient,args=(conn,addr))
        thread.start()

