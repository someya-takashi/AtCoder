def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out

# 例 : 6進数を10進数へ変換
print(Base_n_to_10("3532", 6))