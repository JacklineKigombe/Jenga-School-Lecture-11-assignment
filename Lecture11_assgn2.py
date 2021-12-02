def sumnum(num1, num2):
    sum = 0
    for i in range(num1, num2+1):
        sum = sum + i
    return sum

def mainsum():
    a = 50
    b = 150
    print("Sum of the numbers from %d to %d = %d" % (a,b, sumnum(a,b)))


mainsum()
