def titleToNumber(s):
    n = len(s) 
    ans = 0

    for i in range(n):
        ans = ans*26 + (ord(s[i])-ord('A')) + 1
    return ans


print 'A', titleToNumber('A')
print 'Z', titleToNumber('Z')
print 'AB', titleToNumber('AB')
