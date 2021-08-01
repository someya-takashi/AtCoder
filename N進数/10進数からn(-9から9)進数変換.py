# 負のn進数にも対応
# nの範囲は-9 ~ -2, 2 ~ 9
def Base_10_to_n(X : int, n : int) -> str: 
    ret = ''
    while X != 0:
        r = X%n
        if r < 0:
            r += 2
        ret = str(r)+ret
        X = (X-r)//n
    return ret