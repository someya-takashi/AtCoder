# https://atcoder.jp/contests/typical90/tasks/typical90_ak

import sys
input = sys.stdin.readline

#####segfunc#####
def segfunc(x, y):
    return max(x, y)
    # return min(x, y)
    # return max(x, y)
    # return x^y
#################

##### 単位元 #####
ide_ele = -10**15
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


W, N = map(int, input().split())
sp = []
for _ in range(N):
    l, r, v = map(int, input().split())
    sp.append([l, r, v])

dp = [[-10**15] * (W+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    l, r, v = sp[i-1]
    sg = SegTree(dp[i-1], segfunc, ide_ele)
    for j in range(W+1):
        # i番目を使わない
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        # 遷移不可
        if j < l:
            continue
        # 左端が0以下になる場合（0~j-lの範囲からのみ遷移可能）
        elif l <= j < r:
            ll = 0
            rr = j-l
        # j-r, j-lの範囲すべてから遷移可能
        elif r <= j:
            ll = j-r
            rr = j-l
        dp[i][j] = max(dp[i-1][j], sg.query(ll, rr+1) + v)


if dp[N][W] < 0:
    print(-1)
else:
    print(dp[N][W])
