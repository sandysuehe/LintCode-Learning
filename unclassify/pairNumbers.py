def pairNumbers(p):
    n = len(p)
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (p[i][0] + p[j][0]) % 2 == 0 and (p[i][1] + p[j][1]) % 2 == 0:
                count += 1
    return count

#p = [[1,2],[3,4],[5,6]]
p = [[0,3],[1,1],[3,4],[5,6]]
print pairNumbers(p)
