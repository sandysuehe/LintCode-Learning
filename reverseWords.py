def reverseWords(s):
    s =s.strip(" ")
    print s
    mlist = s.split() 
    return " ".join(mlist[::-1])

s = "the sky is blue"
s = "  Life  doesn't  always    give     us  the       joys we want."
print reverseWords(s)
