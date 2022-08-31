''' Assignment: Square using While '''

import turtle as tt


def clear():
    tt.clear()
    tt.setpos(-180, 0)

tt.penup()
tt.setpos(-180, 0)
tt.speed(20)

distance = 90
leg = 60
n = 4   # square times

tt.pensize(4)
tt.color('red', 'yellow')

# while while
count = 0
while count < n:
    tt.pendown()
    tt.begin_fill()
    tt.forward(leg)
    i = 0

    while i < 3:
        tt.left(90)
        tt.forward(leg)
        i += 1
    tt.penup()
    tt.end_fill()
    tt.setheading(0)
    tt.forward(distance)
    count += 1
clear()

# while for
count = 0
while count < n:
    tt.pendown()
    tt.begin_fill()
    tt.forward(leg)

    for j in range(3):
        tt.left(90)
        tt.forward(leg)
    tt.penup()
    tt.end_fill()
    tt.setheading(0)
    tt.forward(distance)
    count += 1
clear()

# for while
for i in range(n):
    tt.pendown()
    tt.begin_fill()
    tt.forward(leg)
    i = 0

    while i < 3:
        tt.left(90)
        tt.forward(leg)
        i += 1
    tt.penup()
    tt.end_fill()
    tt.setheading(0)
    tt.forward(distance)

tt.mainloop()