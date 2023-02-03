#start
print ("Provide the polynomial function's details:")
n=int(input("Enter the degree of polynomial:"))
if n==0:
    a,b,c=0,0,0
    d=float(input("Coeff 1:"))
elif n==1:
    a,b=0,0
    c=float(input("Coeff 1:"))
    d=float(input("Coeff 2:"))
elif n==2:
    a=0
    b=float(input("Coeff 1:"))
    c=float(input("Coeff 2:"))
    d=float(input("Coeff 3:"))
elif n==3:
    a=float(input("Coeff 1:"))
    b=float(input("Coeff 2:"))
    c=float(input("Coeff 3:"))
    d=float(input("Coeff 4:"))
l=int(input("Provide lower bound for x:"))
u=int(input("provide upper bound for x:"))
s=int(input("Provide the steps in which you wish to increment x:"))
def polynomial(x):
    k=round(a*(x**3) + b*(x**2) + c*(x) + d)
    return k
fmin=0   
for i in range(l,u+1,s):
    if i<fmin:
        fmin=i
#now we have got the least value of function for our plot 
#so now we can scale our graph using that as reference
for i in range(l,u+1,s):
    if polynomial(i)<0:
        s1=abs(fmin)
        s2=abs(polynomial(i))
        space=s1-s2
        print (" "*space + s2*"*" + "|")
    elif polynomial(i)>=0:
        space=abs(fmin)
        print (" "*space + "|" + "*"*polynomial(i))
#end        

        
    
    






