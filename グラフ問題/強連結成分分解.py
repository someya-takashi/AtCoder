# 計算量はDFS二回分
# PyPyだと再帰が遅いのでPythonで提出する

import sys
sys.setrecursionlimit(10000000)

class SCC:
 
    def __init__(self, n):
        self.n = n
        self.graph = [[] for i in range(n)]
        self.graph_rev = [[] for i in range(n)]
        self.used = [False]*n
 
    def add_edge(self, fr, to):
        if fr == to:
            return
        self.graph[fr].append(to)
        self.graph_rev[to].append(fr)
 
    def dfs(self, node, graph):
        self.used[node] = True
        for nex in graph[node]:
            if self.used[nex]:
                continue
            self.dfs(nex,graph)
        self.order.append(node)
 
    def first_dfs(self):
        self.used = [False]*self.n
        self.order = []
        for i in range(self.n):
            if self.used[i]:
                continue
            self.dfs(i,self.graph)
    
    def second_dfs(self):
        self.used = [False]*self.n
        self.ans = []
        for node in reversed(self.order):
            if self.used[node]:
                continue
            self.used[node] = True
            self.order = []
            self.dfs(node, self.graph_rev)
            self.ans.append(self.order)
 
    def scc(self):
        self.first_dfs()
        self.second_dfs()
        return self.ans


# 以下使い方の例
# 典型90 https://atcoder.jp/contests/typical90/tasks/typical90_u

N, M = map(int, input().split())
scc = SCC(N)

for _ in range(M):
    a, b = map(int, input().split())
    # 有向グラフを構築
    scc.add_edge(a-1, b-1)

ans = 0
for group in scc.scc():
    ans += len(group)*(len(group)-1)//2

print(ans)