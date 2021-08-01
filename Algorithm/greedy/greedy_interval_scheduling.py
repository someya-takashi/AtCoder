N = int(input())

# タスクの開始日と終了日
BA = []
for i in range(N):
    a, b = list(map(int, input().split()))
    BA.append([b, a])

# 終了日が小さい順に並び替え
BA.sort()

ans = 0
last = 0
for b, a in BA:
    # 前のタスクの終了日が次のタスクの開始日より小さいか
    if last < a:
        ans += 1
        # 採用したタスクの終了日に更新
        last = b

print(ans)