import turtle as t

t.penup()
t.speed(11)

side = 6
distance = 50
n = 3   # times
angle = 360/side
pole = distance*2

t.pensize(8)

for i in range(n):

    t.color('blue')
    t.begin_fill()

    for j in range(side):
        t.pd()
        t.forward(distance)
        t.left(angle)
    t.end_fill()

    # pole
    t.setx(t.xcor()+distance/2)
    t.left(-90)
    t.forward(pole)
    t.pu()
    # text
    t.setheading(0)
    t.sety(distance/2)
    t.color('white')
    t.write("STOP", False, align="center", font=('Arial', 18, 'normal'))
    # reset
    t.sety(0)
    t.forward(distance*2)

t.mainloop()