# 例題：https://atcoder.jp/contests/abc139/tasks/abc139_e
# ACコード：後で更新

N = int(input())

# Out[i]：頂点iから出た頂点の隣接リスト
Out = [[] for _ in range(N)]


# トポロジカルソートを実行



# トポロジカルソートした頂点配列
topo = [1,2,3,4,5]

# dp[i] : 最後に訪れた頂点がiの時の最長経路
dp = [0] * N

# すべての頂点からスタート
for t in topo:
    # tから行き先があるnxtの距離を更新
    for nxt in Out[t]:
        # 現時点のdpと今回の遷移を比較
        dp[nxt] = max(dp[nxt], dp[t] + 1)

# 0で初期化したので最後に1を足す
print(max(dp)+1)