#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297617
#DP?
#this subsequence is wild. 2^n?

i2c = lambda i: chr(ord('a')+i)

def f(l):
    tc = 0  #total count
    cc = 0  #continued count
    cl = {i2c(i):0 for i in range(26)}  #cl with each char!
    for c in l:
        cc   -= cl[c] #same! can't continue, others okay!
        cc   += 1    #new char is okay!
        cl[c] = 1    #new c as continuous
        tc   += cc
        #print(cc,tc)
    return tc + 2

l = list(input())
print(f(l))
