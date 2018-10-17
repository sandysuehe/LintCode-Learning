def hammingWeight(n):
    res = 0
    if n <= 0:
        return res
    while n:
        count = n % 2
        n = n / 2
        res += count
    return res

n = 11
print hammingWeight(n)
