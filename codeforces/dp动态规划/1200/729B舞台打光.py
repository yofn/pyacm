#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/729/B
#四个方向分别做,应该会容易些
#python nested list 不太适合做二维数组用, cf不支持numpy; 所以还是回到一维数组吧
#1000*1000也会超时? 分析下时间复杂度!
#改用高效点的实现 (采用预处理!!! 不仅高效而且简化了处理逻辑)
#用Python3.7还是超时; 用PyPy总算通过..

n,m = list(map(int,input().split()))
ss  = [list(map(int,input().split())) for _ in range(n)]
ll  = []
ll.append([ss[i][j] for i in range(n) for j in range(m)])           #(t-d)(l-r)
ll.append([ss[i][j] for i in range(n) for j in range(m-1,-1,-1)])   #(t-d)(r-l)
ll.append([ss[i][j] for j in range(m) for i in range(n)])           #(l-r)(t-d)
ll.append([ss[i][j] for j in range(m) for i in range(n-1,-1,-1)])   #(l-r)(b-t)
cnt = 0
for t in range(4):
    l       = ll[t] 
    run,nor = (m,n) if t<2 else (n,m)
    for r in range(nor):
        rs  = r*run
        ho  = 0     #0 for no object!
        for i in range(run):
            if l[rs+i] == 1:
                ho  = 1
                continue
            cnt += ho
print(cnt)
