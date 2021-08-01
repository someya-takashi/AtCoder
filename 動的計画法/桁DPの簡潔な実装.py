# https://opt-cp.com/digit-dp-implementation/

# 問題：https://atcoder.jp/contests/abc154/tasks/abc154_e
# 「配る DP」で書く
# 「遷移前の状態」「状態遷移」「遷移後の状態」を変数で管理し，遷移前の状態と状態遷移の列挙を全て for 文に任せる
#  for 文の中では，まず遷移後の状態を表す変数を遷移前の状態で初期化し，必要に応じて遷移後の状態を書き換える
# 不要な遷移は continue で抜ける

N = input()
K = int(input())

n = len(N)

dp = [[[0] * 2 for _ in range(K+1)] for _ in range(n+1)]
dp[0][0][0] = 1

for i in range(n):
    # Nの上からi桁目の数
    ni = int(N[i])
    for j in range(K+1):
        for k in range(2):
            for x in range(10):
                # 遷移後の状態を表す変数j2, k2を遷移前の状態で初期化
                j2 = j
                k2 = k

                # xの上からi桁目の数字xが非ゼロならj2を更新
                if x != 0:
                    j2 += 1
                # 非ゼロの桁がKより多いなら無視
                if j2 > K:
                    continue

                
                # xがNより多いことが確定したら無視
                if k == 0 and x > ni:
                    continue
                # xがNより小さいことが確定したらk2を更新
                if x < ni:
                    k2 = 1
                
                # 遷移式
                dp[i+1][j2][k2] += dp[i][j][k]

print(dp[n][K][0] + dp[n][K][1])