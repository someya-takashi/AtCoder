# 計算量 O(VE)
# 最短経路を求める
# 最大コストを求めたい場合はコストに-1をかけて得られたdistを-1倍する

V = int(input())
r = int(input())
G = [[] for _ in range(V)]

# V: グラフの頂点数
# r: 始点
# G[v] = [(w, cost), ...]: 頂点vからコストcostで到達できる頂点w
INF = 10**18
dist = [INF] * V
dist[r] = 0
update = 1
for _ in range(V):
    update = 0
    for v, e in enumerate(G):
        for t, cost in e:
            if dist[v] != INF and dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                update = 1
    if not update:
        break
# for-else: breakをした場合elseに入る
else:
    syori = "kokonikaku"
    # 負閉路検出処理