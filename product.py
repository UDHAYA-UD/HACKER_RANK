from itertools import product
n = int(input())
arr = list(map(int, input().split()))
for p in product(arr, repeat=n):
    print(*p)