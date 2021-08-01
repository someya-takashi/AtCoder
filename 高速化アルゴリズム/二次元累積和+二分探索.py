# https://atcoder.jp/contests/abc203/tasks/abc203_d

N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ruiseki = [[0] * (N+1) for _ in range(N+1)]

def check(x):
    for i in range(1, N+1):
        for j in range(1, N+1):
            ruiseki[i][j] = 0
            if A[i-1][j-1] <= x:
                ruiseki[i][j] += 1
            ruiseki[i][j] += ruiseki[i-1][j]
            ruiseki[i][j] += ruiseki[i][j-1]
            ruiseki[i][j] -= ruiseki[i-1][j-1]

    for i in range(N-K+1):
        for j in range(N-K+1):
            num = ruiseki[i+K][j+K] - ruiseki[i+K][j] - ruiseki[i][j+K] + ruiseki[i][j]
            if num >= -(-(K**2)//2):
                return True

    return False

ok = 10**10
ng = -1

while abs(ng-ok) > 1:
    mid = (ng+ok)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
