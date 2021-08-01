# DAGのトポロジカルソート
# AOJ : https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B&lang=jp
# けんちょん：https://qiita.com/drken/items/23a4f604fa3f505dd5ad

import sys
sys.setrecursionlimit(10000000)

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    s, t = map(int, input().split())
    graph[s].append(t)

# 訪問済みを記録
seen = [False] * N
# 再帰関数を抜けた順に頂点を格納
order = []

def dfs(n):
    seen[n] = True
    for c in graph[n]:
        if seen[c]:
            continue
        dfs(c)

    # 抜け駆けに頂点を追加
    order.append(n)

# 未到達の頂点についてdfsを行う
for i in range(N):
    if seen[i]:
        continue
    dfs(i)

# この配列の逆順がトポロジカルソート（の一例、トポロジカルソートは複数存在し一意に決まらない）
order = order[::-1]

for i in range(N):
    print(order[i])