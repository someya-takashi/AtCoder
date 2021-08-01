# 例題：https://atcoder.jp/contests/abc170/tasks/abc170_e
# 実装の参考先：https://tsubo.hatenablog.jp/entry/2020/06/15/124657

import heapq
# insert(x), 要素の挿入：O(logN)
# erase(x), 要素の削除：O(logN)
# is_exist(x), 要素の存在を確認：O(1)
# get_min(), 最小値の取得：O(1)

class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()

    def insert(self,x):
        heapq.heappush(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,"is not in HeapDict")
            exit()
        else:
            self.d[x]-=1

        while len(self.h)!=0:
            if self.d[self.h[0]]==0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]

    def __len__(self):
        return len(self.h)