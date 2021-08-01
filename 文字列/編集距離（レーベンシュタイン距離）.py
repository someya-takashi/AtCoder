# https://o-treetree.hatenablog.com/entry/DPL1E

N, M = map(int, input().split())

A = list(input())
B = list(input())

dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = i
for j in range(M+1):
    dp[0][j] = j

for i in range(1, N+1):
    for j in range(1, M+1):
        # 削除の遷移：dp[i-1][j]、コスト = 1
        # 挿入の遷移：dp[i][j-1]、コスト = 1
        # 置換の遷移：do[i-1][j-1]、コスト = 0（A[i] = B[j]のとき）、1（A[i] != B[j]のとき）

        same = 1
        if A[i-1] == B[j-1]:
            same = 0

        dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1] + same)

print(dp[N][M])