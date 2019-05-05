import _thread
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
host="127.0.0.1"
port=5000
s.bind((host,port))
s.listen(5)
clients=[]

def connectNewClient(c):
     while True:
        global clients
        msg = c.recv(2048)
        msg ='Client ('+str(clients.index(c)+1)+'):  '+msg.decode('ascii')
        sendToAll(msg,c)
def sendToAll(msg,con):
    for client in clients:
        client.send(msg.encode('ascii')) 
        
while True:
    c,ad=s.accept()
    print('Connection Established')
    clients.append(c)
    c.send(('Client ('+str(clients.index(c)+1)+')').encode('ascii'))
    _thread.start_new_thread(connectNewClient,(c,))