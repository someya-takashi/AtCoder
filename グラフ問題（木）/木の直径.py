# https://atcoder.jp/contests/typical90/tasks/typical90_c

# argmaxで楽したいとき用、PyPY不可
# 時間ぎりぎりならPyPy使用してループで最大値のインデックス求める
from numpy.core.fromnumeric import argmax

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

path1 = [-1] * N
path1[0] = 0

from collections import deque
Q = deque()
Q.append(0)

while Q:
    q = Q.popleft()

    for n in graph[q]:
        if path1[n] == -1:
            path1[n] = path1[q] + 1
            Q.append(n)

u = argmax(path1)

path2 = [-1] * N
path2[u] = 0
Q.append(u)

while Q:
    q = Q.popleft()

    for n in graph[q]:
        if path2[n] == -1:
            path2[n] = path2[q] + 1
            Q.append(n)

print(max(path2)+1)