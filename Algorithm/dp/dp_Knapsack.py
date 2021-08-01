N, W = list(map(int, input().split()))

# 1始まりにするために先頭にダミーを入れる
ws = [0]
vs = [0]
for i in range(N):
    w, v = list(map(int, input().split()))
    ws.append(w)
    vs.append(v)

# 重さと価値の最大値を記録する二次元リスト
value = []
for i in range(N+1):
    value.append([-10**18]*(W+1))

value[0][0] = 0

for i in range(1, N+1):
    for w in range(W+1):
        # 品物iを使わない場合
        value[i][w] = max(value[i][w], value[i-1][w])
        # 品物iを使う場合
        if w - ws[i] >= 0:
            value[i][w] = max(value[i][w], value[i-1][w-ws[i]] + vs[i])

ans = max(value[N])
print(ans)



