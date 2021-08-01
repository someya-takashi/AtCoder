# https://atcoder.jp/contests/abc005/tasks/abc005_4

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

s2 = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        s2[i][j] = D[i-1][j-1] + s2[i-1][j] + s2[i][j-1] - s2[i-1][j-1]

# 範囲外の場合分けが面倒なので0行0列を0でパディング
tako = [0] * (N*N+1)

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(i):
            for l in range(j):
                p = s2[i][j] - s2[k][j] - s2[i][l] + s2[k][l]
                num = (i-k)*(j-l)
                tako[num] = max(tako[num], p)

Q = int(input())

for i in range(Q):
    p = int(input())
    ans = 0
    for j in range(p+1):
        ans = max(ans, tako[j])

    print(ans)