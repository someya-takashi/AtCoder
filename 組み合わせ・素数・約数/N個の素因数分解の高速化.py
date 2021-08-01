# N個の数列Aに対して1つずつ素因数分解をすると、Aの最大値をaとしてO(N√a)の計算量になる
# 各要素に対して素因数分解を行うのではなく、aまでの素数と2 <= i <= aに対する最小の素因数（D[i]）を
# エラトステネスの篩で予め計算しておき、その結果をN個の数列に利用することで、Aiの素因数分解の
# 計算量を√AiからlogAiに改善できる
# 結果として、全体の計算量はO(Nloga)となり、N=10**6, Ai <= 10**6のような制約でも解くことができる


# 問題例：https://atcoder.jp/contests/abc177/tasks/abc177_e
from math import gcd

N = int(input())
A = list(map(int, input().split()))

# setwiseかどうか
gcd_all = A[0]
for i in range(1, N):
    gcd_all = gcd(gcd_all, A[i])

    if gcd_all == 1:
        break

# setwiseではない場合
if gcd_all != 1:
    print("not coprime")
    exit()

#pairwiseの確認
A_max = max(A)

prime_flag = [True] * (A_max+1)
# Dのi番目はiの中で最小の素数：D[24] = 2
D = [0] * (A_max+1)
prime_flag[0] = False
prime_flag[1] = False

# 前処理としてAの最大までの素数のリストとDをエラトステネスの篩で列挙
# 前処理の計算量はAloglogAなのでA=10**6では可能
for i in range(2, A_max+1):
    if prime_flag[i]:
        # iが素数の場合、その倍数をふるい落とし
        for j in range(i, A_max+1, i):
            prime_flag[j] = False
            if D[j] == 0:
                D[j] = i

# 素数のカウンター
prime_count = [0] * (A_max+1)
pair_flag = True

# Aの素因数分解の計算量は事前準備により最大でlogAなので、全体の計算量はO(NlogA)
for i in range(N):
    temp = A[i]
    d = 0
    # 1になるまで素因数分解
    while temp != 1:
        # tempの素数が他でも使われている場合
        if prime_count[D[temp]] == 1 and d != D[temp]:
            pair_flag = False
            break
        prime_count[D[temp]] = 1
        d = D[temp]
        temp = temp // D[temp]

    if not pair_flag:
        break

if pair_flag:
    print("pairwise coprime")
else:
    print("setwise coprime")