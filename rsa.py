#!/usr/bin/python3


import sys
import random
import time


def is_prime(num, k=20):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False

    d = num - 1
    r = 0
    while d % 2 ==0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, num - 2)
        x = pow(a,d,num)
        if x == 1 or x == num -1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        exit()
