import turtle as t
from math import ceil

def diamond(times):
    row = ceil(times/4)
    col = 4
    size = 50
    distance = 30+size
    for i in range(row):
        for j in range(col):
            t.lt(45)
            t.pd()
            for k in range(4):
                t.forward(size)
                t.lt(90)
            t.lt(-45)
            t.pu()
            t.forward(distance)
        if i == row-2:
            col -= (col*row)-times
        t.goto(0, t.ycor()-(distance))

        

t.pu()
t.pensize(4)
t.speed(11)
n = 10
diamond(n)
# diamond(n)


t.mainloop()