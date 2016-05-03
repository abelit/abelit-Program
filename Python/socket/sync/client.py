# if __name__=='__main__':
# 	import socket
# 	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 	sock.connect(('localhost',8080))
# 	import time
# 	time.sleep(2)
# 	sock.send('1')
# 	print(sock,recv(1024))
# 	sock.close()
# import socket  

# HOST='localhost'  
# PORT=8080
# BUFFER=4096  

# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
# sock.connect((HOST,PORT))  
# sock.send('hello, tcpServer!')  
# recv=sock.recv(BUFFER)  
# print('[tcpServer said]: %s' % recv)  
# sock.close() 

# import socket

# serverHost = 'localhost'
# serverPort = 50014

# sockobj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sockobj.connect((serverHost,serverPort))
# sockobj.send('Hello,Server')
# print(sockobj.recv(1024))
# sockobj.close()

from socket import *  
  
HOST = 'localhost'  
PORT = 21567  
BUFSIZE = 1024  
ADDR = (HOST, PORT)  
  
tcpCliSock = socket(AF_INET, SOCK_STREAM)  
tcpCliSock.connect(ADDR)  
  
while True:  
    data = input('>')  
    if not data:  
        continue  
    print('input data: [%s]' %data)  
    tcpCliSock.send(data.encode('utf8'))  
    rdata = tcpCliSock.recv(BUFSIZE)  
    if not rdata:  
        break  
    print(rdata.decode('utf8'))  
    if data == 'bye' or data == 'shutdown':  
        break  
  
tcpCliSock.close()  