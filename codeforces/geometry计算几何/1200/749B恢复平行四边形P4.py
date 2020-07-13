#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/749/B
#只剩三个点..恢复出所有可能的第四点
#对每个点找对面的点!

pl = [list(map(int,input().split())) for _ in range(3)]
xl = [p[0] for p in pl]
yl = [p[1] for p in pl] 
s4 = set([(sum(xl)-(xl[i]<<1),sum(yl)-(yl[i]<<1)) for i in range(3)])
print(len(s4))
[print(*s) for s in s4]
