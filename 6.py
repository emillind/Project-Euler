from math import sqrt
from sys import stdin

def six():
    maxnumber = 100
    sum_of_squares = sum_squares(maxnumber)
    square_of_sum = square_sum(maxnumber)
    print(str(square_of_sum - sum_of_squares))

def sum_squares(number):
    sum = 0
    for i in range(1,number+1):
         sum += i*i
    return sum

def square_sum(number):
    if number % 2 == 0:
        sum = number*number/2 + number/2
    else:
        number -= 1
        sum = number*number/2 + number/2 + (number + 1)
    return sum*sum

if __name__ == '__main__':
    six()
