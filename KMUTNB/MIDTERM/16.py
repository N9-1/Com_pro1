num = int(input())
num_p = "is a prime number"

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            num_p = "is not a prime number"
            break
        else:
            num_p = "is a prime number"
    print(num ,num_p)
else:
    print(num,"is not a prime number")
