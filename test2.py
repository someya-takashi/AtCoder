import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

#####segfunc#####
def segfunc(x, y):
    return x + y
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

In = [0] * N
Out = [0] * N
# Depth : 木の高さをInとOut時に記憶（区間処理用）
# セグ木に渡してmin(In[a], In[b])からmax(Out[a], Out[b])区間の範囲minを取るとLCAのDepthがわかる
Depth = []
# Depth_index : 木の高さ（インデックスで直接参照用）
Depth_index = [0] * N
idx = 0
# オイラーツアー
def dfs(now, d = 0, parent=-1):
    global idx
    # 行きがけ
    In[now] = idx
    idx += 1
    Depth.append(d)
    Depth_index[now] = d

    for c in graph[now]:
        if c != parent:
            dfs(c, d+1, now)
            Depth.append(0)
            idx+=1
    
    Out[now] = idx
    idx+=1
    Depth.append(0)
    
dfs(0)

nodes = [0] * N
def dfs2(n, parent=-1):
    count = 1
    for c in graph[n]:
        if c == parent:
            continue
        count += dfs2(c, n)
 
    nodes[n] = count
 
    return count
dfs2(0)

sg = SegTree(Depth, segfunc, ide_ele)

for i in range(N):
    ans = 0
    l = In[i]
    r = Out[i]
    pl = In[0]
    pr = Out[0]
    a = 0
    b = 0
    a += sg.query(l, r+1)
    a -= nodes[i]*Depth_index[i]
    b = (N-nodes[i])*Depth_index[i]
    b -= sg.query(pl, l)
    b -= sg.query(r+1, pr+1)
    ans = a+b
    
    print(ans)
