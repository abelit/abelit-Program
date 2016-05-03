# from socket import *

# # 建立三个客户端，分别连接三个不同的服务端程序, 接收服务端传过来的数据并打印
# # 这三个客户端是阻塞方式通信的
# if __name__ == '__main__':
# 	ports = [10000, 10001, 10002]
# 	for port in ports:
# 		address = ('127.0.0.1', port)
# 		sock = socket(AF_INET, SOCK_STREAM)
# 		sock.connect(address)
# 		poem = ''
# 		while True:
# 			data = sock.recv(4)
# 			if not data:
# 				sock.close()
# 				break
# 			poem += data.decode('utf8')
# 		print(poem)
# 		sock.close()


import datetime, errno, optparse, select, socket

def connect(port):
	"""Connect to the given server and return a non-blocking socket."""
	address = ('127.0.0.1', port)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(address)
	sock.setblocking(0)		# 设置为非阻塞模式
	return sock

def format_address(address):
	host, port = address
	return '%s:%s' % (host or '127.0.0.1', port)

if __name__ == '__main__':
	ports = [10000, 10001, 10002]
	start = datetime.datetime.now()

	sockets = list(map(connect, ports))
	poems = dict.fromkeys(sockets, '') # socket -> accumulated poem
	sock2task = dict([(s, i + 1) for i, s in enumerate(sockets)])

	while sockets:
		#运用select来确保那些可读取的异步socket可以立即开始读取IO
		#OS不停的搜索目前可以read的socket，有的话就返回rlist
		rlist, _, _ = select.select(sockets, [], [])
		for sock in rlist:
			data = ''
			while True:
				try:
					new_data = sock.recv(1024)
					new_data = new_data.decode('utf8')
				except socket.error as e:
					if e.args[0] == errno.EWOULDBLOCK:
						break
					raise
				else:
					if not new_data:
						break
					else:
						print(new_data)
						data += new_data

			task_num = sock2task[sock]
			if not data:
				print(poems[sock])	# 打印sock接收到的数据
				sockets.remove(sock)
				sock.close()
				print('Task %d finished\n' % task_num)
			else:
				addr_fmt = format_address(sock.getpeername())
				msg = 'Task %d: got %d bytes of poetry from %s\n'
				print(msg % (task_num, len(data), addr_fmt))

			poems[sock] += data		# 保存每个sock接收到的数据

	elapsed = datetime.datetime.now() - start
	print('Got poems in %s' %elapsed)
