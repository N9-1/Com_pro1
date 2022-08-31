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

''' Assignment: Calculate area (side area) of a Cylinder '''

from math import pi

while True:
    rad, h = eval(input('Enter radius, height: '))
    if rad > 0.5 and h > 0.5:
        break
    else:
        print(f'radius and height must more than 0.5')
curved_area = 2 * pi * rad * h
print(f'The curved surface area \
of a cylinder is {curved_area:.2f}cm^2')

''' Assignment: welfare benefit (>= 60 years old) '''

while True:
    age = eval(input('Enter age: '))
    if age >= 60:
        break
    else:
        print(f'Age must greater than or equal to 60')

if age >= 81:
    money_add = 1000
elif age >= 76:
    money_add = 900
elif age >= 71:
    money_add = 800
elif age >= 66:
    money_add = 600
else:
    money_add = 500
print(f'You will receive a welfare payment of {money_add} THB/Month')
