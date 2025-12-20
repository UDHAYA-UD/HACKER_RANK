from itertools import product
n = int(input())
arr = list(map(int, input().split()))
res = list(product(arr, repeat=n))
for i in res:
    print(*i)
    