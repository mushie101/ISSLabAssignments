
# Leap Year

def isLeapYear (x):
    if x % 4 == 0:
        if (x % 100 == 0) and (x % 400 == 0):
            return True
        else:
            return False
    else:
        return False

print(isLeapYear(1900))
