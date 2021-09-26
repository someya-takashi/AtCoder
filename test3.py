import sys
sys.setrecursionlimit(100000000)

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

nodes = [0] * N
dist = [0] * N

def dfs(n, d = 0, parent=-1):
    count = 1
    dist[n] = d
    for c in graph[n]:
        if c == parent:
            continue
        count += dfs(c, d+1, n)

    nodes[n] = count

    return count

dfs(0)

ans = 0
for i in range(1, N):
    ans += nodes[i] * (N-nodes[i])

print(ans)