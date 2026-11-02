import sys
import socket
from threading import Thread

def usage():
    print("usage: client.py username port", file=sys.stderr)
def inp(s):
    while True:
        data = s.recv(4096)
        print(data.decode())
def out(s,name):
    s.send(name.encode())
    while True:
        data = input(": ")
        s.send(data.encode())
def main(argv):
    try:
        port = int(argv[2])
    except:
        usage()
        return 1
    ip = 'localhost'
    sock = socket.socket()
    sock.connect((ip,port))
    i = Thread(target=inp,args=(sock,),daemon=True)
    o = Thread(target=out,args=(sock,argv[1]),daemon=True)
    i.start()
    o.start()
    i.join()
    o.join()
if __name__ == "__main__":
    sys.exit(main(sys.argv))
