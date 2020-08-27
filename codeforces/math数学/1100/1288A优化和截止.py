#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1288/A
# 不等式1? 最小化x+(n+x)//(x+1); 因为n很大,所以不能一个个算.
# 不等式2: x+(n+x)//(x+1)<=d ==> n<=(d-x)(x-1) => (d+1)**2>=(4n+d%2)..
# 注意符号和题目反了..

def f(l):
    d,n = l     #d=deadline, n=program days!
    if n<=d:
        return True
    f   = (n<<2)+(d+1)%2    # +1 if d is even else 0
    return d>=((f-1)//(d+1))# a little trick on //: (d+1)>=(f-1)//(d+1)+1

q = int(input())
for _ in range(q):
    l = list(map(int,input().split()))
    print('YES' if f(l) else 'NO')
