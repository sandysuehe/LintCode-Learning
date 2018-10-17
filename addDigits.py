def addDigits(num):
    if num / 10 == 0:
        return num
    count = 0
    while num:
        count +=  num % 10
        num = num / 10
    return addDigits(count)
    
num = 38
num = 100 
print addDigits(num)
