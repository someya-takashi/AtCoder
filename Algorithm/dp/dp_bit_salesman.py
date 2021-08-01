N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ALL = 1<<N

cost = [[10**4]*N for _ in range(ALL)]

cost[0][0] = 0

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

print(cost[ALL-1][0])