import sys
sys.setrecursionlimit(100000000)

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

nodes = [0] * N

def dfs(n, parent=-1):
    count = 1
    for c in graph[n]:
        if c == parent:
            continue
        count += dfs(c, n)

    nodes[n] = count

    return count

dfs(0)
print(nodes)