#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1154/A

a   = list(map(int,input().split()))
abc = [max(a)-i for i in a]
abc.remove(0)
print(*abc)
     
