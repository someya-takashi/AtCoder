import itertools

comb = [[1, 2], [2, 3], [3, 1]]

# それぞれの要素から一つずつ選んで2**3通りの組み込みを作成
for p in itertools.product(*comb):
    print(p)

#結果
(1, 2, 3)
(1, 2, 1)
(1, 3, 3)
(1, 3, 1)
(2, 2, 3)
(2, 2, 1)
(2, 3, 3)
(2, 3, 1)