# 計算量　流すフローをFとするとO(F|E|)

from collections import defaultdict, deque

INF = float("inf")

# 頂点、辺の数
V, E  = map(int, input().split())

Start = 0
Goal = V-1
ans = 0

# 有向辺をsetで保持するdefaultdict
lines = defaultdict(set)

# a→bへのコストはV×Vの配列で別に保持しておく
cost = [[0] * V for _ in range(V)]

# 有向辺を張る
for i in range(E):
    # 入力が0-indexedの場合
    a, b, c = map(int, input().split())
    # コスト0の辺が入力にある場合の例外処理
    if c != 0:
        lines[a].add(b)
        cost[a][b] += c

# Ford-Fulkerson法
def Ford_Fulkerson(s):
    global ans

    q = deque()
    # 探索点とフローを追加（最初は出来るだけ流したいのでINFを流す）
    q.append([s, INF])
    # 到達済み判定用
    ed = [True] * V
    ed[s] = False
    # ルート
    route = [0 for _ in range(V)]
    route[s] = -1

    while q:
        s, flow = q.pop()
        for t in lines[s]:
            if ed[t]: # 未到達の場合
                flow = min(cost[s][t], flow) # flow = min(その辺のコスト、直前のflow)
                route[t] = s
                q.append([t, flow])
                ed[t] = False
                if t == Goal:
                    ans += flow
                    break
        else:
            continue
        break
    else:
        return False
    
    # ラインの更新
    t = Goal
    # BFSで求めたルートの辺を潰して逆向き同コストの辺を張る
    s = route[t]

    while s != -1:
        # s -> t のコスト減少、ゼロになるなら辺を削除
        cost[s][t] -= flow
        if cost[s][t] == 0:
            lines[s].remove(t)
        # t -> s （逆順）のコスト増加、元がゼロなら辺を作成
        if cost[t][s] == 0:
            lines[t].add(s)
        cost[t][s] += flow
        t = s
        s = route[t]

    return True


# Ford-Fulkerson法を実行
# 始点から実行し、Falseが返ってくる（Goalに到達できなかった）まで繰り返す

while True:
    if Ford_Fulkerson(Start):
        continue
    else:
        break

print(ans)