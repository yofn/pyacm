#!/usr/bin/env python3
'''
分析:
    三种情况: 
    202X XX XX
    X20X XX XX
    XXXX X2 02
    漏掉一个情况:
    XXX2 02 XX
#y202X = lambda y1,y2: min(y2-y1+1,10) if (y2>=y1 and y1<2030 and y2>2019) else 0
returns number of all candidate years (include partial years)
    普通完整年: +2
    特殊完整年: 365+leap
    特殊部分年: 区域年天数 
    普通部分年: 0202, 1202是否在内!
'''

s365   = [     2021,2022,2023,     2025,2026,2027,     2029] + [ 202,1202,2202,3202,4202,5202,6202,7202,8202,9202] 
s366   = [2020,               2024,               2028]
syears = [2020,2021,2022,2023,2024,2025,2026,2027,2028,2029] + [ 202,1202,2202,3202,4202,5202,6202,7202,8202,9202] 
ndays  = [None,31,28,31,30,31,30,31,31,30,31,30,31]     #normal
ldays  = [None,31,29,31,30,31,30,31,31,30,31,30,31]     #normal
isleap = lambda y: (y%400==0) or (y%4==0 and y%100>0)

def days(y,m1,d1,m2,d2):
    if m2<m1:
        return 0
    if m1==m2:
        return max(d2-d1+1,0)
    global ndays,ldays
    mdays = ldays if isleap(y) else ndays
    return (mdays[m1]-d1+1) + sum([mdays[m] for m in range(m1+1,m2)]) + (d2)

# make sure y2>y1+1
fullyeardays = lambda y1,y2: (y2-y1-1)*2            + \
        364*(sum([(i>y1 and i<y2) for i in s366]))  + \
        363*(sum([(i>y1 and i<y2) for i in s365]))
print(fullyeardays(2020,2025))

feb2 = lambda m1,d1,m2,d2: (m1< 2 or (m1== 2 and d1<=2)) and (m2> 2 or (m2== 2 and d2>=2))
dec2 = lambda m1,d1,m2,d2: (m1<12 or (m1==12 and d1<=2)) and (m2>12 or (m2==12 and d2>=2))

def f(l):
    y1,m1,d1,y2,m2,d2 = l
    if y2<y1:   #special case
        return 0
    if y1==y2:  #special case (make it FAST)
        return days(y1,m1,d1,m2,d2) if y1 in syears else (feb2(m1,d1,m2,d2) + dec2(m1,d1,m2,d2))
    c  = fullyeardays(y1,y2) if y2>y1+1 else 0
    c += days(y1,m1,d1,12,31) 
    c += days(y2, 1, 1,m2,d2) 
    return c

t = int(input())
for _ in range(t):
    l   =  list(map(int,input().split()))
    print(f(l))

