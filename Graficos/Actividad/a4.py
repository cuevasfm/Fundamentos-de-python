import turtle
import time

#Linea punteada
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()
turtle.forward(10)
time.sleep(1)
for i in range(10):
  turtle.penup()
  turtle.forward(5)
  turtle.pendown()
  turtle.forward(10)
  time.sleep(1)

turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.forward(10)
time.sleep(1)
for i in range(10, 20, 1):
  turtle.penup()
  turtle.forward(5)
  turtle.pendown()
  turtle.forward(10 + i)
  time.sleep(1)

time.sleep(10)