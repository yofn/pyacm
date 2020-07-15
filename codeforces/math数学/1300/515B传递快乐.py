#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/515/B
#n个男孩,m个女孩; i天, i男孩和i女孩聚会, 有一人快乐另一人则也会变快乐
#问会不会都快乐!
#可以暴力,但应该有更优雅的数学解
#Let g = greatest common divisor of n and m.
#If i-th person is happy, then all people with number x satisfying x=i%g will become happy some day because of this person.
#测试用例2有问题??!

def allHappy(ubl,ugl,n,m):
    if len(ubl)==0 or len(ugl)==0: return True
    gcd = lambda a,b: b if a%b==0 else gcd(b,a%b)
    g   = gcd(n,m)
    hbl = [False]*g #happy lists
    hgl = [False]*g
    for i in range(n):
        if i not in ubl:
            hbl[i%g] = True
    for i in range(m):
        if i not in ugl:
            hgl[i%g] = True
    #print(ubl,ugl,g,hbl,hgl)
    return not (False in [(hbl[i] or hgl[i]) for i in range(g)])

n,m = list(map(int,input().split())) #100
ubl = list(map(int,input().split())) #unhappy boys
ugl = list(map(int,input().split())) #unhappy girls

print('Yes' if allHappy(ubl[1:],ugl[1:],n,m) else 'No')

