def iter_p_adic(p, n):
    '''
    連続して増加するp進数をリストとして返す。nはリストの長さ
    return
    ----------
    所望のp進数リストを次々返してくれるiterator
    '''
    from itertools import product
    tmp = [range(p)] * n
    return product(*tmp)

# p=3, n=4なら(0,0,0,0)...(2,2,2,2)までの4**3通り