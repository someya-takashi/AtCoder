N = int(input())
# 頂点i,j間のコスト行列
A = [list(map(int, input().split())) for _ in range(N)]

ALL = 1<<N

cost = [[10**10]*N for _ in range(ALL)]

# 巡回しないかつ、始点と終点が任意のケースを想定
# 初期化は各頂点のスタート位置を0にする
# 始点が決まっている場合は始点のところだけ0にする
for i in range(N):
    cost[1<<i][i] = 0

def has_bit(n, i):
    return (n & (1<<i) > 0)

# すべての集合：{}からスタートして{0,1,2,3...,N}まで
for n in range(ALL):
    # すべての遷移元
    for i in range(N):
        # すべての遷移先
        for j in range(N):
            # すでに訪問済みか同じ都市は無視する
            if has_bit(n, j) or i ==j:
                continue
            cost[n|1<<j][j] = min(cost[n|1<<j][j], cost[n][i] + A[i][j])

print(min(cost[ALL-1]))