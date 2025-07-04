import turtle
import time

time.sleep(3)
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
for i in range(3):
  turtle.forward(80)
  turtle.left(120)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

for i in range(4):
  turtle.forward(100)
  turtle.left(90)

turtle.penup()
turtle.goto(300,0)
turtle.pendown()

for i in range(5):
  turtle.forward(120)
  turtle.left(72)

time.sleep(10)