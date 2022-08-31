# assignment5.py

''' Assignment 5: Input Output '''

''' Temp converter '''

Celsius = eval(input("Enter °C : "))
Fahrenheit = Celsius * 9/5 + 32
print('%s °C = %.3f °F' % (Celsius, Fahrenheit))
print('{} °C = {:.3f} °F'.format(Celsius, Fahrenheit))
print(f'{Celsius} °C = {Fahrenheit:.3f} °F')

''' Area '''

w, h = [eval(x) for x in input("Enter two values \
(width height) : ").split()]
area = w * h
perimeter = 2 * (w + h)
print('Area = {} \nPerimter = {}'.format(area, perimeter))
print(f'Area = {area} \nPerimter = {perimeter}')


''' Formula '''

# Equations of Motion
u, a, t = [eval(x) for x in input("Enter three values \
    \n(initial_velocity acceleration time) : ").split()]
v = u + a * t                       # find velocity (u a t)
s = u * t + 1/2 * a * pow(t, 2)     # find displacement (u t a)
v_squared = pow(u, 2) + 2 * a * s   # find velocity squared (u a s)
print(f'Velocity = {v} m/s \nDisplacement = {s} m \
    \nVelocity^2 = {v_squared} m/s')

# Calculate rate of interest
from math import log


a, p, t = [eval(x) for x in input("Enter three values \
    \nTotal Amount (A) \nPrincipal (P) \nTime (t) : ").split()]
r = log(a / p) / t  # Rate
print(f'Interest Rate = {r*100} % per year')
