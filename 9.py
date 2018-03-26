from sys import stdin

def nine():
    answer = 1000
    for i in range(1, int(answer/3)):
        for j in range(i+1, int((answer-i)/2)):
            k = answer-j-i
            if (i*i + j*j) ==  k*k:
                print(i*j*k)

if __name__ == '__main__':
    nine()
