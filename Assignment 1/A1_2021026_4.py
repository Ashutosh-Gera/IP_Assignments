def F1(b1):
    return b1 and (not b1)
def F2(b1,b2,b3):
    return (b1 or b2) and (b2 or (not b3)) 
a=int(input('''Choose your function
1. F1
2. F2
: ''')) 
if a==1:
    b1=bool(input('Enter b1:'))
    if F1(b1)==True:
        print ('F1 is Satisfiable') 
        print (bool(b1), bool(not b1))
    else:
        #This expression(F1) is unsatisfiable
        print ('Unsatisfiable')
if a==2:
    b1=bool(input('Enter b1:'))
    b2=bool(input('Enter b2:'))
    b3=bool(input('Enter b3:'))
    if F2(b1,b2,b3)==True:
        print ('F2 is Satisfiable')
        print (bool(b1), bool(b2), bool(b3))
    else:
        #This expression (F2) is unsatisfiable
        print ('Unsatisfiable')    


