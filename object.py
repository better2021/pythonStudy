
# -*- coding: UTF-8 -*-

class Employee:
  empCount = 0
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1

  def displayCount(self):
    print(Employee.empCount)

  def displayEmplotee(self):
    print('name:',self.name,',salary:',self.salary)

# 创建 Employee 类的第一个对象
emp1 = Employee('zara',1500)
# 创建 Employee 类的第二个对象
emp2 = Employee('xiaoming',2000)

emp1.displayEmplotee()
emp2.displayEmplotee()
emp1.displayCount()

print(hasattr(emp1,'age')) # 检查是否存在一个属性
print(setattr(emp1,'age',18)) # 添加属性age的值为18
print(getattr(emp1,'age')) # 获取age属性的值
# delattr(emp1,'age') # 删除属性age
print(emp1.age)



# python的正则表达式
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
import re
print(re.match('www','www.baidu.com').span())
print(re.match('awww','www.baidu.com'))

# re.search 扫描整个字符串并返回第一个成功的匹配。
# 匹配成功re.search方法返回一个匹配的对象，否则返回None
print(re.search('com','www.baidu.com').span())

# Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
phone = '2004-959-559'
num = re.sub(r'\D','',phone) # 删除非数字（-）的字符串
print('电话号码为：',num)  

pattern = re.compile(r'\d+') # 查找数字
result = pattern.findall('opp 12 good 258')
print(result)  
