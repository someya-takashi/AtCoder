# PAST 的あて　https://atcoder.jp/contests/past202012-open/tasks/past202012_k
# 制約が HW = 16 と小さい -> bit全探索？
# 的が複数の場合から考えると考察が複雑になるので、的が0や1の部分問題から
# 入力の初期配置の状態まで辿れないかを考える
# 一つ前の状態への遷移を漸化式で表せないか
# 的の狙い方が自由 -> 最適な的の狙い方を考えるといろいろと場合分けが必要そうでバグる
# 的の狙い方は高々16通りしかないので、全探索をしよう、という思考ができるようにする

S = [input() for _ in range(4)]
ans = 0
for i in range(4):
    for j in range(4):
        if S[i][j] == "#":
            target_num = 4*i+j
            ans += 1 << target_num

ALL = 1 << 16
dp = [10**10] * ALL
dp[0] = 0

# すべてのdpをiが小さい順に更新していく
for i in range(1, ALL):
    # 狙い位置jを全探索
    for j in range(16):
        # kの役割については下記参照
        k = 5
        success = 0
        if i & 1 <<j:
            success += dp[i-(1<<j)]
        else:
            k-=1
        if j >=4 and i & 1 << (j-4):
            success += dp[i-(1<<(j-4))]
        else:
            k-=1
        if j+4 < 16 and i & 1 << (j+4):
            success += dp[i-(1<<(j+4))]
        else:
            k-=1
        if (j+1)%4 != 0 and i & 1 << (j+1):
            success += dp[i-(1<<(j+1))]
        else:
            k-=1
        if j%4 != 0 and i & 1 <<(j-1):
            success += dp[i-(1<<(j-1))]
        else:
            k-=1

        if k > 0:
            # 例：下と右に的がない場合のdp遷移
            # dp[i] = 1 + dp[i-中]/5 + dp[i-上]/5 + dp[i-左]/5 + dp[i]/5 + dp[i]/5
            # 5をかけて両辺のdp[i]をまとめる
            # dp[i] = (5+dp[i-中]+dp[i-上]+dp[i-左])/3
            # 分母の3は5-的がない場所の個数、よって下式のようなdp遷移となる
            # これをすべての狙い位置jで計算し、minになるjが最適な狙い位置
            dp[i] = min(dp[i], (success+5)/k)

print(dp[ans])