#!/usr/bin/python3

'''
https://oi-wiki.org/basic/enumerate/
求小于N的最大素数
'''


def isPrime(n):
    for i in range(2,n//2):
        if n%i == 0:
            return False
    return True

def largestPrime(n):
    if type(n) is not int:
        return False
    if n<1:
        return None
    for i in range(n-1,0,-1):
        if isPrime(i):
            return i
    return None

assert(largestPrime(2)==1)
assert(largestPrime(1)==None)
assert(largestPrime(1.1)==False)
assert(largestPrime(10)==7)
assert(largestPrime(16)==13)
assert(largestPrime(50)==47)


print('all test passed!')
