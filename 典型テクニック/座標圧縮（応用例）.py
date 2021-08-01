# https://atcoder.jp/contests/typical90/tasks/typical90_ac
# 座標圧縮を使った部分点回答
# W < 10**5, N < 9000なのでWNではTLE
# 登場する座標がLとRで最大2N個なので、座標圧縮することでN^2になり、間に合う
# Wがもっと大きい場合でも、Nに落とせるので、このような場合に座標圧縮するかの判断をできるようにする

W, N = map(int, input().split())

# 登場する座標を管理（重複排除のためセット）
wx = set()
lr = []
for i in range(N):
    l, r = map(int, input().split())
    wx.add(l-1)
    wx.add(r-1)
    lr.append([l-1, r-1])

# 圧縮前と圧縮後の座標の対応を管理する辞書
d = {}

# ソートするためリストに変換
wx = list(wx)
wx.sort()

# 座標が小さい順から0, 1, 2, .. と圧縮後の座標を割り当てる
for i, x in enumerate(wx):
    d[x] = i

# ブロックの高さの配列を圧縮後の座標の個数分用意
w = [0] * len(d)

for i in range(N):
    l, r = lr[i]

    h = 0
    for j in range(d[l], d[r]+1):
        h = max(h, w[j])

    for k in range(d[l], d[r]+1):
        w[k] = h+1

    print(h+1)