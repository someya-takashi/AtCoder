N, M = map(int, input().split())
A = list(map(int, input().split()))

import math
from functools import reduce

# 2つの最小公倍数
def my_lcm_base(x, y):
    if x > M or y > M:
        print(0)
        exit()
    return (x * y) // math.gcd(x, y)

# リストで渡された要素の最小公倍数
def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)

A = [a//2 for a in A]
lcm = my_lcm(*A)

check = 0
for i in range(N):
    num = 0
    temp = A[i]
    while temp % 2 == 0:
        temp //= 2
        num += 1
    if i == 0:
        check = num
    else:
        if check != num:
            print(0)
            exit()

print((M//lcm+1)//2)