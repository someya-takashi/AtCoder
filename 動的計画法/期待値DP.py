# https://atcoder.jp/contests/abc184/tasks/abc184_d

A, B, C = map(int, input().split())

import sys 
sys.setrecursionlimit(1000000)

def dfs(a, b, c):
    if dp[a][b][c] >= 0:
        return dp[a][b][c]
    else:
        ret = 0
        S = a + b + c
        ret += a / S * (dfs(a+1, b, c) + 1)
        ret += b / S * (dfs(a, b+1, c) + 1)
        ret += c / S * (dfs(a, b, c+1) + 1)
        dp[a][b][c] = ret
    
    return ret


dp = [[[-1] * 101 for _ in range(101)] for _ in range(101)]

for i in range(101):
    for j in range(101):
        for k in range(101):
            if i == 100 or j == 100 or k == 100:
                dp[i][j][k] = 0


print(dfs(A, B, C))