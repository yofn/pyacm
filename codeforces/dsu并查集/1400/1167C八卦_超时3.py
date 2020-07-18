#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1167/C
# PyPy超时@4, Py超时@6
# 不用dsu, 用tree会不会快点?
# union的时候用tree来union会不会快点??
# NOTE: 修改了DisjointSet的实现, find的时候compress的厉害些! (结果4都过不了..原来能到6)
# 不用压缩,反而过了Case4; ..但还是没过Case6(5e5,5e5)
# 继续优化,但好像与算法没太大关系了..
# 尽力了,实在过不了~~~这就是为什么竞赛的时候大家都用C++!

@profile
def main():
    n,m     = list(map(int,input().split())) #5e5, 5e5
    parents = list(range(n))
    ranks   = [0]*n
    sizes   = [1]*n
    for _ in range(m):
        g   = list(map(int,input().split()))
        if g[0]==0:
            continue
        rs,rl = g[0],g[1:]
        pi,ss = 1,2     #pair interval and step size
        while pi < rs:
            for ii in range(0,rs-pi,ss):
                i,j = rl[ii]-1,rl[ii+pi]-1
                while parents[i]!=i:
                    i   = parents[i]
                while parents[j]!=j:
                    j   = parents[j]
                if i==j:
                    continue
                rd  = ranks[i] - ranks[j]
                if   rd == 0:       # Increment repr0's rank if both nodes have same rank
                    ranks[i] += 1
                elif rd <  0:       # Swap to ensure that repr0's rank >= repr1's rank
                    i,j = j,i
                parents[j]  = i   #merge
                sizes[i]   += sizes[j]
                sizes[j]    = 0
            pi = ss
            ss = ss<<1
    for i,s in enumerate(sizes):
        if s>0:
            continue
        j   = i
        jl  = [j] 
        while parents[j]!=j:
            j = parents[j]
            jl.append(j)
        s   = sizes[j]
        for j in jl[:-1]:
            sizes[j] = s
    print(*sizes)    #final sizes

main()
