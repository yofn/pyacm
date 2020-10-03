#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/E

concat  = lambda l1,l2: l1 + l2

def shuffle(l):
    pass

def f(s1,s2):
    r1 = eval(s1)
    r2 = eval(s2)
    return r1==r2

s1 = input()
s2 = input()
print('not equal' if not f(s1,s2) else 'equal')
