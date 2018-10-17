def concatenetedString(s1, s2):
    hash_set = set()
    for i in s2:
        hash_set.add(i)

    hash_set1 = set()
    for j in s1:
        if j in hash_set:
            s1 = s1.replace(j, "")
            hash_set1.add(j)

    for k in s2:
        if k in hash_set1:
            s2 = s2.replace(k, "")
    return s1+s2
    
s1 = "aacdb"
s2 = "gafd"
s1 = "abcs"
s2 = "cxzca"
print concatenetedString(s1, s2)
