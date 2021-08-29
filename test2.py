import sys
sys.setrecursionlimit(100000000)

N = int(input())
A = list(map(int, input().split()))

M = N//2

def dfs(n, now, last):
    
    if now < n//2-1 or now > n//2 + 1:
        return -10**18

    if now == M or n == N:
        return 0

    ret = 0
    if not last:
        ret = dfs(n+1, now+1, True) + A[n]
    ret = max(ret, dfs(n+1, now, False))

    return ret
    
print(dfs(0, 0, False))    
