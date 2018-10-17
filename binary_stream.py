def getOutput1(s):
    cur = 0
    n = len(s)
    mlist = []
    for i in xrange(n):
        cur = (cur*2 + int(s[i])) % 3
        if cur % 3 == 0:
            mlist.append(i+1)
    return mlist

s = "11011"
#s = "0000"
print getOutput1(s)
