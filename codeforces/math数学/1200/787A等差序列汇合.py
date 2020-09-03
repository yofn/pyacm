#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/787/A
#求n st. n%a=b%a, n%c=d%c
#暴搜(0-lcm(a,c))之间的数?
#   t   = max(a,c)
#解法和答案不太一样: https://codeforces.com/blog/entry/51163

gcd = lambda a,b: a if b==0 else gcd(b,a%b)
lcm = lambda a,b: a*b//(gcd(a,b) if a>b else gcd(b,a))

def f(l1,l2):
    a,b = l1
    c,d = l2
    s   = max(b,d)
    e   = s + lcm(a,c) + 1
    i   = s
    while i < e:
        if (i-b)%a==0 and (i-d)%c==0:
            return i
        i += 1  # not optimized, but work?
    return -1

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(f(l1,l2))
