from math import sqrt
from sys import stdin

def two():
    previous = 1
    current = 2
    i = 0
    sum = 2
    while current < 4000000:
        temp = previous
        previous = current
        current += temp
        if current%2 == 0:
            sum += current
        i += 1
    print(sum)

if __name__ == '__main__':
    two()
