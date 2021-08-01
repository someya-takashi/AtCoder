from collections import deque

#頂点数N, 辺情報E, 始点sとする

# 隣接行列を容易
visited = []
for i in range(N):
    visited.append(False)

# キューを用意
Q = deque()
Q.append(s)
visited[s] = True

# キューから取り出しながら探索する
while len(Q) > 0:
    i = Q.popleft()
    for j in E[i]:
        if not visited[j]:
            visited[j] = True
            Q.append(j)