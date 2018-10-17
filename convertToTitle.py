def convertToTitle(n):
    charlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    if n <= 0:
        return res
    while n:
        res = charlist[(n-1)%26] + res 
        n = (n-1)/26
    return res



print 1, convertToTitle(1)
print 26, convertToTitle(26)
print 27, convertToTitle(27)
print 53, convertToTitle(53)
print 54, convertToTitle(54)
