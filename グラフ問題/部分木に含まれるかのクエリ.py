# オイラーツアーで各頂点に入ったタイミングInと抜けたタイミングOutを記録
# aがbの部分木に含まれるか=aはbの子孫かの判定は
# In[b] < In[a] and Out[b] > Out[a]で判定可能

# 例題：Past 巨大企業
# aがbの部下かを判定

import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())

# オイラーツアーに使う配列
In = [0] * N
Out = [0] * N
graph = [[] for _ in range(N)]
root = 0
for i in range(N):
    p = int(input())
    p-=1
    if p == -2:
        root = i
    else:
        graph[i].append(p)
        graph[p].append(i)

# 順番を管理するインデックス
idx = 0
# オイラーツアー
def dfs(now, parent=-1):
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

dfs(root)

Q = int(input())

for _ in range(Q):
    a, b = map(int, input().split())
    a-=1
    b-=1
    if In[b] < In[a] and Out[b] > Out[a]:
        print("Yes")
    else:
        print("No")