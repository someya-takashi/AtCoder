N = int(input())

p = list(map(float, input().split()))

import math

s = math.ceil(N/2)

p_list = [[0]*(N+1) for _ in range(N+1)]
p_list[1][0] =(1-p[0])
p_list[1][1] = p[0]

for i in range(1, N+1):
    for j in range(i+1):
        if j == 0:
            p_list[i][0] += p_list[i-1][0] * (1-p[i-1])
            continue
        # 裏の場合
        p_list[i][j] += p_list[i-1][j] * (1-p[i-1])
        # 表の場合
        p_list[i][j] += p_list[i-1][j-1] * p[i-1]

sum_p = 0
for i in range(s,N+1):
    sum_p += p_list[N][i]

print(sum_p)