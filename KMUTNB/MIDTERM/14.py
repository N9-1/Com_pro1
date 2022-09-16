while True:
    n = int(input())
    if n > 30:
        break
    else:
        print('n > 30')

print(n)
while n > 10:
    n = n - 3
    print(n)