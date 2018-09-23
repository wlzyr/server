#!/usr/bin/python3  

import socket
import threading

def date_analysis(conn,add):
    a = "3"
    date = conn.recv(1024)
    conn.send(a.encode("utf-8"))
    conn.close()

def monitor():
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = "127.0.0.1"
    port = 9999
    sk.bind((ip,port))
    sk.listen(5)
    while True:
        conn,add = sk.accept()
        th = threading.Thread(target=date_analysis,args=(conn,add))
        th.start()

def main():
    monitor()

if __name__ == "__main__":
    main() 