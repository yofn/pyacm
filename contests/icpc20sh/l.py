#!/usr/bin/python3
#@profile

gcd = lambda a,b: a if b==0 else gcd(b,a%b)
dis = lambda x,y: (x*x+y*y)**0.5

def f(n,m): #n>m
    if gcd(n,m)==1:
        return dis(n,m)
    ans = n+m
    for i in range(1,m):
        j   = (n*i-1)//m
        d   = dis(i,j) + dis(m-i,n-j)
        ans = min(ans,d)
    return ans

T   = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    print(f(n,m) if n>m else f(m,n))
