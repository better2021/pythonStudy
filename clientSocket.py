
import socket
client = socket.socket()
host = socket.gethostname()
port = 8088

client.connect((host,port))  # 连接端口
print('接受来自服务端的消息：',client.recv(1024))
client.close()