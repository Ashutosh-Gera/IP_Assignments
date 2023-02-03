from cases import function1,generateData
def function2(k):
    #calculates factorial of a number using recursion
    if k==1:
        return 1
    else:
        return k*function2(k-1)    

#print (function2(6))

def testing():
    n=int(input('Enter the number of input-output pairs to be tested:'))
    flag=True 
    for i in range(n):
        f3=open('Assignment 2\A2_2021026_B1\input {}.txt'.format(i+1),'r')
        a=int(f3.read())
        b=function2(a)
        f4=open('Assignment 2\A2_2021026_B1\output {}.txt'.format(i+1),'r')
        c=int(f4.read())
        if b==c:
            pass
        else:
            flag=False

    if flag:
        return 'SUCCESS'
    return 'FAILED'

print (testing())




    


