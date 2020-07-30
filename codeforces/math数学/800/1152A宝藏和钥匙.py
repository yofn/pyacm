#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1152/A

n,m = list(map(int,input().split()))
al  = list(map(int,input().split()))
bl  = list(map(int,input().split()))
cae = sum([a%2==0 for a in al])
cao = sum([a%2==1 for a in al])
cbe = sum([b%2==0 for b in bl])
cbo = sum([b%2==1 for b in bl])
print(min(cae,cbo)+min(cao,cbe))
