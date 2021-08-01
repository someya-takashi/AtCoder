N, W = map(int, input().split())

wi = [0]
vi = [0]

for i in range(N):
    w, v = map(int, input().split())
    wi.append(w)
    vi.append(v)

# 取りうる価値の最大値
v_sum = 0
for i in range(N+1):
    v_sum += vi[i]

weight = [[10**100]*(v_sum+1) for _ in range(N+1)]

weight[0][0] = 0

for i in range(1, N+1):
    for j in range(v_sum+1):
        weight[i][j] = min(weight[i][j], weight[i-1][j])

        if j - vi[i] >= 0:
            weight[i][j] = min(weight[i][j], weight[i-1][j-vi[i]] + wi[i])

# 価値最大からスタートして初めてW以下となった価値が答え
ans = 0
for v in range(v_sum, 1, -1):
    if weight[N][v] <= W:
        ans = v
        break

print(ans)