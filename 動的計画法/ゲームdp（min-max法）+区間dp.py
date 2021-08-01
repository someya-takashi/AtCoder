# https://qiita.com/drken/items/4e1bcf8413af16cb62da
# https://atcoder.jp/contests/dp/tasks/dp_l

N = int(input())
A = list(map(int, input().split()))
INF = 10**10

dp = [[0] * (N+1) for _ in range(N+1)]

for l in range(1, N+1):
    for i in range(N-l+1):
        j = i + l

        if (N-l) % 2 == 0:
            dp[i][j] = max(dp[i+1][j] + A[i], dp[i][j-1] + A[j-1])
        else:
            dp[i][j] = min(dp[i+1][j] - A[i], dp[i][j-1] - A[j-1])


print(dp[0][N])
