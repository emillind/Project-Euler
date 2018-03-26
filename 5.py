from math import sqrt
from sys import stdin

def five():
    highestdivider = 20
    number = highestdivider
    while True:
        if divisible_by_all(number, highestdivider):
            print(str(number))
            return
        number += highestdivider

def divisible_by_all(number, highestdivider):
    if not divisible(number, 2):
        return False
    for i in range(int(highestdivider/2)+1, highestdivider+1):
        if not divisible(number, i):
            return False
    return True

def divisible(number, divider):
    return number % divider == 0

if __name__ == '__main__':
    five()
