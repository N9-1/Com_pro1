import turtle as t

def diamond(row, col):
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
        t.goto(0, t.ycor()-(distance))

        

t.pu()
t.pensize(4)
t.speed(11)
row = 2
col = 4
diamond(row, col)
row = 3
col = 2
diamond(row, col)


t.mainloop()