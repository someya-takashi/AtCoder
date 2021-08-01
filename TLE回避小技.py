# テクニック集：https://qiita.com/c-yan/items/dbf2838cdd89864ef5ac
# 目次
# 高速入力
# min, maxよりif文を使う
# ダイクストラ、heapでタプル使ったら早くなった


print("高速入力")
# 10**5個のクエリなど、入力に時間がかかってしまう場合に使うとTLEを防げる
# https://atcoder.jp/contests/typical90/tasks/typical90_bl などで通常のinputではTLEになった

import sys
input = sys.stdin.readline

print("min, maxよりif文を使う")
# ワーシャルフロイドの計算がギリギリの時、下記のような書き換えで2080ms→1810msに改善
# N = 400, O(N**3)
# 上記の提出：https://atcoder.jp/contests/arc035/submissions/23661835

cost = [0][0]
i, k, j = 0

# TLE
cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# 高速化
if cost[i][j] > cost[i][k] + cost[k][j]:
    cost[i][j] = cost[i][k] + cost[k][j]


print("ダイクストラ、heapでタプル使ったら早くなった")
# ダイクストラのheappushをリストからタプルにしただけで半分くらいになった

# tuple : 1022 ms https://atcoder.jp/contests/past202104-open/submissions/me
# list : 2059 ms https://atcoder.jp/contests/past202104-open/submissions/24232601