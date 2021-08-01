# https://atcoder.jp/contests/abc029/tasks/abc029_d
# https://algo-logic.info/digit-dp/
# Nまでの整数で1が何個登場するか

N = input()

dp = [[[0] * (len(N)+1) for _ in range(2)] for _ in range(len(N)+1)]
dp[0][0][0] = 1

for i in range(len(N)):
    for j in range(len(N)):

        # i桁目まででNより小さいならi+1桁目は0-9まで使える
        dp[i+1][1][j] += dp[i][1][j] * 9 # i+1桁目が1以外
        dp[i+1][1][j+1] += dp[i][1][j]   # i+1桁目が1

        # i+1桁目の上限
        ni = int(N[i])
        
        # i桁目までNと同じ（smaller=False）でi+1桁目はNより小さい数(smaller=True）の時
        # ni = 6なら6より小さい0から5の1以外と1の計ni個使える
        if ni > 1:
            dp[i+1][1][j] += dp[i][0][j] * (ni-1) #i+1桁目が0~ni-1の1以外
            dp[i+1][1][j+1] += dp[i][0][j] # i+1桁目が1の時
        # niが1なら1より小さい0のみ使える
        elif ni == 1:
            dp[i+1][1][j] += dp[i][0][j]

        # i桁目までNと同じ、i+1桁目もNと同じ
        # i桁目が1ならjを1増やし、1以外ならそのまま
        if ni == 1:
            dp[i+1][0][j+1] += dp[i][0][j]
        else:
            dp[i+1][0][j] += dp[i][0][j]

ans = 0
for i in range(1, len(N)+1):
    ans += (dp[len(N)][1][i] + dp[len(N)][0][i]) * i

print(ans)