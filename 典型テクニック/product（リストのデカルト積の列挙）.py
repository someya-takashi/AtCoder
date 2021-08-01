# 問題iの選択肢がi番目に格納されているとする
sentakushi = [[1,2,3], [4,5,6], [2,3,5]]
# 問題iの答え
T = [2, 4, 5]
from itertools import product

# *でリストの要素を展開して引数に渡す
for p in product(*sentakushi):
    print(p)

    # 各選択肢の組み合わせの総得点を全探索
    ans = 0
    for i, q in enumerate(p):
        if q == T[i]:
            ans += 1

print(ans)
        