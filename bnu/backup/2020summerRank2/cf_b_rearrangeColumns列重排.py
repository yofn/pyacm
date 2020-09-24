#!/usr/bin/env python3

# 2020暑期排位2B
r1 = input()
r2 = input()
m1cnt,m2cnt,mbcnt,m0cnt = 0,0,0,0
for i in range(len(r1)):
    if   r1[i]=='#' and r2[i]=='#':
        mbcnt += 1
    elif r1[i]=='#':
        m1cnt += 1
    elif r2[i]=='#':
        m2cnt += 1
    else:
        m0cnt += 1
if mbcnt == 0 and (m1cnt>0 and m2cnt>0):
    print('NO')
else:
    print('YES')
    print('#'*(m1cnt+mbcnt) + '.'*(m2cnt+m0cnt))
    print('.'*m1cnt + '#'*(mbcnt+m2cnt) + '.'*m0cnt)

