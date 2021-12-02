def sumnum(num1, num2, k):
    sum = 0
    for i in range(num1, num2+1):
        sum = sum + i**k
    return sum
        
def mainsum():
    a = 50
    b = 150
    k = 2
    print("Sum of %d power of numbers from %d to %d = %d" % (k,a,b, sumnum(a,b,k)))


mainsum()

