# 問題:https://atcoder.jp/contests/abc102/tasks/arc100_a
# 解説:https://drken1215.hatenablog.com/entry/2019/12/22/122300

# |x-a|+|x-b|+|x-c|....の最小値はa,b,c...の中央値になる
# 従って、a,b,cをソートし、中央値を求めれば、O(NlogN)で解ける