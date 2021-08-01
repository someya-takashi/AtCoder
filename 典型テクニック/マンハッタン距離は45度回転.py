"""
（与式） = |Xi - Xj| + |Yi - Yj|
    = max(Xi - Xj, Xj - Xi) + max(Yi - Yj, Yj - Yi)
    = max((Xi - Xj) + (Yi - Yj), (Xi - Xj) + (Yj - Yi), (Xj - Xi) + (Yi - Yj), (Xj - Xi) + (Yj - Yi))
    = max((Xi + Yi) - (Xj + Yj), (Xi - Yi) - (Xj - Yj), -{(Xi - Yi) - (Xj - Yj)}, -{(Xi + Yi) - (Xj + Yj)})
    = max(|(Xi + Yi) - (Xj + Yj)|, |(Xi - Yi) - (Xj - Yj)|)
ここで、
Zi = Xi + Yi
Wi = Xi - Yi
と置き換えると、
（与式）= max(|Zi - Zj|, |Wi - Wj|)
ここで i を固定すると、
（与式）= max(Zi - min(Zj), max(Zj) - Zi, Wi - min(Wj), max(Wj) - Wi)
となるので、
各クエリ毎の点を(Xi, Yi)と見なせば、O(1)でクエリを処理することが可能
※前処理として、min(Zj), max(Zj), min(Wj), max(Wj)をO(N)で求める
"""

# 典型90 : https://atcoder.jp/contests/typical90/tasks/typical90_aj
# マンハッタン距離を45度回転させた点i,j間の距離はmax(|Zi - Zj|, |Wi - Wj|)となり、
# これは回転後座標におけるチェビシェフ距離になる

N, Q = map(int, input().split())

P = []

X = []
Y = []

for _ in range(N):
    x, y = map(int, input().split())
    X.append(x+y)
    Y.append(x-y)
    P.append([x+y, x-y])

Xmax = max(X)
Xmin = min(X)
Ymax = max(Y)
Ymin = min(Y)

for _ in range(Q):
    # 点qと点q以外の(N-1)個の点におけるマンハッタン距離の最大を求める
    q = int(input())
    x, y = P[q-1]
    # マンハッタン距離が最大となるのは4つの候補しかない
    ans = max(abs(x-Xmax), abs(x-Xmin), abs(y-Ymax), abs(y-Ymin))
    print(ans)
