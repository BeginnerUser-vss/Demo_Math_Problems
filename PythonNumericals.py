# Python program to convert decimal numbers to octal number

def decToOct(n):
    print(oct(n))
 
n = 33
decToOct(n)

# Python program to reverse an integer

def reverseInteger(integer):
    result=0

    while integer!=0:
        remainder = integer % 10
        result = result * 10 + remainder
        integer //= 10

    return result

print("The reverse of 43 is ",reverseInteger(43))

# Python Program to print Fibonacci series with Recursive method 

def recursiveFibo(n):
    if n<=1:
        return n
    else:
        return (recursiveFibo(n-1)+recursiveFibo(n-2))

fiboNum = 9
print("The fibonacci series of number",fiboNum)
print(recursiveFibo(fiboNum))

for i in range(fiboNum+1):
    print(recursiveFibo(i))






    
