# 10**5個のクエリなど、入力に時間がかかってしまう場合に使うとTLEを防げる
# https://atcoder.jp/contests/typical90/tasks/typical90_bl などで通常のinputではTLEになった

import sys
input = sys.stdin.readline


# メモ化再帰
from functools import lru_cache
@lru_cache(maxsize=None)
def dfs():
    return