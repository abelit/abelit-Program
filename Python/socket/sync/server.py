# if __name__=='__main__':
# 	import socket
# 	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 	sock.bind(('localhost',8080))
# 	sock.listen(5)
# 	while True:
# 		connection,address=sock.accept()
# 		try:
# 			connection.settimeout(5)
# 			buf=connection.recv(1024)
# 			if buf=='1':
# 				connection.send('Welcome to server!')
# 			else:
# 				connection.send('Please go out!')
# 		except socket.timeout:
# 			print('time out')
# 		connection.close()
# import socket
# HOST='localhost'
# PORT=8080
# BUFFER=4096

# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind((HOST,PORT))
# sock.listen(0)
# print('tcpServer listen at: %s:%s\n\r' %(HOST,PORT))
# while True:
# 	client_sock,client_addr=sock.accept()
# 	print('%s:%s connect' %client_addr)
# 	while True:
# 		recv=client_sock.recv(BUFFER)
# 		if not recv:
# 			client_sock.close()
# 			break
# 		print('[Client %s:%s said]:%s' % (client_addr[0],client_addr[1],recv))
# 		client_sock.send('tcpServer has received your message')
# 	sock.close()

# import socket

# myHost = 'localhost'
# myPort = 50014
# sockobj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sockobj.bind((myHost,myPort))
# sockobj.listen(5)

# while True:
#   print('I am listenning')
#   conn, addr = sockobj.accept()
#   print("Connected By:" ,addr)
#   try:
#     conn.settimeout(5)
#     data = conn.recv(1024)
#     if not data:break
#     conn.send('Echo=>' + data)
#   except socket.timeout:
#     print('Time Out')
#   conn.close()

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
quit = False
shutdown = False

while True:
	print('waiting for connection...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('...connected from: ', addr)

	while True:
		data = tcpCliSock.recv(BUFSIZE)
		data = data.decode('utf8')
		if not data:
			break
		ss = '[%s] %s' %(ctime(), data)
		tcpCliSock.send(ss.encode('utf8'))
		print(ss)
		if data == 'bye':
			quit = True
			break
		elif data == 'shutdown':
			shutdown = True
			break
	print('Bye-bye: [%s: %d]' %(addr[0], addr[1]))
	tcpCliSock.close()

	if shutdown:
		break
tcpSerSock.close()
print('Server has been stoped')