n = 5

num = int(input())
min_num = num
max_num = num

for i in range(n-1):
    num = int(input())
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
    
print(max_num, min_num)