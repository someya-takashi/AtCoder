# ダブリングを利用して計算量をO(ND)からO(NlogD)に削減する解法
# 繰り返し二乗法は累乗の計算を短縮するために2→4→8..と累乗をまとめてとりlogの計算に削減する手法
# 累乗だけでなく、この手法は合成可能な関数に適応でき、一般的にダブリングと呼ばれる
# 繰り返し二乗法は関数がf(x) = x^a のときの呼び方

# ダブリングのイメージ
# T1[k] = T[k]
# T2[k] = T1[T1[k]]
# T4[k] = T2[T2[k]]
# T8[K] = T4[T4[k]]
# ...

N, M, D = map(int, input().split())
A = list(map(int, input().split()))

amida = [i for i in range(N)]

# あみだくじ一回分の番号の遷移
for i in range(M):
    amida[A[i]-1], amida[A[i]] = amida[A[i]], amida[A[i]-1]

# 制約より少し多めに2^40回分の操作を記録する配列を用意
dp = [[0] * N for _ in range(40)]

# あみだくじ0回の番号位置
for i in range(N):
    dp[0][i] = i

# あみだくじ1回したときの番号位置（前計算しておいたamidaを利用）
for i in range(N):
    dp[1][i] = amida[dp[0][i]]

# dp[i]があみだくじを2^i回したときを表す
for i in range(2, 40):
    for j in range(N):
        # dpの遷移：2^(i-1)回したときj番目に来る数字を2^(i-1)回の遷移式（dp[i-1]）に代入
        dp[i][j] = dp[i-1][dp[i-1][j]]

a = []
# 累乗を分解：例 100→64+32+4
for i in range(N):
    ans = i
    for j in range(40):
        # bitが立っていたら2^jの遷移式を利用
        if D & 1<<j:
            ans = dp[j+1][ans]

    a.append([i, ans])
    
a.sort(key=lambda x:x[1])

for i in range(N):
    print(a[i][0]+1)