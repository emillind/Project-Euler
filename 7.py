from math import sqrt
from sys import stdin

def seven():
    xth_prime = 10001
    count = 1
    number = 1
    while count < xth_prime:
        number += 2
        if is_prime(number):
            count += 1
    print(number)

def is_prime(int):
    cond = int/2
    x = 3
    while x <= cond:
        if int % x == 0:
            return False
        x += 2
    return True

if __name__ == '__main__':
    seven()
