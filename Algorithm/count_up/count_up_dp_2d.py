H, W = list(map(int, input().split()))
A = []
for i in range(H):
    s = input()
    A.append(s)

cnt = []
for i in range(H):
    cnt.append([0]*W)

cnt[0][0] = 1

MOD = 10**9+7

for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            continue

        if i > 0:
            cnt[i][j] += cnt[i-1][j]
        if j > 0:
            cnt[i][j] += cnt[i][j-1]
        cnt[i][j] %= MOD

print(cnt[H-1][W-1])