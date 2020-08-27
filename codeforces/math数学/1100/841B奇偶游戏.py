#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/841/B
# 思路1: 前缀和..
# 思路2: (错误)
#   1. 如果起始总和为奇,玩家2总是输,应为他不能改变总的奇偶性..
#   2. 如果起始总和为偶,但玩家1可以走一手,则总和又成了
# 思路3:
#   1. 玩家1每次都改变奇偶性; 玩家2改变不了奇偶性
# 思路4:
#   1. 起始总和为奇,玩家1直接赢
#   2. 起始总和为偶,玩家1如果能走一手将总和变为奇,下一手赢
#   3. 玩家2唯一的机会是全偶数

def f(l):
    return 'First' if sum([i%2>0 for i in l])>0 else 'Second'

_ = input()
l = list(map(int,input().split()))
print(f(l))
