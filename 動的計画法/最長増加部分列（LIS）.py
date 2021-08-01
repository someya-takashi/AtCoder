# https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5

N = int(input())
A = [int(input()) for _ in range(N)]

# dpの長さが最長増加部分列の長さ
dp = [10**10]

import bisect

for i in range(N):
    a = A[i]
    # i番目の数字がこれまでの部分列の末尾の数より小さい場合、部分列に追加できる
    if a > dp[-1]:
        dp.append(a)
    # 末尾に追加できなくてもそれまでの部分列でより小さい部分列を作れる場合は更新
    # 部分列はソート列なので、更新場所は二分探索で高速に求めることができる
    else:
        dp[bisect.bisect_left(dp, a)] = a

# dpの長さが最長増加部分列の長さ
print(len(dp))