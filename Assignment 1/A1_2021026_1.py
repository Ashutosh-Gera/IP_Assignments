#start
print ('''Choose the type of pattern by entering the number beside it:
1.Right-angled triangle
2.Isosceles triangle
3.Kite
4.Half Kite
5.X''')
a=int(input("Enter the number beside your desired pattern:"))
n=int(input('Enter the value of n:'))
if a==1:
    for i in range(1,n+1):
        l=[int(j) for j in range(1,i+1)]
        print (*l)
elif a==2:
    if n%2==0:
        k=0
        for i in range(1,2*n,2):
           l=[str(j) for j in range(1,i+1)]
           s=''.join(l)
           space=n-k
           print (" "*space + s + " "*space)
           k=k+1
elif a==3:
    if n%2==0:
        k=0
        for i in range(1,2*n,2):
           l1=[str(j) for j in range(1,i+1)]
           s1=''.join(l1)
           space=n-k
           print (" "*space + s1 + " "*space)
           k=k+1
        for i in range((2*n)-3,0,-2):
           l2=[str(j) for j in range(1,i+1)]
           s2=''.join(l2)
           space=int(n-((i+1)/2)) 
           print (' '*space,s2)
elif a==4:
    for i in range(1,n+1):
        l=[int(j) for j in range(1,i+1)]
        print (*l)
    for i in range(n-1, 0,-1):
        l=[int(j) for j in range(1,i+1)]
        print (*l)
elif a==5:
    k=0
    for i in range((2*n)-1, 2,-2):
        l=[str(j) for j in range(1,i+1)]
        s=''.join(l)
        print (' '*k,s)
        k+=1
    k=0
    for i in range(1,2*n,2):
           l=[str(j) for j in range(1,i+1)]
           s=''.join(l)
           space=n-k
           print (" "*space + s + " "*space)
           k=k+1
#end

       
        
            

        

            

                   
                

    