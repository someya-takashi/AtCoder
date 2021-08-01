# ユーグリッドの互除法により最大公約数を求める
def GCD(m, n):
    if n == 0:
        return m
    
    # 再帰呼び出し
    return GCD(n, m % n)