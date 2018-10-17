def isValidParentheses(s):
    stack = []
    for char in s:
        if char in ("{", "[", "("):
            stack.append(char)
        else:
            if not stack:
                return False
            if char == "]" and stack[-1] != "[":
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            stack.pop()
    return not stack 


#s = "()[]{}"
s = "([)]"
s = "]"
s = "([{}])"
s = "["
print isValidParentheses(s)
