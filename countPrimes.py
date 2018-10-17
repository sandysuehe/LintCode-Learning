def countPrimes(n):
    if n < 3:
        return 0
    
    primes = [True] * (n-1)
    primes[0] = False
    primes[1] = False

    import math
    for i in range(2, int(math.sqrt(n))+1):
        if primes[i]:
            for j in range(i*i, n-1, i):
                primes[j] = False

    print sum(primes)
        
countPrimes(10)
