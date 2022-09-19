def allSum(num):
    cal = 0
    for i in num:
        cal += i
    return cal 

n = 5
lst = []
for i in range(n):
    ele = int(input(f'{i+1}: '))
    lst.append(ele)

print(f'Sum = {allSum(lst)}')
