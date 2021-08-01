A = list(input())
B = list(input())

dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            # Aのi文字目とBのj文字目が同じとき
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 異なる場合は左(j-1)か上(i-1)の大きいほうを引き継ぐ
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(A)][len(B)])