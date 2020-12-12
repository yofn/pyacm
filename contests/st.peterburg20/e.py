#!/usr/bin/python3
import math

n  = int(input())
mi = n-1
ab = lambda x: x if x>=0 else -x
for r in range(1, int(math.sqrt(n))+2): #1e6
    # Case 1: all same, n=c*r, %=0
    # Case 2: even r,    r//2 less, n=c*r -  r   //2, %=r//2
    # Case 3: odd r, (r-1)//2 less, n=c*r -  r   //2  %=(r+1)//2
    # Case 4: odd r, (r+1)//2 less, n=c*r - (r+1)//2, %=r//2
    c  = (n+r-1)//r
    rr = n%r
    cc = n%c
    if rr in [0,r//2,(r+1)//2] or cc in [0,c//2,(c+1)//2]:
        mi = min(ab(r-c),mi)
print(mi)
