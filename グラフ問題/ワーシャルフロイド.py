# cost[i][j]: 頂点v_iから頂点v_jへ到達するための辺コストの和
N, M  = map(int, input().split())

INF = 10**10
cost = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = c
    cost[b-1][a-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][k]!=INF and cost[k][j]!=INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])