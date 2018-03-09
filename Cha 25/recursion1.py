# Sissi Xu S3C2
def factorial(n):
    if n==1:
        return 1
    return factorial(x-1)*x

def count7(n):
    if n // 10 == 0:
        if n == 7:
            return 1
        return 0
    if n % 10 == 7:
        return 1 + count7(n//10)
    return count7(n//10)

def count8(n):
    if n / 10 <= 0:
        return 0
    if n % 10 == 8:
        return 1 + count8(n // 10)
    elif n % 10 == 8 and n % 100 // 10 == 8:
        return 2 + count8(n // 10)
    else:
        return count8(n // 10)

def powerN(base, n):
    if n == 1:
        return base
    else:
        return base * powerN(base, n-1)

def countX(str):
    if len(str) == 0:
        return 0
    elif str[0] == "x":
        return 1 + countX(str[1:])
    else:
        return countX(str[1:])

def countHi(str):
    if len(str) < 2:
        return 0
    elif str[0] + str[1] == "hi":
        return 1
    elif str[0:2] == "hi":
        return 1 + countHi(str[2:])
    else:
        return countHi(str[1:])

def changeXY(str):
    if len(str) == 0:
        return ""
    elif str[0] == "x":
        return "y" + changeXY(str[1:])
    else:
        return str[0] + changeXY(str[1:])

def changePi(str):
    if len(str) < 2:
        return str
    elif str[0:2] == "pi":
        return "3.14" + changePi(str[2:])
    else:
        return str[0] + changePi(str[1:])

def noX(str):
    if len(str) == 0:
        return ""
    elif str[0] == "x":
        return noX(str[1:])
    else:
        return str[0] + noX(str[1:])

def array6(nums, n):
    if len(nums) == 0:
        return False
    elif nums[n] == 6:
        return True
    else:
        return array6(nums, n+1)

def array11(nums, n):
    if len(nums) == 0:
        return 0
    elif nums[n] == 11:
        return 1 + array11(nums, n+1)
    else:
        return array11(nums, n+1)

def array220(nums, n):
    if len(nums) < 2:
        return False
    elif (nums[n + 1]) / (nums[n]) == 10:
        return True
    else:
        return array220(nums, n+2)

def allStar(str):
    if len(str) <= 1:
        return str
    else:
        return str[0] + "*" + allStar(str[1:])

def pairStar(str):
    if len(str) <= 1:
        return str
    elif str[0] == str[1]:
        return str[] + "*" + str[1] + pairStar(str[2:])
    else:
        return str[0] + pairStar(str[1:])

def endX(str):
    if len(str) <= 1:
        return str
    elif str[0] == "x":
        return endX(str[1:]) + "x"
    else:
        return str[0] + endX(str[1:])

def countPairs(str):
    if len(str) < 2:
        return 0
    elif str[0] == str[2]:
        return 1 + countPairs(str[1:])
    else:
        return countPairs(str[1:])

def countAbc(str):
    if len(str) < 3:
        return 0
    elif str[0:3] == "abc" or str[0:3] == "aba":
        return 1 + countAbc(str[1:])
    else:
        return countAbc(str[1:])

def count11(str):
    if len(str) < 2:
        return 0
    elif str[0:2] == "11":
        return 1 + count11(str[2:])
    else:
        return count11(str[1:])

def stringClean(str):
    if len(str) <= 1:
        return str
    elif str[0] == str[1]:
        return stringClean(str[1:])
    else:
        return str[0] + stringClean(str[1:])

def countHi2(str):
    if len(str) < 2:
        return 0
    if str[0:3] == "xhi":
        return countHi2(str[3:])
    elif str[0:2] == "hi":
        return counthi2(str[2:])
    else:
        return countHi2(str[1:])

def nestParen(str):
    if len(str) <= 2:
        if str == '()':
            return True
        else:
            return False
    if str[0] == '(' and str[-1] == ')':
        return nestParen(str[1:-1])
    else:
        return False

def strCount(str, sub):
    if len(str) < len(sub):
        return 0
    elif str[0:len(sub)] == sub:
        return 1 + strCount(str[len(sub):], sub)
    else:
        return strCount(str[1:], sub)

def strCopies(str, sub, n):
    if len(str) < len(sub):
        if n == 0:
            return True
        else:
            return False
    elif str[0:len(sub)] == sub:
        return strCopies(str[len(sub):], sub, n-1)
    else:
        return strCopies(str[1:], sub, n)
