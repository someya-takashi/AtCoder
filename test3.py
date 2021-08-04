N = int(input())

l = -10**18
r = 10**18
s = 0

for _ in range(N):
    a, t = map(int, input().split())
    if t == 1:
        s += a
        l += a
        r += a
    elif t == 2:
        l = max(a, l)
        r = max(a, r)
    else:
        l = min(a, l)
        r = min(a, r)

Q = int(input())
X = list(map(int, input().split()))
for i in range(Q):
    if X[i] + s <= l:
        print(l)
    elif X[i] + s >= r:
        print(r)
    else:
        print(X[i] + s)

    
