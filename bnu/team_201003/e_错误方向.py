#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297617
#DP?
#this subsequence is wild. 2^n?
#need a 2D table?

i2c = lambda i: chr(ord('a')+i)
c2i = lambda c: ord(c)-ord('a')

def f(l):
    tc = 1      #total count
    cl = [0]*26 #count of str with c in it!
    for c in l:
        i       = c2i(c)
        cc      = tc-cl[i]  #count of str without c in it!
        cl[i]  += cc        #now insert cc+c into cl!
        # TODO need to update cl[j]!
        tc     += cc
        print(cc,tc)
    return tc%11092019

l = list(input())
print(f(l))
