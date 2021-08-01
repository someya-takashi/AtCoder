# https://atcoder.jp/contests/typical90/tasks/typical90_ab
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/028.jpg

# 二次元平面上に紙がN枚置かれており、i番目の紙の左下の座標と右上の座標が与えられている
# i=0からNまでのkについて、紙がk枚重なっている領域の面積をそれぞれ求める

N = int(input())
area = 1001

grid = [[0] * area for _ in range(area)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    grid[lx][ly] += 1
    if rx <= area-1 and ry <= area-1:
        grid[rx][ry] += 1

    if rx <= area-1:
        grid[rx][ly] -= 1

    if ry <= area-1:
        grid[lx][ry] -= 1

imos = [[0] * area for _ in range(area)]

for i in range(area):
    for j in range(area):
        imos[i][j] += grid[i][j]

        if i > 0:
            imos[i][j] += imos[i-1][j]
        if j > 0:
            imos[i][j] += imos[i][j-1]
        if i > 0 and j > 0:
            imos[i][j] -= imos[i-1][j-1]

counter = [0] * (N+1)

for i in range(area):
    for j in range(area):
        if imos[i][j] != 0:
            counter[imos[i][j]] += 1

for i in range(1, N+1):
    print(counter[i])
