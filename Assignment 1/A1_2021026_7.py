def calculate_area(l,a,b,d):
   if (b-a)%d==0:
       def f(x):
           y=sum([int(x)**i for i in l])
           return y
       k=(b-a)%d
       def integralf(r1,r2):
           a=((r2-r1)/6)*( f(r1) + 4*f((r1+r2)/2) + f(r2))
           return a
       s=0    
       while a!=b:
           s+=integralf(a,a+d)
           a+=d
       return s   
l=[float(i) for i in input('Enter the elements of list in form of space separated real numbers:').split()] 
a=float(input("Enter a:"))
b=float(input('Enter b:'))
d=float(input('Enter c:'))
print ('Using simpsons 1/3 Algo, Area: ',calculate_area(l,a,b,d))
#end




