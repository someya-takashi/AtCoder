# https://atcoder.jp/contests/abc102/tasks/arc100_a

N = int(input())
A = list(map(int, input().split()))

def sum_b(b):
    result = 0
    for i in range(N):
        result+=abs(A[i] - (b+i+1))

    return result

l = -10**10
r = 10**10
mid = (l+r) // 2

while abs(mid-l) > 1 or abs(mid-r) > 1:
    lb = sum_b(l)
    rb = sum_b(r)
    mb = sum_b(mid)
    # print(lb, mb, rb)
    # print(l, mid, r)

    if rb < lb:
        l = mid
        mid = (l+r) // 2
    elif rb == lb:
        mid = (l+r) // 2
        break
    else:
        r = mid
        mid = (l+r) // 2

print(min(sum_b(l), sum_b(mid), sum_b(r)))