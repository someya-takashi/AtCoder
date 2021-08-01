# https://atcoder.jp/contests/abc153/tasks/abc153_e

H, N = map(int, input().split())

A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[10**10] * (H+1) for _ in range(N+1)]

dp[0][0] = 0

for i in range(1, N+1):
    for j in range(H+1):
        # i番目の魔法を使わない場合の遷移
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        # i番目の魔法を使う遷移
        if dp[i][j] != 10**10:
            if j+A[i-1] < H+1:
                dp[i][j+A[i-1]] = min(dp[i][j+A[i-1]], dp[i][j] + B[i-1])
            # ダメージがH以上をHにまとめる
            else:
                dp[i][H] = min(dp[i][H], dp[i][j] + B[i-1])

print(dp[N][H])