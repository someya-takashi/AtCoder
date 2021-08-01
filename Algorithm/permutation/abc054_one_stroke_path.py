# メモ：順列列挙できる制約はN=11くらいまで？

from itertools import permutations

N, M = map(int, input().split())

graph =[[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

p = range(1,N)

ans = 0

# 1からNまでのパスの順列を列挙し、終点まで繋がるパスが存在するか全探索
for i in permutations(p):
    flag = True
    
    # 頂点1からのパスがあるか
    if not 0 in graph[i[0]]:
        continue

    for n in range(len(i)-1):
        # 次の頂点へのパスがあるか
        if not i[n+1] in graph[i[n]]:
            flag = False
            break

    if flag:
        ans += 1

print(ans)