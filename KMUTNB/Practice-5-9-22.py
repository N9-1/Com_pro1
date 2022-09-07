'''Problem 1: GPX'''
 
total_point = 0
total_credit = 0

name = input('Name: ')

for i in range(3):
    while True:
        if i == 0:
            grade = input('Sci Grade: ')
        elif i == 1:
            grade = input('Math Grade: ')
        else:
            grade = input('Computer Grade: ')

        if grade == 'A+' or grade == 'A' or grade == 'B+' or grade == 'B' \
            or grade == 'C+' or grade == 'C' or grade == 'D+' or grade == 'D' or grade == 'F':
            break
        else:
            print('Grade must be A+ -> F.')
    while True:
        credit = float(input('Credit: '))
        if credit > 0:
            break
        else:
            print('Credit must be more than 0.')

    if grade == 'A+':
        grade = 4
    elif grade == 'A':
        grade = 3.5
    elif grade == 'B+':
        grade = 3
    elif grade == 'B':
        grade = 2.5
    elif grade == 'C+':
        grade = 2
    elif grade == 'C':
        grade = 1.5
    elif grade == 'D+':
        grade = 1
    elif grade == 'D':
        grade = 0.5
    else:
        grade = 0
   
    total_point += grade * credit
    total_credit += credit

gpx = total_point / total_credit
print(f'Name: {name}')
print(f'GPX: {gpx:6.2f}')

'''Problem 2: welfare'''

name = input('Name: ')

while True:
    salary = eval(input('Salary: '))
    child = int(input('child: '))
    if salary >= 0 or child >= 0:
        break
    else:
        print("Input can't be negative")
 
if salary <= 15000 and child >= 3:
    money = 600
    bonus = ((child-2)/100) * salary
    money += bonus
 
elif salary <= 15000 and child >= 2:
    money = 600
elif salary <= 15000 and child >= 1:
    money = 500
else:
    money = 0
 
print(f'Name: {name}')
print(f'สวัสดิการ: {(money):7.2f} THB/Month')
