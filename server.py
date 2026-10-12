import sys
import socket
import select

def delete(socket,dick):
    for i in list(dick):
        if socket is dick[i]["socket"]:
            del dick[i]
            break
    return None

def broadcast(data,sockets,server_socket):
    for s in sockets:
        if s is not server_socket:
            s.sendall(data.encode())
def look_name(socket,dick):
    for i in dick:
        if socket==dick[i]["socket"]:
            name = dick[i]["name"]
            return name
    return None
def run_server(port):
    server_socket = socket.socket()
    server_socket.bind(('localhost',port))
    server_socket.listen(5)
    listen_sockets = [server_socket]
    client_dict = {}
    i = 0
    while(True):
        sel , _, _ = select.select(listen_sockets,[],[])
        for s in sel:
            if s is server_socket:
                client_socket , addr = server_socket.accept()
                new_ninja = client_socket.getpeername()
                name = client_socket.recv(256).decode()
                client_dict[i] = {"socket" : client_socket , 'name' : name}
                i+=1
                print(f"New Connection from : {name}")
                d = (f"New Connection from : {name}")
                broadcast(d,listen_sockets,server_socket)
                listen_sockets.append(client_socket)
            else:
                name = look_name(s,client_dict)
                data = s.recv(4096)
                if data:
                    d =(f"{name} :{data.decode()}")
                    print(d)
                    broadcast(d,listen_sockets,server_socket)
                else:    
                    d = (f"{name} : Disconnected")
                    print(d)
                    delete(s,client_dict)
                    broadcast(d,listen_sockets,server_socket)
                    s.close()
                    listen_sockets.remove(s)
                   
                    
def usage():
    print("usage: server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
