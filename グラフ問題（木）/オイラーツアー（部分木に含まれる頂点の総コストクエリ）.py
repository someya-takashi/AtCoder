import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

#####segfunc#####
def segfunc(x, y):
    return sum(x, y)
    # return min(x, y)
    # return max(x, y)
    # return x^y
#################

##### 単位元 #####
ide_ele = 0
# 最小値：float("inf")
# 最大値：float("inf")*(-1)
# Xor : 0
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    x,y = map(int, input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

# 頂点にコストがある場合
cost = [0] * N
for i in range(N):
    c = int(input())
    cost[i] == c

In = [0] * N
Out = [0] * N
# 部分木クエリ処理用配列（https://qiita.com/recuraki/items/72e37eb9be9f71bc623a）
# vcost : 部分木に含まれる頂点・辺の総コスト計算用
vcost = []


idx = 0
# オイラーツアー
def dfs(now, parent=-1):
    global idx
    # 行きがけ
    In[now] = idx
    idx += 1
    vcost.append(cost[now])

    for c in graph[now]:
        if c != parent:
            dfs(c, now)
            idx+=1
    
    Out[now] = idx
    idx+=1
    vcost.append(0)
    
dfs(0)

# 部分木に含まれる頂点コスト計算用セグ木
sg = SegTree(vcost, segfunc, ide_ele)

Q = int(input())

for q in range(Q):
    # aの部分木の総コストを答える場合
    a = int(input())
    a-=1

    # Range Sum Querry
    l = In[a]
    r = Out[a]
    # 部分木のコストに関するRSQ
    sub_cost = sg.query(l, r+1)

    print(sub_cost)

