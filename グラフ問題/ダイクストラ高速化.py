# https://atcoder.jp/contests/abc022/tasks/abc022_c
# にてダイクストラの書き方を変えるとTLE→851msと大幅に時間短縮できたのでメモ

# 変更前でTLEになっていた部分
# とりあえずheapに入れ、取り出した時にそれ以前に取り出されているかを確認していたが、
# 変更後のコードのようにheapに入れる前にpathの値を更新できるか確認し、更新が可能な
# 場合はpathを更新し、heapに入れる
# while Q and flag:
#     l, i = heapq.heappop(Q)
#     if path[i] != 10**12:
#         continue
#     path[i] = l
 
#     for c, lc in graph[i]:
#         if i == 0 and c == u:
#             continue
#         if i == u and c == 0:
#             ans = min(ans, l + lc)
#             flag = False
#             break
#         if path[c] != 10**12:
#             continue
#         heapq.heappush(Q, [l+lc, c])

# 変更後
# path[0] = 0
# while Q and flag:
#     l, i = heapq.heappop(Q)
#     # 下記の判定を入れても時間はあまり変わらなかった、入れておいたほうが無難？
#     if path[i] < l:
#             continue

#     for c, lc in graph[i]:
#         if i == 0 and c == u:
#             continue
#         if i == u and c == 0:
#             ans = min(ans, l + lc)
#             flag = False
#             break
#         if path[c] > path[i] + lc:
#             path[c] = path[i] + lc
#         heapq.heappush(Q, [l+lc, c])


# コード全体
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, l = map(int, input().split())
    graph[u-1].append([v-1, l])
    graph[v-1].append([u-1, l])

import heapq
ans = 10**10

for u, lu in graph[0]:
    path = [10**12] * N
    Q = []
    heapq.heappush(Q, [0, 0])
    flag = True
    path[0] = 0

    while Q and flag:
        l, i = heapq.heappop(Q)

        for c, lc in graph[i]:
            if i == 0 and c == u:
                continue
            if i == u and c == 0:
                ans = min(ans, l + lc)
                flag = False
                break
            if path[c] > path[i] + lc:
                path[c] = path[i] + lc
                heapq.heappush(Q, [l+lc, c])
            
if ans == 10**10:
    print(-1)
else:
    print(ans)