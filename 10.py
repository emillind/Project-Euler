from math import sqrt
from sys import stdin

def ten():
    number = 2000000
    sum = 0
    a = [True] * number
    for i in range(2, int(sqrt(number)+1)):
        if a[i]:
            for j in range(i*i, number, i):
                a[j] = False
    for i in range(2, number):
        if a[i]:
            sum += i
    print(sum)

if __name__ == '__main__':
    ten()
