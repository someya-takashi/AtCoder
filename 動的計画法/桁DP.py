# https://atcoder.jp/contests/tdpc/tasks/tdpc_number
# https://algo-logic.info/digit-dp/

D = int(input())
N = input()
mod = 10**9+7

# dp[i][j][smaller] : i桁目まで見てmodがjになる数
# 最終的にN桁目まで見てmodが0になる数、dp[N][0][0]とdp[N][0][1]から0を引いた数が答えになる
dp = [[[0] * 2 for _ in range(D)] for _ in range(len(N)+1)]

dp[0][0][0] = 1

for i in range(len(N)):
    for j in range(D):
        for k in range(10):
            # i桁目まででNより小さいならi+1桁目は何でも良い
            dp[i+1][(j + k) % D][1] += dp[i][j][1]
            dp[i+1][(j + k) % D][1] %= mod

        ni = int(N[i])

        for k in range(ni):
            # i桁目まででNと同じで、i+1桁目はNより小さい数のとき
            dp[i+1][(j + k) % D][1] += dp[i][j][0]
            dp[i+1][(j + k) % D][1] %= mod

        # i桁目まででNと同じで、i+1桁目もNと同じ数のとき
        dp[i+1][(j + ni) % D][0] += dp[i][j][0]


print((dp[len(N)][0][0] + dp[len(N)][0][1] - 1)%mod)