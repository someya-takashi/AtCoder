import sys
sys.setrecursionlimit = 10000000

N, M = map(int, input().split())

child = [[] for _ in range(N)]
has_parent = [False] * N

for i in range(M):
    x, y = map(int, input().split())
    child[x-1].append(y-1)
    has_parent[y-1] = True

visited = [False] * N
memo = [0] * N

def dfs(node):
    
    if visited[node]:
        return memo[node]
    
    visited[node] = True

    max_len = 0
    for c in child[node]:
        max_len = max(max_len, dfs(c) + 1)

    memo[node] = max_len
    return max_len

ans = 0
for i in range(N):
    if not has_parent[i]:
        ans = max(ans, dfs(i))

print(ans)
        
