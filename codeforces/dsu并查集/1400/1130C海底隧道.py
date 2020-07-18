#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1130/C
# t11超时, n=50
# kernprof -l -v  ..
# 优化下嵌套的for
# 只考虑边缘.? OK!
# 是否dfs更好??

class DisjointSet:      #only support query, NO construction supported
    def __init__(self, n):
        self.num_sets   = n         #--@union
        self.parents    = list(range(n))
        self.ranks      = [0] * n
        self.sizes      = [1] * n   #used@union: size of set@root! 0 if NOT repsentive

    def find(self,j): #no compress
        while self.parents[j]!=j:
            j   = self.parents[j]
        return j

    def union(self,i,j):
        i   = self.find(i)
        j   = self.find(j)
        if i == j:
            return False
        rd  = self.ranks[i] - self.ranks[j]
        if   rd == 0:       # Increment repr0's rank if both nodes have same rank
            self.ranks[i] += 1
        elif rd <  0:       # Swap to ensure that repr0's rank >= repr1's rank
            i, j = j, i
        self.parents[j]  = i   #merge
        self.sizes[i]   += self.sizes[j]
        self.sizes[j]    = 0
        self.num_sets   -= 1
        return True

#@profile
def main():
    n   = int(input())  #50
    n2  = n*n
    p1  = list(map(int,input().split()))
    p2  = list(map(int,input().split()))
    ll  = [c=='0' for c in ''.join([input() for _ in range(n)])]  #land list
    dsu = DisjointSet(n2)
    for i in range(n2):
        if ll[i]:
            if i>=1 and i%n>0 and ll[i-1]: # with left
                dsu.union(i,i-1)
            if i>=n and ll[i-n]:    # with upper
                dsu.union(i,i-n)
    r1  = dsu.find((p1[0]-1)*n+p1[1]-1)
    r2  = dsu.find((p2[0]-1)*n+p2[1]-1)
    mc  = 2*n2
    l1  = []
    l2  = []
    for i in range(n2):
        if ll[i] and not(                               \
                i>=1     and i%n>0   and ll[i-1] and    \
                i>=n     and ll[i-n] and                \
                i%n!=n-1 and ll[i+1] and                \
                i+n<n2   and ll[i+n]):  # not (all neighbors=True)
            if dsu.find(i)==r1:
                l1.append((i//n,i%n))
            if dsu.find(i)==r2: #r1 might = r2!
                l2.append((i//n,i%n))
    for x1,y1 in l1:
        for x2,y2 in l2:
            cost = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
            if cost < mc:
                mc = cost
    print(mc)
main()

