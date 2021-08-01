N = int(input())
A = []
for i in range(N-1):
    # A[i]はA[i][i+1]からスタートするため、0からiまでの(i+1)個はダミーで埋める
    lst = list(map(int, input().split()))
    A.append([0]*(i+1) + lst)

ALL = 2**N

happy = [0]*ALL

# 整数nで表現される集合に要素iが含まれているかを判定
def has_bit(n, i):
    return (n & (1<<i) > 0)

# happyを各集合nに対して計算
# すべての集合に対して
for n in range(ALL):
    # すべての従業員に対して
    for i in range(N):
        # すべての相手従業員に対して
        for j in range(i+1, N):
            if has_bit(n, i) and has_bit(n, j):
                happy[n] += A[i][j]

ans = -10**100

for n1 in range(ALL):
    for n2 in range(ALL):
        # n1とn2の集合に同じ従業員が含まれる場合スキップ
        if n1 & n2 > 0:
            continue
        # n3はn1とn2の和集合を全集合から引いた補集合として求まる
        n3 = ALL - 1 - (n1|n2)
        ans = max(ans, happy[n1] + happy[n2] + happy[n3])

print(ans)