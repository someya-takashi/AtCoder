N, M = list(map(int, input().split()))

ok = [True] * (N+1)
for i in range(M):
    a = int(input())
    ok[a] = False

MOD = 10**9+7

cnt = [0]*(N+1)
cnt[0] = 1

for i in range(1, N+1):
    if ok[i]:
        if i == 1:
            cnt[i] = cnt[i-1]
        else:
            # 足し算、引き算、掛け算しか使わない場合は、最後にMODで割った余りと
            # 任意のタイミングでMODで割り、その余りに置き換えて最後まで計算した
            # 場合と結果が変わらない
            # べき乗や階乗などを扱うときは数値が大きくなりメモリを多く消費するので、
            # 適宜MODで割っていき小さい値にする
            cnt[i] = (cnt[i-1] + cnt[i-2]) % MOD

print(cnt[N])