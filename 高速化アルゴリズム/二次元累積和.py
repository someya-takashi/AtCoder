# 参考：https://tqk.hatenablog.jp/entry/ABC106-2
# 一次元直線を走る列車のうち、pからqに閉区間を持つ列車が何本あるかを求める問題
# https://atcoder.jp/contests/abc106/tasks/abc106_d

N, M, Q = map(int, input().split())

train = [[0] * N for _ in range(N)]

for _ in range(M):
    l, r = map(int, input().split())
    # ここは0-indexed
    train[l-1][r-1]+=1

# ruiseki[q][q] - ruiseki[q][p-1] - ruiseki[p-1][q] + ruiseki[p-1][p-1]を計算するときに
# インデックス参照外にならないよう1行目と1列目にダミーで0配列を追加しておく
ruiseki = [[0] * (N+1) for _ in range(N+1)]

# N<=500なので二次元累積和が利用できる

for i in range(1, N+1):
    for j in range(1, N+1):
        ruiseki[i][j] += train[i-1][j-1]
        ruiseki[i][j] += ruiseki[i-1][j]
        ruiseki[i][j] += ruiseki[i][j-1]
        ruiseki[i][j] -= ruiseki[i-1][j-1]

# クエリに対する回答
for _ in range(Q):
    # 1行目と1列目にダミーを追加したので1-indexedで操作
    p, q = map(int, input().split())
    # pの外側の領域を引きたいので、pを-1すること（図を描けばわかりやすい）
    ans = ruiseki[q][q] - ruiseki[q][p-1] - ruiseki[p-1][q] + ruiseki[p-1][p-1]
    print(ans)


