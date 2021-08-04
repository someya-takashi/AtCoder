# テクニック集：https://qiita.com/c-yan/items/dbf2838cdd89864ef5ac
# 目次
# 高速入力
# min, maxよりif文を使う
# ダイクストラ、heapでタプル使ったら早くなった
# メモ化再帰のlru_cache


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


print("メモ化再帰のlcu_cache")
# memo配列で結果をメモ化するより、lcu_cacheで関数の引数の結果をキャッシュするほうが早いかも
# 例：memo配列（TLE）：https://atcoder.jp/contests/abc195/submissions/24743427
# 例：lcu_cache（AC）：https://atcoder.jp/contests/abc195/submissions/24743471
# 上記ではmemo配列を使うとTLEになった（WAもあったので、単にmemo配列でのメモ化でミスしている可能性もある）