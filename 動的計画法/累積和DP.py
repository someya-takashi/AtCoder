# https://atcoder.jp/contests/abc183/tasks/abc183_e
# Queen on Grid
# 右、下、右下に移動可能なクイーンの駒が1,1からH,Wに辿り着くまで何通りの移動経路があるかを求める問題
# 今いるマスの左、上、左上からの遷移があるが、全ての遷移元の移動組み合わせを毎回合計しているとTLEになる
# そこで、今いるマスのすぐ左(j-1)、すぐ上(i-1)、すぐ左上(i-1, jh-1)にそれ以前の累積和を保持しておき、
# O(1)で求める。そして今いるマスの累積和を更新する

H, W = map(int, input().split())
maze = []
mod = 10**9+7

for i in range(H):
    s = list(input())
    maze.append(s)

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

# (i, j)の左から遷移可能な数の累積和
X = [[0] * W for _ in range(H)]
# (i, j)の上から遷移可能な数の累積和
Y = [[0] * W for _ in range(H)]
# (i, j)の左上から遷移可能な数の累積和
Z = [[0] * W for _ in range(H)]

X[0][0], Y[0][0], Z[0][0] = 0, 0, 0

for i in range(H):
    for j in range(W):
        if maze[i][j] == "#":
            continue
        if i == 0 and j == 0:
            continue
        if 0 <= j-1 and maze[i][j-1] != "#":
            dp[i][j] += dp[i][j-1] + X[i][j-1]
            X[i][j] = X[i][j-1] + dp[i][j-1]
        if 0 <= i-1 and maze[i-1][j] != "#":
            dp[i][j] += dp[i-1][j] + Y[i-1][j]
            Y[i][j] = Y[i-1][j] + dp[i-1][j]
        if 0 <= j-1 and 0 <= i-1 and maze[i-1][j-1] != "#":
            dp[i][j] += dp[i-1][j-1] + Z[i-1][j-1]
            Z[i][j] = Z[i-1][j-1] + dp[i-1][j-1]

        dp[i][j] %= mod
        X[i][j] %= mod
        Y[i][j] %= mod
        Z[i][j] %= mod
    

print(dp[H-1][W-1] % mod)

