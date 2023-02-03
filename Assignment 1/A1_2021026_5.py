#start
def getReverse(n):
    return (int(str(n)[::-1]))
def checkPalindrome(n):
    if n==int(str(n)[::-1]):
        return 'true' 
    else:
        return 'false'
def checkNarcissistic(n):
    a=len(str(n))
    l=[int(i)**a for i in str(n)]
    if sum(l)==n:
        return 'true'
    else:
        return 'false' 
def findDigitSum(n):
    if n>=0:
        k=sum([int(i) for i in str(n)])
        s=k
        while not(len(str(s))==1):
            s=sum([int(i) for i in str(s)])
            k=k+s
    return k        
def findSquareDigitSum(n):
    if n>=0:
        k=sum([int(i)**2 for i in str(n)])
        s=k
        while not(len(str(s))==1):
            s=sum([int(i)**2 for i in str(s)])
            k=s+k
    return k
while True:
    print ("-"*100)
    print (''' Hello User, welcome to the application.PLease select one of the following operations.
    1.Find Reverse of a number
    2.Check Whether a number is a palindrome or not.
    3.Check whether a number is a narcissistic number or not.
    4.Find the sum of digits of a number
    5.Find the sum of squares of digits of a number.
    6.Select 6 to exit the application.''')
    print ("-"*100)
    x=int(input('Select the desired option(1-6):'))
    if 1<=x<=5:
        n=int(input('enter your number:'))
        if x==1:
            print (getReverse(n))
        elif x==2:
            print (checkPalindrome(n))
        elif x==3:
            print (checkNarcissistic(n))
        elif x==4:
            print (findDigitSum(n))
        elif x==5:
            print (findSquareDigitSum(n))
    elif x==6:
        break 
#end        


