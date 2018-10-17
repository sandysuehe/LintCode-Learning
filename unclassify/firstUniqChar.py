def firstUniqChar(s):
    hash_map = {}
    for i in s:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1

    for i in s:
        if hash_map[i] == 1:
            return s.index(i)
    return -1
    
#s = "lintcode" 
s = "lovelintcode"
s = ""
s = "aa"
print firstUniqChar(s)
