#PythonDraw.py
import turtle
turtle.setup(1000,600)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor(0.46,0.34,0.76)
turtle.seth(-40)
for i in range(4):
           turtle.circle(50,80)
           turtle.circle(-50,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
