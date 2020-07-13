#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/11178/B
#need a state machine to be clear!
#state: 'S', 'W', 'WO'
#trans:
#   1. 'S---meet vv--->W'; 
#   2. 'W---meet vv--->W'; #update w,wow
#   3. 'W---meet o--->WO'; #update wo
#   4. 'WO--meet o--->WO'; #update wo
#   5. 'WO--meet vv--->W'; #update w,wow
# could be simplified into update logic on w/wow and wo respectively!
# 注意人类可能习惯使用乘法/把o和w合起来算,而算法上简单的实现正好相反!!!
# 计算思维的好例子! (对比数学..数学相当于CISC,而算法可能是RISC!)
# 一开始想用w-list,o-list来记录连续的o和w,发现是错误的做法;所以开始画状态机,画出状态机后才发现逻辑可大大简化..

s    = input()  #1e6
w    = 0
wo   = 0
wow  = 0
for i in range(1,len(s)):
    if s[i]=='v' and s[i-1]=='v':
        w   += 1
        wow += wo
        continue
    if s[i]=='o':
        wo  += w
print(wow)
