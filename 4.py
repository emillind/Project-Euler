from math import sqrt
from sys import stdin

def four():
    best = 0
    for i in range(100,1000):
        for j in range(100,1000):
            current = i*j
            if current > best:
                if str(current) == str(current)[::-1]:
                    best = current
    print(best)

if __name__ == '__main__':
    four()
