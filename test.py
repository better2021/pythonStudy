name = input('请输入您的名字')
print('hello')

age = 25
if age >= 18:
  print('adult')
else:
  print('teenager')

# sun = 10 
# for i in range(101):
#   sun = sun + i
# print(sun)

def myAbs(x): # def 定义函数
  if x >= 0:
    return x
  else:
    return -x

# print(myAbs(-23.3))

# def power(x):
#   return x*x

# print(power(6))

# L = []
# n = 0
# while n<= 100:
#   L.append(n)
#   n += 2

# print(L)  

# d = {'a': 1, 'b': 2, 'c': 5}
# for key in  d:
#   print(key)

# for value in d.values():
#   print(value)

# for i in 'asdf':
#   print(i)

L = ['HELLO','PYTHON']
lower = [s.lower() for s in L]
print(lower)

def is_odd(n):
  return n%2 == 0

odd = list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))  
print(odd)






