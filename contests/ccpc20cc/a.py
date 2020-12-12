#!/usr/bin/env python3
# 01 backpack!
 
prices  = [648,328,198,88,28, 6,1]
reward  = [388,198,128,58,28,18,8]
tot     = sum(prices)

states  = [0]*(tot+1)

for i in range(7):
    for j in range(tot,prices[i]-1,-1):
        states[j] = max(states[j-prices[i]]+reward[i], states[j])

n   = int(input())
print(states[n]+n*10)

