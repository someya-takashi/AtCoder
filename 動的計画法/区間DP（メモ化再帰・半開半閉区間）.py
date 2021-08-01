N = int(input())
A = list(map(int, input().split()))

dp = [[-1] * (N+1) for _ in range(N+1)]

def dfs(l, r):
    if dp[l][r] != -1:
        return dp[l][r]
    if l == r-1 or l > r-1:
        return 0
    
    res = 0
    if abs(A[l] - A[r-1]) <= 1 and dfs(l+1, r-1) == r - l -2:
        res = r - l
    
    for mid in range(l+1, r):
        res = max(res, dfs(l, mid) + dfs(mid, r))
    
    dp[l][r] = res
    return res

print(dfs(0, N))