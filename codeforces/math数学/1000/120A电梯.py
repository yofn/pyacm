#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/120/C
# input.txt
# output.txt


d,r = [line.rstrip() for line in open('./input.txt')]
left = (d=='front' and r=='1') or (d=='back' and r=='2')
with open('./output.txt','w') as f:
    f.write('L' if left else 'R')
