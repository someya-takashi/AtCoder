# 再帰に時間がかかるので、提出はPyPyではなくPythonで出す

import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())

# オイラーツアーに使う配列
In = [0] * N
Out = [0] * N
graph = [[] for _ in range(N)]

for i in range(N-1):
    # 木の辺を張る
    a, b = map(int, input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

# 順番を管理するインデックス
idx = 0
# オイラーツアー
def dfs(now, parent):
    global idx
    # 行きがけ
    In[now] = idx
    idx += 1

    for c in graph[now]:
        if c != parent:
            dfs(c, now)
    
    # 抜けがけ
    Out[now] = idx
    idx+=1

# 根を決めて根からスタート、根のParentは適当に範囲外の-1にした
dfs(0, -1)

############# 以下、何らかのクエリの処理 #############

Q = int(input())