import turtle as t
import random as r

def square():
    distance_x = r.randrange(-200,200,20)
    distance_y = r.randrange(-200,200,20)
    size = r.randrange(60,300,30)
    t.pd()
    for i in range(4):
        t.forward(size)
        t.lt(90)
    t.pu()
    t.goto(distance_x, distance_y)


t.pu()
t.speed(11)
t.pensize(4)

n = 6

for i in range(n):  
    square()


t.mainloop()