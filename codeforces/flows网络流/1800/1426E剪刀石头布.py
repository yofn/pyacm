#!/usr/bin/env python3

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(max(a[0]+b[1]-n,0)+max(a[1]+b[2]-n,0)+max(a[2]+b[0]-n,0),min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0]))
