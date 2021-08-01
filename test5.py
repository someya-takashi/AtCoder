N = int(input())
A = list(map(int, input().split()))
SUM = sum(A)
A = A*2

ans = 10**15

from collections import deque
Q = deque()
now = 0
i = 0
while i < 2*N:
    while now < SUM/2:
        Q.append(A[i])
        now += A[i]
        ans = min(ans, SUM-now)
        i += 1

    while Q and now > SUM/2:
        rm = Q.popleft()
        now -= rm
        ans = min(ans, SUM-now)
    
print(ans)