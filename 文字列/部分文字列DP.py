# Sに含まれる文字で元の順序を保ったまま部分文字列を作るとき、wordを作る方法は何通りあるか
# We Love ABC : https://atcoder.jp/contests/abc104/tasks/abc104_d
# chokudai : https://atcoder.jp/contests/abc211/tasks/abc211_c
# ringoさんの解説放送：youtube.com/watch?v=DEGyESFF8iE

S = input()
N = len(S)
mod = 10**9+7

# 0番目はダミー
word = ["", "c", "h", "o", "k", "u", "d", "a", "i"]
W = len(word)

# Sのi番目まででwordのj番目までを作る通り数
dp = [[0] * W for _ in range(N+1)]

# 0番目まででwordの0番目（空文字列）を作る方法は1通り
dp[0][0] = 1

for i in range(1, N+1):
    # i番目の文字を使わない
    # i-1番目と同じ
    for k in range(W):
        dp[i][k] += dp[i-1][k]
        dp[i][k] %= mod

    # 使う
    # (i-1, j-1)から遷移
    for j in range(1, W):
        if S[i-1] == word[j]:
            dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= mod
    
print(dp[N][-1]%mod)