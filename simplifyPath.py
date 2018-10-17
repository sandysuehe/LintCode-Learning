def simplifyPath(path):
    ans = []
    plist = path.split("/")
    for char in plist:
        if len(ans) != 0 and char == "..":
            ans.pop()
        elif char not in (".", "", ".."):
            ans.append(char)
    return "/" + "/".join(ans) 

path = "/a/./b/../../c/"
print simplifyPath(path)
