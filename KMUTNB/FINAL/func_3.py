import turtle as t

def olympic():
    r = 50
    distance = 8
    n = 5
    for i in range(n):
        if i == 0:
            t.color('blue')
        elif i == 1:
            t.color('yellow')
        elif i == 2:
            t.color('black')
        elif i == 3:
            t.color('green')
        elif i == 4:
            t.color('red')
        t.pd()
        t.circle(r)
        t.pu()
        if (i % 2) == 0:
            t.sety(t.ycor()-(r))
            t.forward(r)
        else:
            t.sety(t.ycor()+(r))
            t.forward(r+distance)
        # print(i, t.pos())
        t.heading()
    t.goto(0, t.ycor()-r*3)
    # print(t.pos())

t.pu()
t.pensize(4)
t.speed(11)

olympic()
olympic()
olympic()
# print(t.pos())
t.mainloop()