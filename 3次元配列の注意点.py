H, W = map(int, input().split())

# H <= 3000, W <= 3000 のような制約でk=4と(H, W, k)の3次元配列を作る場合
# 該当の問題：https://atcoder.jp/contests/abc175/tasks/abc175_e

# ダメな例： 3348 ms	1071780 KB
dp = [[[-10**10] * 4 for _ in range(W)] for _ in range(H)]

# OKな例： 2602 ms	428984 KB
dp = [[[-10**10] * W for _ in range(H)] for _ in range(4)]

# 小さい変数は一番外側に書かないと何故か遅い

"""
dp[i][j][k]の代わりにdp = defaultdict(lambda: -10**18)として
キーにタプルで(i, j, k)のように状態管理することも可能 
"""