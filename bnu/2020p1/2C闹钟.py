#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1354/A
# 之前做过: bnu/2020summerTraining1/cf_a_alarm闹钟.py 
# 这次写的更好些!!

def f(l):
    a,b,c,d = l     #a=target sleep time, b=1st alarm; c=later alarms; d=time2fall sleep
    if b>=a:
        return b    #enough@1st alarm!
    if c<=d:
        return -1   #no chance to get target sleep time!
    non = (a-b+c-d-1)//(c-d)
    return b + non*c

t  = int(input())
for _ in range(t):
    l = list(map(int,input().split()))
    print(f(l))

