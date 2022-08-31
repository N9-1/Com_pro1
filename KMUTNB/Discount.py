# Discount.py

''' Assignment: Discount '''

qty, price = [eval(x) for x in input("Enter two values \
(Quality Price) : ").split()]
sumtotal = qty * price
two_per = (2/100)   # ส่วนลด 2%
five_per = (5/100)  # ส่วนลด 5%
eight_per = (8/100) # ส่วนลด 8%
if sumtotal > 1000:
    discount = sumtotal * eight_per
elif sumtotal > 500:
    discount = sumtotal * five_per
else:
    discount = sumtotal * two_per
net_price = sumtotal - discount
net_price_f = '{0:8.2f}'.format(net_price)
print(f'Net price = {net_price_f}') # ใช้ f
print("Net price =", net_price_f)   # ไม่ใช้ f
