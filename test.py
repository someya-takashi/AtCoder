N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

SA = [0]
SB = [0]
for i in range(N):
    SA.append(SA[i]+A[i])

for i in range(M):
    SB.append(SB[i]+B[i])

import bisect

ans = 0
for i in range(N+1):
    now = SA[i]

    rest = K - now
    if rest > 0:
        j = bisect.bisect_right(SB, rest)
        total = i + j - 1
        ans = max(ans, total)

print(ans)