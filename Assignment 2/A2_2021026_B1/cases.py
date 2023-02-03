def function1(k):
    #function returns factorial of any number n
    output=1
    for i in range(1,k+1):
        output*=i
    return output

#print (function1(6))

def generateData():
    n=int(input('Enter the number of input-output pairs you would like to generate:'))
    for i in range(n):
        a=int(input('Enter input {} :'.format(i+1)))
        f1=open('Assignment 2\A2_2021026_B1\input {}.txt'.format(i+1),'w')
        f1.write(str(a))
        f2=open('Assignment 2\A2_2021026_B1\output {}.txt'.format(i+1),'w')
        f2.write(str(function1(a)))
        f1.close()
        f2.close()

generateData()        