
import socket  # 导入 socket 模块
s = socket.socket() # 创建socket对象
host = socket.gethostname() # 获取本地主机名
port = 8088 # 设置端口号
s.bind((host,port)) #  绑定host及端口

s.listen(5) #等待客户端连接
while True:
  title = b'hello python haha' # 发送消息时要在数据前加b,强制转换
  c,addr = s.accept() # 建立客户端连接
  print('连接地址：' ,addr)
  c.send(title)
  c.close() #关闭连接

