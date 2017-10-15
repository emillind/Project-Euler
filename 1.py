from math import sqrt
from sys import stdin

def one():
    num = 1000
    sum = 0
    j = 0
    i = 0
    while i < num:
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
        i += 1
    print(sum)

if __name__ == '__main__':
    one()
