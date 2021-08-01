# https://atcoder.jp/contests/abc170/tasks/abc170_e
# https://tsubo.hatenablog.jp/entry/2020/06/15/124657


import heapq
# insert(x), 要素の挿入：O(logN)
# erase(x), 要素の削除：O(logN)
# is_exist(x), 要素の存在を確認：O(1)
# get_min(), 最小値の取得：O(1)

class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()

    def insert(self,x):
        heapq.heappush(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,"is not in HeapDict")
            exit()
        else:
            self.d[x]-=1

        while len(self.h)!=0:
            if self.d[self.h[0]]==0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]

    def get_len(self):
        return len(self.h)

#####segfunc#####
def segfunc(x, y):
    return min(x, y)
    # return min(x, y)
    # return max(x, y)
    # return x^y
#################

##### 単位元 #####
ide_ele = 10**15
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

import sys
input = sys.stdin.readline

# 幼稚園の数
NUM = 2*10**5

N, Q = map(int, input().split())
# 幼児iのレートと所属する幼稚園のリスト
position = [None] * N
# 幼稚園の数分の順序付き集合（マルチセット）
kind = [HeapDict() for _ in range(NUM)]

for i in range(N):
    a, b = map(int, input().split())
    # 最大値を取り出すため-1倍
    kind[b-1].insert(-a)
    position[i] = [a, b-1]

A = [ide_ele] * NUM
for i in range(NUM):
    if kind[i].get_len():
        # セグメント木を初期化するための初期レート分布
        A[i] = -kind[i].get_min()

sg = SegTree(A, segfunc, ide_ele)

for i in range(Q):
    c, d = map(int, input().split())
    c-=1
    d-=1
    a, b = position[c]
    position[c] = [a, d]
    # 移動元の幼稚園bから-aを削除
    kind[b].erase(-a)
    # 移動先の幼稚園dへ-aを追加
    kind[d].insert(-a)

    # 幼児数が0でないなら幼稚園bの最大値を更新
    if kind[b].get_len():
        mb = kind[b].get_min()
        sg.update(b, -mb)
    else:
        sg.update(b, ide_ele)
    # 幼稚園dの最大値を更新
    md = kind[d].get_min()
    sg.update(d, -md)
    # 各幼稚園の最大値の中で、一番小さい値を出力
    print(sg.query(0, NUM+1))