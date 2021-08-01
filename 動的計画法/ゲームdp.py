# https://atcoder.jp/contests/dp/tasks/dp_k

N, K = map(int, input().split())
A = list(map(int, input().split()))
min_a = min(A)

dp = [False] * (K+1)

dp[0] = False
for i in range(N):
    dp[A[i]] = True

for i in range(1, K+1):
    flag = False
    for j in range(N):
        if dp[i]:
            continue
        if i - A[j] >= 0:
            if not dp[i-A[j]]:
                dp[i] = True
                break

if dp[K]:
    print("First")
else:
    print("Second")