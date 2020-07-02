#!/usr/bin/python3

'''
https://oi-wiki.org/basic/enumerate/
一个数组中的数互不相同，求其中和为  的数对的个数
'''

def numPairs2(l):
    pass

def numPairs(l):
    maxN = max(max(l),abs(min(l)))
    met  = [False]*(maxN*2+1)
    nop  = 0
    for i in l:
        if met[maxN-i] is True:
            nop +=1
        met[maxN+i] = True
    return nop

assert(numPairs([0,-1,1])==1)
assert(numPairs([0,-1,2])==0)
assert(numPairs([0,-1,1,2,-2])==2)
assert(numPairs([0,-1,1,2,-2,-3])==2)


print('all test passed!')
