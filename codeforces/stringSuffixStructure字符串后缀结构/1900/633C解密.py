#!/usr/bin/env python3

#ref: book_DG!

c2i = {chr(i+ord('a')):i for i in range(26)}
NoL = 26
NoN = int(1e6)+3

def makeTree(pl):
    nxt = [[0]*NoL for _ in range(NoN)]  #keyword tree in S4.3.1@DG
    pid =  [0]*NoN      #ln = [0]*NoN; sts = [None]*NoN
    tot =   0           #track nodes in tree
    for pi in range(len(pl)):
        now = 0
        for c in pl[pi]:
            ci = c2i[c]
            if nxt[now][ci]==0:
                tot += 1
                nxt[now][ci]=tot
            now = nxt[now][ci]
        pid[now]= pi+1  #1-based pattern index! sln[now]= len(p)#used to mark end of string
    return nxt,pid,tot

mem = {}
def searchWithMemory(t,p,nxt,pid):  #a kind of dp; here solves the dict problem in S4.3.1@DG
    now = 0
    if p not in mem: mem[p]=False
    for j in range(p,len(t)):
        if pid[now]>0:  #if matched a pattern
            if j not in mem:
                searchWithMemory(t,j,nxt,pid)
            mem[p] = mem[p] or mem[j]
        ci = c2i[t[j]]
        if nxt[now][ci]==0:
            return False
        now = nxt[now][ci]
    return True

def f(t,pl):
    pd = {p.lower():p for p in pl}
    pl = list(pd.keys())
    t  = t[::-1]
    nxt,pid,tot = makeTree(pl)
    searchWithMemory(t,0,nxt,pid)
    #dp = [False]*len(t)
    return mem

_   =  input()
t   =  input()
pl  = [input() for _ in range(int(input()))]
print(f(t,pl))
