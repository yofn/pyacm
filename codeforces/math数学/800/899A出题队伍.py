#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/899/A

n   = int(input())
al  = list(map(int,input().split()))
n2  = sum([a==2 for a in al])
n1  = n-n2
print(min(n1,n2)+max(n1-n2,0)//3)
