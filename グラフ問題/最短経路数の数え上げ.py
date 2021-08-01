# N頂点、M個の無向辺
# 有向グラフの場合は隣接リストを書き換えて使う
# 辺のコストは1
# コストが1以上の場合はBFS部分をダイクストラに書き換えて使う
# 頂点1からNまでの最短経路の個数を求める
N, M = map(int, input().split())
mod = 10**9+7
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# BFS部分
from collections import deque
Q = deque()
Q.append(0)
dist = [10**10] * N
# 最短経路の個数を管理する配列
num = [0] * N
dist[0] = 0
num[0] = 1

while Q:
    now = Q.popleft()

    for nxt in graph[now]:
        if nxt == now:
            continue
        # キューへの追加と個数の更新
        if dist[now] +1 < dist[nxt]:
            dist[nxt] = dist[now] + 1
            # 次頂点の経路数としてこれまでの経路数を代入
            num[nxt] = num[now]
            Q.append(nxt)
        # 距離が同じで行ける別のパスがある場合、その経路数を加算
        elif dist[now] + 1 == dist[nxt]:
            num[nxt] += num[now]
            num[nxt] %= mod

# Nまで到達できない場合
if dist[N-1] == 10**10:
    print(0)
    exit()

print(num[N-1]%mod)