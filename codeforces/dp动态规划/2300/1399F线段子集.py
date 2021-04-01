#!/usr/bin/env python3
#https://codeforces.com/contest/1399/problem/F
# f(l,r)=max(f(l,r-1), max{Ri=r} f(l,Li-1)+f(Li,Ri)

def f(sl):
    sl.sort(key=lambda s:(s[1],-s[0]))
    tl  = sorted(list(set([s[0] for s in sl] + [s[1] for s in sl])))
    cd  = {tl[i]:i for i in range(len(tl))}
    csl = [[] for i in range(len(tl))]
    for s0,s1 in sl:
        csl[cd[s1]].append(cd[s0])
    dp  = [[len(csl[0])]] #dp[0][0]=1 or 0
    for r in range(1,len(tl)):
        dp.append(dp[-1]+[0])
        for li in csl[r]:  #use this to update all l before!
            dp[r][li] += 1
            for l in range(li):
                dp[r][l] = max(dp[r][l],dp[r][li]+dp[li-1][l])
    return dp[-1][0]

T = int(input())
for i in range(T):
    n  =  int(input())
    ll = [list(map(int,input().split())) for _ in range(n)]
    print(f(ll))

