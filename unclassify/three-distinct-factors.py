#https://www.lintcode.com/problem/three-distinct-factors
import math
def isThreeDisctFactors(n):
    if n < 2:
        return False
    num = int(math.sqrt(n))

    # judge n is a square number
    if  num ** 2 == n:
        if isprime(num):
            return True
        else:
            return False
    else:
        return False

# judge n is a prime 
def isprime(num):
    if num < 2:
        return False
    sqrt_num = int(math.sqrt(num))
    for i in range(2, sqrt_num):
        if num % i == 0:
            return False
    return True

n = 9
n = 10000001400000049
print isThreeDisctFactors(n)
