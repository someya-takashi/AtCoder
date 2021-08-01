# https://qiita.com/keroru/items/6e0a22e8c9bf2a24dc68
# https://atcoder.jp/contests/abc032/tasks/abc032_c

from collections import deque

## 入力の受け取り
n,k=map(int,input().split())
a=[int(input()) for i in range(n)]

## コーナーケースの処理
if 0 in a:
    print(n)
    exit()

ans=0
q=deque()
p=1  ## 今、見ている区間の要素の積をpで管理する。
for c in a:
    q.append(c)  ## dequeの"右端"に要素を一つ追加する。
    p*=c

    while q and p>k: ## 要素の積がKを超えているか？
        rm=q.popleft() ## 条件を満たさないのでdequeの"左端"から要素を取り除く
        p//=rm ## 取り除いた値に応じて要素の積を更新する

    ans=max(ans,len(q)) ## dequeに入っている要素の積がK以下になるまで区間を縮めた。

print(ans)