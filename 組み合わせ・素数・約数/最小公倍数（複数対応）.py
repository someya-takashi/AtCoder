# 最大公約数の計算量がlog(max(A))なので、計算量はlen(A)*log(max(A))

import math
from functools import reduce

A = list(map(int, input().split()))

# 2つの最小公倍数
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

# リストで渡された要素の最小公倍数
def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)

ans = my_lcm(*A)