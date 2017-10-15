from math import sqrt
from sys import stdin

def isprime(int):
    if int == 2:
        return True
    cond = int/2
    x = 2
    while x <= cond:
        if int % x == 0:
            return False
        x += 1
    return True

def nextprime(current):
    i = current + 1
    while True:
        if isprime(i):
            return i
        i += 1

def three():
    num = 600851475143
    p = 1
    if isprime(num):
        print(num)
    else:
        while not isprime(num):
            p = nextprime(p)
            if num % p == 0:
                num = num / p
        print(num)

if __name__ == '__main__':
    three()
