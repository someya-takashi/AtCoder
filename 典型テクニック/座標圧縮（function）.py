# 座標の重複に対応
# 0-index
# 引数のリストはソートしておく
def compression(A: list) -> list:
    "座標圧縮"
    num = 0
    B = []
    for i in range(len(A)):
        if i > 0 and A[i] == A[i-1]:
            B.append(B[-1])
        else:
            B.append(num)
            num += 1
    return B