from turtle import *
speed(10)
pensize(5)

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def draw_circle(r):
    fd(r)
    rt(90)
    fd(r)
    for i in range(2):
        rt(90)
        fd(r)
    rt(90)
    circle(-r,90)

def draw_degree(n):
    if n == 1:
        r = 10*fibonacci(n)
    else:
        r = 10*fibonacci(n)
        draw_circle(r)
        draw_degree(n-1)

pu()
goto(200,130)
pd()
seth(-90)
draw_degree(10)
hideturtle()
done()
