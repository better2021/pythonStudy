from turtle import *

print('start draw star')
color('pink', 'red')
def drawStar(x,y):
  pu()
  goto(x,y)
  pd()
  seth(0)
  for i in range(5): 
    fd(40)
    rt(144)

for x in range(0,250,50):
  drawStar(x,0)

done()     