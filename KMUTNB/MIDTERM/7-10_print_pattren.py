n = 6
# 7)
print('7)')
for i in range(n):
    for j in range(i+1):
        print(j+1, end='|')
    print()

print('-'*20)
print('8)')
# 8)
for i in range(n):
    for j in range(n-i):
        print(j+1, end='|')
    print()

print('-'*20)
print('9)')
# 9)
for i in range(n):
    print(' '*((n-(i+1))*2), end='')
    for j in range(i+1):
        print(j+1, end='|')
    print()

print('-'*20)
print('10)')
for i in range(n, 0, -1):
    print(' '*((n-i)*2), end='')
    for j in range(i):
        print(j+1, end='|')
    print()

print('-'*20)
print('c) จากหนังสือ')
print('reverse ตัวเลข')
# C
for i in range(n):
    for j in range(n, 0, -1):
        if j-1 > i:
            print(" ", end=' ')
        else:
            print(j, end=' ')
    print()
