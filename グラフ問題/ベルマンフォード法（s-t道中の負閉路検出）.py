# Coins Respawn : https://atcoder.jp/contests/abc137/tasks/abc137_e
# s-tにおける最短（今回はスコア最大）経路を求める問題
# s-t道中に負閉路（無限に点数を稼げるループ）がある場合はそれを報告する
# tまで辿りつけない負閉路にハマらないよう、dfsを二回行い一方通行となる頂点を削除する

import sys
sys.setrecursionlimit(100000000)

N, M, P = map(int, input().split())
graph = [[] for _ in range(N)]
# 逆辺を張ったグラフ
r_graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1].append([b-1, c])
    r_graph[b-1].append([a-1, c])

# 頂点1から辿り着けるか
accessible = [False] * N
# 頂点Nから辿り着けるか
r_accessible = [False] * N
accessible[0] = True
r_accessible[N-1] = True

# 始点から順方向にdfs
def dfs(now, par = -1):
    for nxt, c in graph[now]:
        if nxt == par:
            continue
        if not accessible[nxt]:
            accessible[nxt] = True
            dfs(nxt, now)

# 終点から逆辺を使ってdfs
def r_dfs(now, par = -1):
    for nxt, c in r_graph[now]:
        if nxt == par:
            continue
        if not r_accessible[nxt]:
            r_accessible[nxt] = True
            r_dfs(nxt, now)

dfs(0)
r_dfs(N-1)

new_graph = [[] for _ in range(N)]

# 新しいグラフを作成
for i, g in enumerate(graph):
    for to, c in g:
        # 順方向の辺の内、逆方向からも辿り着ける辺を追加
        if accessible[to] and r_accessible[to]:
            # 最短経路問題にするためマイナスで追加
            # 1辺につきPのコストを最後に支払うので、あらかじめPを引いておく
            new_graph[i].append([to, -c+P])

# ベルマンフォード
INF = 10**18
dist = [INF] * N
dist[0] = 0
update = 1
for _ in range(N):
    update = 0
    for v, e in enumerate(new_graph):
        for t, cost in e:
            if dist[v] != INF and dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                update = 1
    if not update:
        break
# 道中に閉路がある場合
else:
    print(-1)
    exit()

print(max(0, -dist[N-1]))
