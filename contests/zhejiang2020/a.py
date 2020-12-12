#!/usr/bin/env python3
'''
分析:
    三种情况: 
    202X XX XX
    X202 XX XX
    XXXX X2 02
    漏掉一个情况:
    XXX2 02 XX  +28或29!
#y202X = lambda y1,y2: min(y2-y1+1,10) if (y2>=y1 and y1<2030 and y2>2019) else 0
returns number of all candidate years (include partial years)
    普通完整年: +2
    特殊完整年: 365+leap
    小二完整年: 28+leap 
    特殊部分年: 所有天数(days)
    普通部分年: 0202, 1202是否在内!
    小二部分年: 
# make sure y2>y1+1
fullyeardays = lambda y1,y2: (y2-y1-1)*2            + \
        364*(sum([(i>y1 and i<y2) for i in s366]))  + \
        363*(sum([(i>y1 and i<y2) for i in s365]))
print(fullyeardays(2020,2025))
isleap = lambda y: (y%400==0) or (y%4==0 and y%100>0)
syears = [2020,2021,2022,2023,2024,2025,2026,2027,2028,2029] + [ 202,1202,2202,3202,4202,5202,6202,7202,8202,9202] 
'''

s365   = [     2021,2022,2023,     2025,2026,2027,     2029] + [ 202,1202,2202,3202,4202,5202,6202,7202,8202,9202] 
s366   = [2020,               2024,               2028]
ndays  = [None,31,28,31,30,31,30,31,31,30,31,30,31]
ldays  = [None,31,29,31,30,31,30,31,31,30,31,30,31]
feb2   = lambda m1,d1,m2,d2: (m1< 2 or (m1== 2 and d1<=2)) and (m2> 2 or (m2== 2 and d2>=2))
dec2   = lambda m1,d1,m2,d2: (m1<12 or (m1==12 and d1<=2)) and (m2>12 or (m2==12 and d2>=2))

ydays  = {}
for i in range(1000):
    ydays[i*10+2]     = 29 + (i%2)
for i in range(10):
    ydays[i*1000+202] = 365
    ydays[i+2020]     = 365
for y in s366:
    ydays[y] = 366

def pdays(y,m1,d1,m2,d2):   #partial year days!
    if m2<m1:
        return 0
    if y not in ydays:
        return feb2(m1,d1,m2,d2) + dec2(m1,d1,m2,d2)
    yt = ydays[y]
    if   yt == 365:
        return (ndays[m1]-d1+1) + sum([ndays[m] for m in range(m1+1,m2)]) + (d2)
    elif yt == 366:
        return (ldays[m1]-d1+1) + sum([ldays[m] for m in range(m1+1,m2)]) + (d2)
    else:   #28/29 case
        return 0 if (m1>2 or m2<2) else max(0, yt-(d1 if m1==2 else 0)-(yt-d2+1 if m2==2 else 0))

def f(l):
    y1,m1,d1,y2,m2,d2 = l
    if y2<y1:   #special case
        return 0
    if y1==y2:  #special case (make it FAST)
        return pdays(y1,m1,d1,m2,d2)
    c  = 0
    for y in range(y1+1,y2):
        c += ydays[y] if y in ydays else 2
    c += pdays(y1,m1,d1,12,31) 
    c += pdays(y2, 1, 1,m2,d2) 
    return c

t = int(input())
for _ in range(t):
    l   =  list(map(int,input().split()))
    print(f(l))

