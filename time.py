# coding=utf-8
import time
import calendar
import os

ticks = time.time()
local = time.localtime(ticks)
print(ticks)
print(local)
print(time.asctime(local))
# 格式化为2019-03-20 11:54:30 的格式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# 输出日历
cal = calendar.month(2019,1)
print(cal)

# 判断闰年，闰年返回true，否则返回false
print(calendar.isleap(2000))
print(calendar.isleap(1900))

# 定义函数
def sum(arg1,arg2):
  total = arg1 + arg2
  print('相加的和为：' , total)
  return total;

# 调用函数
sum(10,50)

# 打开文件
fo = open('foo.txt','w',encoding='utf-8')
print(fo.name)
fo.write('www.baidu.com\n very good!\n 哈哈哈哈')

# fo = open('foo.txt','r+')  
# str = fo.read()
# print('读取的字符串为：',str)

# 关闭打开的文件
# fo.close()

# 重命名文件foo.txt为test.txt
# os.rename('foo.txt','text.txt')

# 删除一个已经存在的文件
# os.remove('text.txt')

# 创建目录 view
# os.mkdir('view')

# 获取当前的工作目录
print(os.getcwd())

# 删除view目录
# os.rmdir('view')

# 输出python的每个字母
for letter in 'Python':
  print('当前字母：',letter)



import re
str = '陈奕迅演唱(不要说话)'
print(re.findall('\((.*?)\)', str)[0],'----------')