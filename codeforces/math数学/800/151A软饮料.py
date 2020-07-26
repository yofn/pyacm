#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/151/A
# n=#人; k=#瓶; l=毫升; c=limes; d=slices; p=salt; nl/np = per toast 

n,k,l,c,d,p,nl,np = list(map(int,input().split()))
print(min((k*l)//(nl*n),(c*d)//n,p//(np*n)))
