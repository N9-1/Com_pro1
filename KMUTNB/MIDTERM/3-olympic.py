import turtle as t

t.penup()
t.speed(11)

r = 50
distance = 8
n = 5   # times

t.pensize(4)
t.color('blue')

print('home', t.pos())
count = 1
for i in range(n):
    
    if i == 1:
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
        t.sety(-(r))
        t.forward(r)
    else:
        t.sety(0)
        t.forward(r+distance)
    print(i, t.pos())
    t.heading()
    
t.mainloop()
