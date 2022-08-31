# assignment4.py

''' Assignment: Grading system '''

score = eval(input("Enter score: "))

# if else
if score >= 90:
    grade = 'A'
else:
    if score >= 85:
        grade = 'B+'
    else:
        if score >= 80:
            grade = 'B'
        else:
            if score >= 75:
                grade = 'C+'
            else:
                if score >= 70:
                    grade = 'C'
                else:
                    if score >= 65:
                        grade = 'D+'
                    else:
                        if score >= 60:
                            grade = 'D'
                        else:
                            grade = 'F'

# if elif
if score >= 90:
    grade = 'A'
elif score >= 85:
    grade = 'B+'
elif score >= 80:
    grade = 'B'
elif score >= 75:
    grade = 'C+'
elif score >= 70:
    grade = 'C'
elif score >= 65:
    grade = 'D+'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)
print("bye..." if score >= 60 else "Don't give up...")

''' Assignment: Area calculator '''

from math import pi

radius = eval(input("Enter Radius: "))

if radius > 0:
    area = pow(radius, 2) * pi
    print("Area is %8.3f" % (area))
    print(f'Area is {area:8.3f}')
    print('Area is {a:8.3f}'.format(a = area))
else:
    print("Invaild Input radius (must > 0)")

''' Assignment: Discount '''


def without_format(n):
    if len((str(n).split('.'))[1]) == 1:
        return str(n)+'0'
    return str(n)


qty, price = [eval(x) for x in input("Enter two values \
(Quality Price) : ").split()]
sumtotal = qty * price
two_per = (2/100)       # ส่วนลด 2%
five_per = (5/100)      # ส่วนลด 5%
eight_per = (8/100)     # ส่วนลด 8%

if sumtotal > 1000:
    discount = sumtotal * eight_per
elif sumtotal > 500:
    discount = sumtotal * five_per
else:
    discount = sumtotal * two_per

net_price = sumtotal - discount
net_price_wf = without_format(round(net_price, 2))
print(f'Net price = {net_price:8.2f}')                          # ใช้ f
print("Net price =", ' '*(8-len(net_price_wf))+net_price_wf)    # ไม่ใช้ f

