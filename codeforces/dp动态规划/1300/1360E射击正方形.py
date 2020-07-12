#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1360/E
#判断射击结果图是真还是假!
#注意confidence的传递次序.
#从边界做bfs? 或者记忆化搜索DP? 哪个比较高效?
#从右下角开始斜着扫描也可以?

def okay(s,n):
    for sij in range(2*n-2,-1,-1):
        ijl = [(i,sij-i) for i in range(n) if sij>=i and sij<=i+(n-1)]
        for i,j in ijl:
            if i<n-1 and j<n-1 and s[i][j]>s[i+1][j]+s[i][j+1]:
                return False 
    return True

t = int(input())        #1000
for _ in range(t):
    n   = int(input())  #50
    s   = [[int(c) for c in input()] for i in range(n)]
    print('YES' if okay(s,n) else 'NO')

