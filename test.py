N = int(input())
A = list(map(int, input().split()))

acc = [0]
for i in range(N):
    acc.append(acc[i]+A[i])

import bisect

ans = 10**10
for b in range(1, N-1):
    S = acc[b+1]

    a = bisect.bisect_left(acc, S/2)
    Sp = acc[a]
    Sq = S - Sp

    SS = acc[-1] - S

    c = bisect.bisect_left(acc, S+SS/2)
    Sr = acc[c] - S
    Ss = SS-Sr

    ans_min = min(Sp, Sq, Sr, Ss)
    ans_max = max(Sp, Sq, Sr, Ss)

    ans = min(ans, ans_max-ans_min)

print(ans)



    

