def cal(i, j, k):
    i = i**2
    j += 100
    k -= 50
    return i, j, k

i, j, k = 2, 4, 6
i, j, k = cal(i, j, k)
print(f'i = {i}\nj = {j}\nk = {k}')
