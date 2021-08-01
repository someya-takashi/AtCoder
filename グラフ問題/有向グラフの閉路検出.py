# DAGのトポロジカルソート
# AOJ : https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B&lang=jp
# 有向辺の閉路検出もできる（トポロジカルソートができることと有向サイクルが存在しないことが等価なため）

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
# 各頂点の入り次数を検出するための配列
In = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    # bの入り次数をインクリメント
    In[b-1] += 1

from collections import deque
Q = deque()

for i in range(N):
    # 入り次数0の頂点をキューに追加
    if In[i] == 0:
        Q.append(i)

# トポロジカルソート格納用の配列
ans = []

# キューが空になるまで
while Q:
    # 入り次数0の頂点をポップし、ansに追加
    i = Q.popleft()
    ans.append(i)

    # ポップした頂点に隣接する頂点の入り次数を1減らす
    for c in graph[i]:
        In[c] -= 1
        # このときcの入り次数が0になったら、キューに追加する
        if In[c] == 0:
            Q.append(c)

# サイクルに属するような頂点はキューに追加されない、すなわちlen(ans) < Nなら閉路がある
if len(ans) != N:
    print("トポロジカルソートは存在しません（閉路があります）")
else:
    print(" ".join(map(str, ans)))