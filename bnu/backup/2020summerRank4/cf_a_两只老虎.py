#!/usr/bin/env python3

# 2020暑期排位4A两只老虎
# https://codeforces.com/group/H9K9zY8tcT/contest/286003/problem/A
# il = ['2-','4-','6-','7-','2','4','6','7','2+','4+','6+','7+'] 

n       = int(input())
notes   = input()
nl = notes.split(' ')
el = ['5--','1-','3-','5-','1','3','5','1+','3+','5+','1++','3++'] 
al = ''
for n in nl:
    if   n == '0':
        al += 'X'
    elif n in el:
        al += 'E'
    else:
        al += 'I'
print(''.join(al))

