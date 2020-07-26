#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/47/A
# n=500,所以用模拟也是可以的..

import math
n   = int(input())
x   = int((math.sqrt((n<<3)+1)-1)/2)
print('YES' if n-(x*(x+1))//2==0 else 'NO')
